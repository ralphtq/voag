# VOAG — Vocabulary for Ontology Attribution and Governance

VOAG is an OWL vocabulary for describing who owns, stewards, licenses and is
credited for an ontology or graph, and how it is governed. It includes a
catalogue of license types (Creative Commons and others) and the permissions
and requirements they carry. VOAG imports [VAEM](https://github.com/ralphtq/vaem)
and [DTYPE](https://github.com/ralphtq/dtype), and VAEM's own graph metadata
uses VOAG terms.

## IRIs

| What | IRI | File |
|---|---|---|
| Ontology (current) | `http://voag.linkedmodel.org/schema/voag` | `schema/voag.ttl` (v2.0) |
| Namespace | `http://voag.linkedmodel.org/voag/` (prefix `voag:`) | |
| v2.0 | `http://voag.linkedmodel.org/2.0/schema/voag` | `2.0/schema/SCHEMA_voag-v2.0.ttl` |
| v2.0 license reference data | `http://voag.linkedmodel.org/2.0/refdata/voag` | `2.0/refdata/REFDATA_voag-licenses-v2.0.ttl` |
| v1.1 | `http://voag.linkedmodel.org/1.1/schema/voag` | `1.1/schema/SCHEMA_voag-v1.1.ttl` |
| v1.1 vocabulary | `http://voag.linkedmodel.org/1.1/vocab/voag` | `1.1/vocab/VOCAB_voag-v1.1.ttl` |

The IRIs are unchanged by the move out of `linkedmodels`. `schema/voag.ttl`
has the same content as `2.0/schema/SCHEMA_voag-v2.0.ttl` apart from its
ontology IRI, `xsd:string` typing on literals, and the wording of one license
label.

## Layout

```
schema/        current (unversioned) VOAG
1.1/           v1.1 schema and vocabulary
2.0/schema/    v2.0 schema
2.0/refdata/   v2.0 license reference data
2.0/doc/       generated HTML documentation (2015)
2.0/swp/       SWP page for the license documentation (disabled, .ttlx)
images/        logo
```

## Work in progress

- `shacl-schemas`: SHACL-only (no OWL) version,
  `2.0/schema/shacl/SCHEMA_voag_noOWL_v2.0.0.ttl`. It merges cleanly into
  `main` and parses.

## History

VOAG was previously maintained in
[ralphtq/linkedmodels](https://github.com/ralphtq/linkedmodels) under
`voag/voag.linkedmodel.org/`. Its full commit history was carried over when
it moved here.

## License

The ontology metadata names TopQuadrant, Inc. as owner and steward. The
license for this repository is under review.
