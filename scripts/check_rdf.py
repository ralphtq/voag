"""Parse every RDF file in the repository and fail if any does not parse.

Turtle: *.ttl. RDF/XML: *.rdf, *.owl, and extensionless files that start
with an XML declaration (such as schema/dtype).
"""
import pathlib
import sys

import rdflib


def rdf_format(path):
    if path.suffix == ".ttl":
        return "turtle"
    if path.suffix in (".rdf", ".owl"):
        return "xml"
    if path.suffix == "" and path.is_file():
        with path.open("rb") as handle:
            if handle.read(5) == b"<?xml":
                return "xml"
    return None


failed = 0
for path in sorted(pathlib.Path(".").rglob("*")):
    if path.name.startswith(".") or ".git" in path.parts or not path.is_file():
        continue
    fmt = rdf_format(path)
    if fmt is None:
        continue
    try:
        graph = rdflib.Graph().parse(path, format=fmt)
        print(f"ok    {len(graph):6d} triples  {path}")
    except Exception as exc:  # noqa: BLE001
        failed += 1
        print(f"FAIL  {path}: {exc}")
sys.exit(1 if failed else 0)
