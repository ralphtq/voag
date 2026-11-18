"""Add clauses taken from SPDX licence texts to VOAG per-licence refdata graphs.

Usage:
  python3 scripts/add_spdx_clauses.py SPEC.py IN_DIR OUT_DIR SPDX_TEXT_DIR

SPEC.py defines BATCH, a list of licences (see scripts/spdx_clause_specs/). Each gives the
licence IRI local name, its refdata file slug, its SPDX identifier, the clause IRI prefix,
and the clauses as line numbers in the SPDX text, with title and VOAG clause class.
A clause's "num" is the licence's own section number, stripped from the text with the
section's heading; an unnumbered section can name a "heading" line to drop instead, and
"n" sets the clause number explicitly (otherwise unnumbered clauses count from 1).

SPDX_TEXT_DIR holds <SPDX-ID>.txt files from
  https://raw.githubusercontent.com/spdx/license-list-data/main/text/<SPDX-ID>.txt

For each licence the script adds the clauses (text copied from the SPDX file, with hard
line wraps rejoined and list items kept on their own lines), links them with
voag:hasClause, types voag:url as xsd:anyURI (replacing it if the spec gives "url"),
and adds the SPDX page as dcterms:source on the graph's GraphMetaData.
Check the result with scripts/check_spdx_clauses.py.
"""
import importlib.util, os, re, sys

spec_path, in_dir, out_dir, text_dir = sys.argv[1:5]
s = importlib.util.spec_from_file_location("spec", spec_path)
spec = importlib.util.module_from_spec(s)
s.loader.exec_module(spec)

# list-item markers: (a) a) a. A. 1. 1) 1.1. (i) iv. - *
ITEM = re.compile(r"^(\(?([a-zA-Z]|\d{1,3}(\.\d{1,3})*|[ivx]{1,5})[.)]|-|\*)\s")
DROP_LINES = re.compile(r"^(NO WARRANTY|END OF TERMS AND CONDITIONS)$")


def reflow(lines):
    """Rejoin hard-wrapped lines; keep blank-line paragraphs and list items on their own lines."""
    paras, cur = [], []
    for raw in lines:
        line = raw.strip()
        if not line:
            if cur:
                paras.append(cur)
                cur = []
            continue
        if DROP_LINES.match(line):
            continue
        if cur and not ITEM.match(line):
            cur[-1] = cur[-1] + " " + line
        else:
            cur.append(line)
    if cur:
        paras.append(cur)
    text = "\n\n".join("\n".join(p) for p in paras)
    return re.sub(r"[ \t]+", " ", text).strip()


def strip_heading(lines, num, title, heading=None):
    """On the section's first source line, remove 'N.' and the section's own heading (if it has one).
    For an unnumbered section, `heading` is the text of a heading line to drop."""
    lines = list(lines)
    first = lines[0].strip()
    if num is None:
        if heading is not None:
            if first.lower() != heading.lower():
                raise SystemExit(f"expected heading {heading!r}, found {first[:60]!r}")
            lines[0] = ""
        return lines
    m = re.match(r"^%s\.\s*" % re.escape(str(num)), first)
    if not m:
        raise SystemExit(f"section {num} does not start with its number: {first[:60]!r}")
    rest = first[m.end():]
    if rest.rstrip(".").strip().lower() == title.lower():
        rest = ""                                   # heading on a line of its own
    elif rest.lower().startswith(title.lower() + ". "):
        rest = rest[len(title) + 2:]                # inline heading: "N. Title. Body..."
    lines[0] = rest
    return lines


def lit(text):
    t = text.replace("\\", "\\\\")
    if "\n" in t or '"' in t:
        if t.endswith('"'):
            t = t[:-1] + '\\"'
        return '"""' + t.replace('"""', '\\"\\"\\"') + '"""'
    return '"' + t + '"'


def split_statements(body):
    stmts, i, start, inq = [], 0, 0, False
    while i < len(body):
        if body.startswith('"""', i):
            inq = not inq
            i += 3
            continue
        if not inq and body.startswith(" .\n", i):
            end = i + 3
            while body.startswith("\n", end):
                end += 1
            stmts.append(body[start:end])
            start = i = end
            continue
        i += 1
    assert "".join(stmts) == body
    return stmts


