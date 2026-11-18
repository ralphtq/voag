"""Draft clause boundaries for an SPDX licence text: find the longest run of top-level numbered
sections (N. ...), numbered consecutively from 0 or 1, and propose a title for each.
Usage: python3 scripts/detect_spdx_sections.py TEXT_DIR ID [ID ...]   (prints JSON per licence)"""
import json, re, sys

text_dir, ids = sys.argv[1], sys.argv[2:]
SEC = re.compile(r"^\s{0,6}(?:Section\s+|ARTICLE\s+|Article\s+)?(\d{1,2})\.?\s+(\S.*)$")
END = re.compile(r"^\s*(END OF TERMS|EXHIBIT|Exhibit [A-Z]|APPENDIX|Appendix|How to Apply|ADDENDUM|Addendum|[A-Z][A-Za-z ]* Notice$)")


def heading(rest):
    """Return the section's own heading if the line starts with one."""
    rest = rest.strip()
    if len(rest) <= 90 and (rest.isupper() or not rest.endswith(".") or re.fullmatch(r"[A-Z][\w ,;:'’&/()-]*\.", rest)) \
            and len(rest.split()) <= 12 and not re.search(r"\b(shall|must|may|is|are|you|You)\b", rest):
        return rest.rstrip(".").strip()
    m = re.match(r"^([A-Z][\w ,;:'’&/()-]{2,70}?)\.\s+[A-Z“\"(]", rest)
    if m and len(m.group(1).split()) <= 10 and not re.search(r"\b(shall|must|may|is|are)\b", m.group(1)):
        return m.group(1).strip()
    return None


for id_ in ids:
    lines = open(f"{text_dir}/{id_}.txt", encoding="utf-8").read().split("\n")
    cands = [(i + 1, int(m.group(1)), m.group(2)) for i, ln in enumerate(lines) if (m := SEC.match(ln))]
    best = []
    for first in (0, 1):
        chain, want = [], first
        for ln, n, rest in cands:
            if n == want:
                chain.append((ln, n, rest)); want += 1
        if len(chain) > len(best):
            best = chain
    end = len(lines) + 1
    if best:
        for i in range(best[-1][0], len(lines)):
            if END.match(lines[i]):
                end = i + 1; break
    secs = [dict(num=n, start=ln, heading=heading(rest), line=rest[:70]) for ln, n, rest in best]
    print(json.dumps(dict(id=id_, lines=len(lines), end=end, sections=secs)))
