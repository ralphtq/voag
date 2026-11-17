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
| v2.0 SHACL (no OWL) | `http://voag.linkedmodel.org/2.0.0/schema/shacl/voag` | `2.0/schema/shacl/SCHEMA_voag_noOWL_v2.0.0.ttl` |

The IRIs are unchanged by the move out of `linkedmodels`. `schema/voag.ttl`
and `2.0/schema/SCHEMA_voag-v2.0.ttl` define the same terms. Apart from the
ontology IRI and `xsd:string` typing on literals, they differ only in the
graph metadata (`vaem:hasOwner` and `vaem:hasSteward` are set only in
`schema/voag.ttl`, and the description is worded differently) and in the
wording of one license label.

## Layout

```
schema/        current (unversioned) VOAG
1.1/           v1.1 schema and vocabulary
2.0/schema/    v2.0 schema
2.0/schema/shacl/  SHACL-only version of v2.0
2.0/refdata/   v2.0 license reference data
images/        logo
scripts/       parse check
```

## SHACL schema

`2.0/schema/shacl/SCHEMA_voag_noOWL_v2.0.0.ttl` is a SHACL-only version of
VOAG 2.0. It imports the SHACL schemas of VAEM
(`http://www.linkedmodel.org/3.0.0/schema/shacl/vaem`) and DTYPE
(`http://www.linkedmodel.org/2.0.0/schema/shacl/dtype`) rather than their OWL
versions.

## History

VOAG was previously maintained in
[ralphtq/linkedmodels](https://github.com/ralphtq/linkedmodels) under
`voag/voag.linkedmodel.org/`. Its full commit history was carried over when
it moved here.

## License

The ontology metadata names Linkedmodels as owner and steward. The license
for this repository is under review.
