"""Minimal Newick parser for Glottolog classification.nex.
Returns (nodes, leaves): nodes = {glottocode: (level, name)} for all
labeled internal nodes; leaves = {leaf_glottocode: family_glottocode}
where family is the nearest ancestor with level=='family' (None if isolate).
"""
import re

KV_RE = re.compile(r"(\w+):((?:[^,\\\]]|\\.)+?)(?=(?:,)|$)")

def parse_newick(text):
    pos = [0]
    n = len(text)
    nodes, leaves = {}, {}
    fam_stack = [None]

    def skip_ws():
        while pos[0] < n and text[pos[0]] in " \t\n":
            pos[0] += 1

    def parse_kv(lab_text):
        kv = {}
        for m in KV_RE.finditer(lab_text.strip().lstrip("&").strip().strip("[]")):
            kv[m.group(1)] = m.group(2).replace("\\,", ",")
        return kv

    def read_label():
        if pos[0] < n and text[pos[0]] == "[":
            depth, i = 0, pos[0]
            while i < n:
                if text[i] == "[":
                    depth += 1
                elif text[i] == "]":
                    depth -= 1
                    if depth == 0:
                        break
                i += 1
            lab = text[pos[0] + 1:i]
            pos[0] = i + 1
            return parse_kv(lab)
        return {}

    def find_matching(i):
        depth = 0
        while i < n:
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    return i
            i += 1
        raise ValueError("unbalanced newick")

    def rec():
        skip_ws()
        if text[pos[0]] == "(":
            j = find_matching(pos[0])
            lab = text[pos[0] + 1:j]
            kv = parse_kv(lab)
            gc = kv.get("glottocode", "")
            nodes[gc] = (kv.get("level"), kv.get("name"))
            cur = gc if kv.get("level") == "family" else fam_stack[-1]
            pos[0] += 1
            fam_stack.append(cur)
            while True:
                rec()
                skip_ws()
                c = text[pos[0]]
                pos[0] += 1
                if c == ",":
                    continue
                if c == ")":
                    break
                raise ValueError(f"bad newick at {pos[0]}")
            fam_stack.pop()
            read_label()
            return
        m = re.match(r"[^,;\[\)\(\s]+", text[pos[0]:])
        if not m:
            raise ValueError(f"bad newick at {pos[0]}")
        leaf = m.group(0)
        pos[0] += len(leaf)
        read_label()
        leaves[leaf] = fam_stack[-1]

    rec()
    return nodes, leaves
