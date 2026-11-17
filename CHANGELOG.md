# Changelog

## Unreleased

- Moved VOAG out of `ralphtq/linkedmodels` into its own repository, with its
  full commit history. IRIs are unchanged.
- Linkedmodels is now the owner and steward, with `voag:LinkedModelsAttribution`
  and `voag:LinkedModelsLogo` replacing the TopQuadrant attribution and logo.
- Removed the local `void:Dataset` class and the import of VoID;
  `voag:Graph` is now a direct subclass of `voag:GovernedObject`.
- Added `voag:distributionClause` for a license's distribution clause.
- Every construct has a single `rdfs:isDefinedBy`.
- Removed the generated 2015 HTML documentation and the disabled SWP page.
- Added the SHACL-only schema `2.0/schema/shacl/SCHEMA_voag_noOWL_v2.0.0.ttl`,
  which imports the VAEM and DTYPE SHACL schemas.
- Added a GitHub Action that checks every Turtle and RDF/XML file parses.
