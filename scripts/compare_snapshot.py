"""Check that a release build says the same as the snapshot it was promoted from.

  python3 scripts/compare_snapshot.py <snapshot-dir> <release-dir> <snapshot-version> <release-version>

Each file in the snapshot build is paired with the release file of the same
name (the version in the path replaced). In the snapshot graph, the snapshot
version (e.g. 3.0.0-SNAPSHOT) is replaced by the release version in every IRI
and literal. Triples whose predicate is listed in "compare_ignore" in
release.json are left out of the comparison (by default vaem:releaseDate and
dcterms:modified, which carry the build date). Any other difference is
reported and the exit status is 1.
"""
import json
import pathlib
import sys

import rdflib
from rdflib import Literal, URIRef
from rdflib.compare import graph_diff, to_isomorphic

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_IGNORED = [
    "http://www.linkedmodel.org/schema/vaem#releaseDate",
    "http://purl.org/dc/terms/modified",
]
_config = json.loads((ROOT / "release.json").read_text(encoding="utf-8"))
IGNORED = {URIRef(p) for p in _config.get("compare_ignore", DEFAULT_IGNORED)}


def renamed(term, old, new):
    if isinstance(term, URIRef):
        return URIRef(str(term).replace(old, new))
    if isinstance(term, Literal):
        return Literal(str(term).replace(old, new), lang=term.language, datatype=term.datatype)
    return term


def load(path, old=None, new=None):
    graph, out = rdflib.Graph().parse(path, format="turtle"), rdflib.Graph()
    for s, p, o in graph:
        if p in IGNORED:
            continue
        if old:
            s, p, o = (renamed(t, old, new) for t in (s, p, o))
        out.add((s, p, o))
    return out


def main():
    snap_dir, rel_dir, snap_version, rel_version = sys.argv[1:5]
    snap_dir, rel_dir = pathlib.Path(snap_dir), pathlib.Path(rel_dir)
    problems = 0
    snap_files = sorted(snap_dir.rglob("*.ttl"))
    if not snap_files:
        sys.exit(f"no .ttl files in {snap_dir}")
    for snap in snap_files:
        rel = rel_dir / str(snap.relative_to(snap_dir)).replace(snap_version, rel_version)
        if not rel.exists():
            print(f"missing in the release: {rel.relative_to(rel_dir)}")
            problems += 1
            continue
        _, only_snap, only_rel = graph_diff(to_isomorphic(load(snap, snap_version, rel_version)),
                                            to_isomorphic(load(rel)))
        for label, triples in (("only in the snapshot", only_snap), ("only in the release", only_rel)):
            for t in sorted(triples, key=str)[:20]:
                print(f"{rel.name}: {label}: {' '.join(str(x)[:80] for x in t)}")
        problems += len(only_snap) + len(only_rel)
        print(f"{rel.relative_to(rel_dir)}: {'same as the snapshot' if not (only_snap or only_rel) else 'DIFFERS from the snapshot'}")
    rel_count = len(list(rel_dir.rglob("*.ttl")))
    if rel_count != len(snap_files):
        print(f"the release has {rel_count} .ttl files, the snapshot {len(snap_files)}")
        problems += 1
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