for lic in spec.BATCH:
    path = os.path.join(in_dir, f"REFDATA_voag-license-{lic['slug']}.ttl")
    t = open(path, encoding="utf-8").read()
    graph = f"<http://voag.linkedmodel.org/$$VERSION$$/refdata/voag-license-{lic['slug']}>"
    src = open(os.path.join(text_dir, lic["spdx"] + ".txt"), encoding="utf-8").read().split("\n")
    cut = t.index("\n\n") + 2
    prefixes, stmts = t[:cut], split_statements(t[cut:])
    subj = lambda st: st.split("\n", 1)[0].strip()
    idx = {subj(st): n for n, st in enumerate(stmts)}
    L = f"voag:{lic['iri']}"
    lic_stmt = stmts[idx[L]]
    assert "voag:hasClause" not in lic_stmt, L
    label = re.search(r'\n  rdfs:label "((?:[^"\\]|\\.)*)"', lic_stmt).group(1)

    clauses = lic["clauses"]
    blocks, links = [], []
    for k, c in enumerate(clauses):
        start = c["start"]
        end = clauses[k + 1]["start"] if k + 1 < len(clauses) else lic["end"]
        text = reflow(strip_heading(src[start - 1:end - 1], c.get("num"), c["title"], c.get("heading")))
        assert text, (L, c)
        n = c.get("n", c.get("num") if c.get("num") is not None else k + 1)
        cid = f"voag:CLS_{lic['clause_prefix']}-{int(n):02d}"
        links.append(cid)
        blocks.append(
            f"{cid}\n"
            f"  a voag:{c['cls']} ;\n"
            f"  dcterms:description {lit(text)} ;\n"
            f"  rdfs:isDefinedBy {graph} ;\n"
            f"  rdfs:label {lit(label + ' - ' + c['title'])} ;\n"
            f"  voag:clauseNumber {int(n)} ;\n"
            f"  voag:title {lit(c['title'])} .\n\n"
        )

    # licence: hasClause links; url fix and xsd:anyURI typing
    lines = lic_stmt.rstrip("\n").split("\n")
    url_i = [n for n, ln in enumerate(lines) if ln.startswith("  voag:url ")]
    assert len(url_i) == 1, L
    old_url = re.match(r'  voag:url "([^"]*)"(\^\^xsd:anyURI)?', lines[url_i[0]]).group(1)
    new_url = lic.get("url", old_url)
    end_char = lines[url_i[0]][-1]
    lines[url_i[0]] = f'  voag:url "{new_url}"^^xsd:anyURI {end_char}'
    # insert hasClause before the first top-level predicate sorting after it
    # (voag:url always exists and sorts after it, so a position is always found)
    ins, inq = None, False
    for n, ln in enumerate(lines[1:], 1):
        before = inq
        inq ^= ln.count('"""') % 2 == 1
        if not before and re.match(r"  [a-z]+:\S+ ", ln) and ln.split()[0] > "voag:hasClause":
            ins = n
            break
    lines[ins:ins] = [f"  voag:hasClause {c} ;" for c in links]
    stmts[idx[L]] = "\n".join(lines) + "\n\n"

    # GMD: SPDX as a source, and a credit sentence
    G = [k for k in idx if k.startswith("voag:GMD_")][0]
    g = stmts[idx[G]]
    d_old = re.search(r'  dcterms:description "((?:[^"\\]|\\.)*)" ;\n', g)
    g = g.replace(d_old.group(0), f'  dcterms:description "{d_old.group(1)} The clause text is taken from the SPDX License List ({lic["spdx"]})." ;\n')
    m = '  dcterms:modified "$$RELEASE_DATE$$"^^xsd:date ;\n'
    assert g.count(m) == 1
    g = g.replace(m, m + f'  dcterms:source <https://spdx.org/licenses/{lic["spdx"]}.html> ;\n')
    stmts[idx[G]] = g

    # clauses go after the licence, before the GMD
    out = prefixes + "".join(stmts[: idx[L] + 1]) + "".join(blocks) + "".join(stmts[idx[L] + 1:])
    out = out.rstrip("\n") + "\n"
    open(os.path.join(out_dir, os.path.basename(path)), "w", encoding="utf-8").write(out)
    print(f"{lic['iri']:32} {lic['spdx']:15} clauses={len(links):2}  url {'changed' if new_url != old_url else 'kept'}")
