"""Check a batch made by scripts/add_spdx_clauses.py.

Usage:
  python3 scripts/check_spdx_clauses.py SPEC.py BEFORE_DIR AFTER_DIR SPDX_TEXT_DIR SCHEMA.ttl

For each licence: every clause is a verbatim (whitespace-normalised) slice of the SPDX text,
in order, and the source words left over are only the stripped section numbers and headings;
the graph diff; one rdfs:isDefinedBy per construct, pointing at the licence's graph; the file
parses with $$VERSION$$ and $$RELEASE_DATE$$ filled in; and no new pySHACL results.
"""
import collections, importlib.util, logging, os, re, sys
import rdflib, pyshacl
from rdflib import RDF, RDFS, URIRef, Graph, Namespace
from rdflib.compare import graph_diff, to_isomorphic

logging.disable(logging.CRITICAL)
spec_path, in_dir, out_dir, text_dir, schema = sys.argv[1:6]
s = importlib.util.spec_from_file_location("spec", spec_path); spec = importlib.util.module_from_spec(s); s.loader.exec_module(spec)
V = Namespace("http://voag.linkedmodel.org/voag/"); SH = Namespace("http://www.w3.org/ns/shacl#")
DC = URIRef("http://purl.org/dc/terms/description")
S = Graph().parse(schema)
words = lambda x: re.sub(r"\s+", " ", x).strip().split(" ")


def results(g):
    _, rg, _ = pyshacl.validate(g + S, shacl_graph=S, inference="none", allow_warnings=True)
    return collections.Counter((str(rg.value(r, SH.sourceShape)).split("/")[-1], str(rg.value(r, SH.focusNode)).split("/")[-1])
                               for r in rg.subjects(RDF.type, SH.ValidationResult))


ok = True
for lic in spec.BATCH:
    name = f"REFDATA_voag-license-{lic['slug']}.ttl"
    before, after = Graph().parse(os.path.join(in_dir, name)), Graph().parse(os.path.join(out_dir, name))
    me = URIRef(f"http://voag.linkedmodel.org/$$VERSION$$/refdata/voag-license-{lic['slug']}")
    L = V[lic["iri"]]
    # 1. text: every clause is a verbatim (whitespace-normalised) slice of the source, in order, and
    #    the only source words not in a clause are the section numbers and headings that were stripped
    src = open(os.path.join(text_dir, lic["spdx"] + ".txt"), encoding="utf-8").read().split("\n")
    keep = [ln for ln in src[lic["clauses"][0]["start"] - 1:lic["end"] - 1]
            if ln.strip() not in ("NO WARRANTY", "END OF TERMS AND CONDITIONS")]
    region = " ".join(words(" ".join(keep)))
    cls = sorted(after.objects(L, V.hasClause), key=lambda c: int(after.value(c, V.clauseNumber)))
    pos, leftover = 0, []
    for c in cls:
        d = " ".join(words(str(after.value(c, DC))))
        i = region.find(d, pos)
        if i < 0:
            print("  TEXT MISMATCH", c); ok = False; continue
        leftover.append(region[pos:i].strip()); pos = i + len(d)
    leftover.append(region[pos:].strip())
    stray = [x for x in leftover if x]
    # 2. graph diff
    _, removed, added = graph_diff(to_isomorphic(before), to_isomorphic(after))
    rem = sorted({(str(s_).split('/')[-1], str(p).split('/')[-1].split('#')[-1]) for s_, p, o in removed})
    new_subj = {str(s_).split('/')[-1] for s_, p, o in added} - {str(s_).split('/')[-1] for s_, p, o in before}
    # 3. isDefinedBy: one per typed construct (other than the graph itself and dcterms terms), pointing at this graph
    bad = [x for x in set(after.subjects(RDF.type, None)) if x != me and not str(x).startswith("http://purl.org/dc/terms/")
           and list(after.objects(x, RDFS.isDefinedBy)) != [me]]
    # 4. placeholders
    txt = open(os.path.join(out_dir, name)).read().replace("$$VERSION$$", "2.0.0").replace("$$RELEASE_DATE$$", "2026-11-18")
    Graph().parse(data=txt, format="turtle")
    # 5. SHACL
    rb, ra = results(before), results(after)
    print(f"{lic['iri']:22} clauses={len(cls):2} unmatched-source={stray} removed={rem} new-subjects={len(new_subj)} "
          f"isDefinedBy-bad={len(bad)} shacl {sum(rb.values())}->{sum(ra.values())} gone={sorted(k[0] for k in rb - ra)} new={sorted(ra - rb)}")
    ok &= not bad and not (ra - rb)
print("ALL OK" if ok else "PROBLEMS")
