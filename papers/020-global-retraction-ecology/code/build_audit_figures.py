#!/usr/bin/env python3
"""Render compact SVG audit figures directly from the frozen RWDB audit JSON."""
from __future__ import annotations
import argparse,html,json
from pathlib import Path

def esc(x): return html.escape(str(x))
def svg(title,subtitle,body,w=1200,h=650):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<title>{esc(title)}</title><rect width="{w}" height="{h}" fill="#fff"/>
<style>text{{font-family:Inter,Arial,sans-serif;fill:#1f2937}}.t{{font-size:30px;font-weight:700}}.s{{font-size:15px;fill:#6b7280}}.lab{{font-size:12px;fill:#6b7280}}.v{{font-size:11px;font-weight:700}}.bar{{fill:#667085}}.partial{{fill:#b6bac2}}.axis{{stroke:#d1d5db;stroke-width:1}}</style>
<text x="70" y="55" class="t">{esc(title)}</text><text x="70" y="82" class="s">{esc(subtitle)}</text>{body}</svg>'''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("audit_json",type=Path)
    ap.add_argument("--out-dir",type=Path,default=Path("papers/020-global-retraction-ecology/figures"))
    args=ap.parse_args()
    d=json.loads(args.audit_json.read_text(encoding="utf-8")); args.out_dir.mkdir(parents=True,exist_ok=True)

    counts=d["dates"]["recent_retraction_counts"]; peak=max(counts.values())
    bars=['<line x1="70" y1="540" x2="1140" y2="540" class="axis"/>']
    for i,(year,n) in enumerate(counts.items()):
        x=82+i*70; bh=round(n/peak*410); y=540-bh
        cls="partial" if year=="2026" else "bar"
        label=year+"*" if year=="2026" else year
        bars += [f'<rect x="{x}" y="{y}" width="44" height="{bh}" rx="4" class="{cls}"/>',
                 f'<text x="{x+22}" y="{y-8}" text-anchor="middle" class="v">{n:,}</text>',
                 f'<text x="{x+22}" y="565" text-anchor="middle" class="lab">{label}</text>']
    bars.append('<text x="70" y="615" class="s">2026 incomplete. Counts are not rates; spikes require event/publisher decomposition.</text>')
    (args.out_dir/"fig01_recent_retractions.svg").write_text(svg("Recorded Retractions by Retraction Year","Retraction Watch snapshot · descriptive counts","".join(bars)),encoding="utf-8")

    reasons=d["top_reason_labels"][:10]; mx=reasons[0][1]; body=[]
    for i,(label,n) in enumerate(reasons):
        y=125+i*48; bw=round(n/mx*650)
        body += [f'<text x="55" y="{y+18}" class="lab">{esc(label[:48])}</text>',
                 f'<rect x="470" y="{y}" width="{bw}" height="28" rx="4" class="bar"/>',
                 f'<text x="{480+bw}" y="{y+18}" class="v">{n:,}</text>']
    body.append('<text x="55" y="630" class="s">Reason is multi-label; bars are not mutually exclusive causes.</text>')
    (args.out_dir/"fig03_top_reason_labels.svg").write_text(svg("High-frequency RWDB Reason Labels","Multi-label descriptive prevalence","".join(body),1200,670),encoding="utf-8")
    print(args.out_dir)

if __name__=="__main__":
    main()
