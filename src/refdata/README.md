# License reference data

This folder is the source of VOAG's license reference data. It is not part of a
release yet; `2.0/refdata/` holds the published v2.0 data.

## Layout

Each license has its own graph, in `REFDATA_voag-license-<slug>.ttl`, with the
graph IRI `http://voag.linkedmodel.org/$$VERSION$$/refdata/voag-license-<slug>`.
A license graph is standalone: it imports only the VOAG SHACL schema, and holds
the `voag:License`, its clauses, its own `vaem:GraphMetaData`, and copies of the
`dcterms:` property declarations its metadata uses.

`REFDATA_voag-licenses.ttl` is the collection graph. It holds the collection's
metadata and logos and imports all the license graphs.

The slug is the license's local name in lower case, with `-license` dropped and
`_` turned into `-`. `UNLICENSE` is `unlicense`, `UtahPublicLicense` is
`utah-public`, and `ZOPE-PUBLICE-LICENSE_V1` is `zope-public-v1`.

## Clauses

A license's clauses are `voag:Clause` individuals (or subclasses), linked with
`voag:hasClause` and named `CLS_<license>-NN`, where `NN` is the license's own
section number. Each has a `voag:title`, a `voag:clauseNumber` and the clause
text, verbatim, in `dcterms:description`.

- **CC BY 4.0**: from the Creative Commons legal code, which Creative Commons
  dedicates to the public domain under CC0.
- **AFL, CC BY-SA 3.0 US, GPL and Perl Artistic 2.0**: from the v2.0 data.
- **Every other license with clauses**: from the texts of the
  [SPDX License List](https://github.com/spdx/license-list-data), by
  `scripts/add_spdx_clauses.py`. Each batch's clause boundaries are in
  `scripts/spdx_clause_specs/`, and `scripts/check_spdx_clauses.py` checks that
  every clause is a verbatim slice of the SPDX text. The graph's metadata cites
  the SPDX page as `dcterms:source`.

## Licenses without clauses

These 20 licenses have no clauses yet, so they fail the `sh:minCount 1` of
`voag:License-hasClause`. Each needs a source for its text. To add clauses from
a file you supply, put the text in a `<SPDX-style id>.txt` file, write a spec
for it and run the scripts above.

### SPDX has a text, but it was not used

| License | Slug | SPDX | Why not used |
|---|---|---|---|
| `FREE-ART-LICENSE` Free Art License | `free-art` | `LAL-1.3` | SPDX has only the French text. |
| `ECOS_V2PT0` eCos license version 2.0 | `ecos-v2pt0` | `eCos-2.0` | Deprecated in SPDX, which has no text for it; SPDX now writes it as GPL with `eCos-exception-2.0`. |

### Not on the SPDX License List

| License | Slug | Note |
|---|---|---|
| `CRYPTIX-GENERAL-LICENSE` Cryptix General License | `cryptix-general` | |
| `DSL-LICENSE` Design Science License (DSL) | `dsl` | |
| `GNU-VERBATIM-COPYING-LICENSE` GNU Verbatim Copying License | `gnu-verbatim-copying` | A one-sentence permission notice, not a full license. |
| `GPLPA` GPL for Computer Programs of the Public Administration | `gplpa` | |
| `HESSLA` Hacktivismo Enhanced-Source Software License Agreement | `hessla` | |
| `JAHIA-COMMUNITY-SOURCE-LICENSE` Jahia Community Source License | `jahia-community-source` | |
| `JOSL_V1PT0` Jabber Open Source License, Version 1.0 | `josl-v1pt0` | |
| `MS-LRL` Microsoft Limited Reciprocal License (Ms-LRL) | `ms-lrl` | |
| `MS-RRL` Microsoft Reference License | `ms-rrl` | |
| `MS-SSL` Microsoft's Shared Source CLI, C#, and Jscript License | `ms-ssl` | |
| `OCL` Open Content License, Version 1.0 | `ocl` | SPDX's `OCLC-2.0` is a different license. |
| `OPEN-DIRECTORY-LICENSE` Open Directory License (aka dmoz.org License) | `open-directory` | |
| `PHORUM-LICENSE_V2PT0` Phorum License, Version 2.0 | `phorum-v2pt0` | |
| `SML` Simple Machines License | `sml` | |
| `SYSTEMC_V3PT0` SystemC "Open Source" License, Version 3.0 | `systemc-v3pt0` | |
| `UtahPublicLicense` University of Utah Public License | `utah-public` | |
| `WEBM-LICENSE` License of WebM | `webm` | |
| `ZOPE-PUBLICE-LICENSE_V1` Zope Public License version 1 | `zope-public-v1` | SPDX has only `ZPL-1.1`. The IRI has a typo (`PUBLICE`). |

## Known data issues

- `APSL_V1PT0` is labelled "Apple's Common Documentation License, Version 1.0",
  the same label as `ACDL_V1PT0`. Its clauses are from SPDX's `APSL-1.0`, and
  `ACDL_V1PT0`'s from SPDX's `CDL-1.0`.
- `GNU-GPL` carries the GPL v3 clauses, which are defined in the `gnu-gpl-v3`
  graph and copied into `gnu-gpl`.
- `voag:url` values are typed `xsd:anyURI` only for the licenses that have
  clauses from SPDX. Some of the other URLs point at sites that no longer exist.
