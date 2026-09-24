#!/usr/bin/env python3
"""Map RWDB atomic Reason labels onto orthogonal analytical facets.

The mapping supplements rather than replaces the official RWDB labels.
Every input label is preserved verbatim and may receive multiple facet values.
"""
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

RULES={
"affected_object":[
 ("data",r"data"),("image",r"image"),("results_conclusions",r"results?|conclusions?"),
 ("text",r"text"),("methods_analysis",r"methods?|analys"),("materials",r"materials?|cell lines?|tissues?"),
 ("authorship_affiliation",r"authorship|affiliation"),("peer_review",r"peer review"),
 ("references_attributions",r"referenc|attribution|cites retracted work"),("human_subjects",r"human subject|patient consent|informed"),
 ("animal_subjects",r"animal welfare|iacuc"),("article_general",r"about article|of/in article")
],
"mechanism":[
 ("error",r"^error|through error"),("unreliability",r"unreliable"),("duplication",r"duplication"),
 ("plagiarism",r"plagiarism|taken from dissertation|taken via peer review|taken via translation"),
 ("falsification_fabrication",r"falsification|fabrication"),("manipulation",r"manipulation"),
 ("paper_mill",r"paper mill"),("computer_generated",r"computer-aided|computer-generated"),
 ("hoax",r"hoax paper"),("peer_review_compromise",r"compromised peer review|fake peer review"),
 ("nonreproducibility",r"not reproducible"),("contamination",r"contamination"),
 ("sabotage",r"sabotage"),("salami_slicing",r"salami slicing"),("bias_balance",r"bias issues|lack of balance"),
 ("false_identity",r"false/forged"),("misconduct_explicit",r"misconduct")
],
"ethics_compliance":[
 ("irb_iacuc",r"irb|iacuc"),("consent",r"consent"),("welfare",r"welfare"),
 ("conflict_of_interest",r"conflict of interest"),("copyright_ownership",r"copyright|ownership"),
 ("policy_breach",r"breach of policy"),("ethical_violation",r"ethical violations"),
 ("approval",r"lack of approval"),("legal",r"legal reasons|civil proceedings|criminal proceedings"),
 ("fees",r"nonpayment of fees|refusal to pay")
],
"process_actor":[
 ("journal_publisher_investigation",r"investigation by journal/publisher"),
 ("institution_company_investigation",r"investigation by company/institution"),
 ("ori_investigation",r"investigation by ori"),("third_party_investigation",r"investigation by third party"),
 ("author_objection",r"objections? by author"),("institution_objection",r"objections? by company/institution"),
 ("third_party_objection",r"objections? by third party"),("author_unresponsive",r"author unresponsive"),
 ("miscommunication_author",r"miscommunication with/by author"),
 ("miscommunication_institution",r"miscommunication with/by company/institution"),
 ("miscommunication_publisher",r"miscommunication with/by journal/publisher"),
 ("miscommunication_third_party",r"miscommunication (?:with/)?by third party|miscommunication with/by third party"),
 ("publisher_error",r"error by journal/publisher|duplication of content through error by journal/publisher"),
 ("third_party_error",r"error by third party"),("rogue_editor",r"rogue editor"),
 ("complaint_author",r"complaints about author"),("complaint_institution",r"complaints about company/institution"),
 ("complaint_third_party",r"complaints about third party"),("third_party_involvement",r"third party involvement"),("commendable_response",r"doing the right thing")
],
"notice_lifecycle":[
 ("notice_absent",r"notice.+lack of"),("notice_limited",r"notice.+limited or no information"),
 ("notice_inaccessible",r"notice.+unable to access"),("removed",r"^removed$"),
 ("temporary_removal",r"temporary removal"),("retract_replace",r"retract and replace"),
 ("updated_correction",r"updated to correction"),("updated_eoc",r"updated to expression of concern"),
 ("updated_retraction",r"updated to retraction"),("prior_notice_update",r"upgrade/update of prior notice"),
 ("eoc_lifted",r"eoc lifted"),("no_further_action",r"no further action"),
 ("withdrawn_outdated",r"withdrawn as out of date"),
 ("withdrawn_republish",r"withdrawn to publish in different journal"),
 ("transfer_ownership",r"transfer of copyright|ownership"),("publishing_ban",r"publishing ban"),
 ("date_unknown",r"date of article and/or notice unknown"),("conference_nonpresentation",r"not presented at conference"),("citation_of_retracted_work",r"cites retracted work")
]
}

def matches(label,patterns):
    text=label.lower()
    return [name for name,pat in patterns if re.search(pat,text,re.I)]

def evidence_specificity(label:str, facets:dict)->str:
    low=label.lower()
    if re.search(r"notice.+(limited|lack|unable)|date of article and/or notice unknown",low):
        return "limited_or_unknown"
    if facets["notice_lifecycle"] or facets["process_actor"]:
        substantive=bool(facets["affected_object"] or facets["mechanism"] or facets["ethics_compliance"])
        return "mixed_procedural_and_substantive" if substantive else "procedural_or_lifecycle"
    if re.search(r"misconduct|ethical violations|breach of policy",low):
        return "broad_integrity_statement"
    if facets["affected_object"] or facets["mechanism"] or facets["ethics_compliance"]:
        return "specific_or_domain_issue"
    return "unclassified"

def map_label(label:str)->dict:
    facets={name:matches(label,pats) for name,pats in RULES.items()}
    return {"reason_raw":label,**facets,"evidence_specificity":evidence_specificity(label,facets)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("reason_nodes_csv",type=Path)
    ap.add_argument("--out",type=Path,default=Path("papers/020-global-retraction-ecology/data/derived/reason_ontology_v1.json"))
    args=ap.parse_args()
    labels=[]
    with args.reason_nodes_csv.open("r",encoding="utf-8",newline="") as fh:
        labels=[row["reason"] for row in csv.DictReader(fh)]
    mapped=[map_label(x) for x in labels]
    unmapped=[x["reason_raw"] for x in mapped if x["evidence_specificity"]=="unclassified"]
    payload={
      "schema_version":1,
      "mapping_version":"v1-rule-based-draft",
      "principle":"orthogonal facets supplement, never replace, the official RWDB atomic label",
      "rows":mapped,
      "unmapped_labels":unmapped,
      "gate":"No manuscript facet result until unmapped_labels is empty and manual audit is frozen."
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"labels":len(labels),"unmapped":len(unmapped),"unmapped_labels":unmapped},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
