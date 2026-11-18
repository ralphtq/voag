# Batch 2: clause boundaries are line numbers in the SPDX text files (text/<spdx>.txt).
# "num" is the licence's own section number; "heading" is an unnumbered heading line to drop;
# "n" sets the clause number; "end" is the first line after the last clause; "url" replaces voag:url.

GPL2_STYLE = [  # AGPL-1.0 follows the GPL-2.0 text section by section
    ("Scope and Definitions", "DefinitionClause"), ("Verbatim Copies", "DistributionClause"),
    ("Modified Works", "ModificationClause"), ("Object Code and Executable Form", "DistributionClause"),
    ("Termination", "TerminationClause"), ("Acceptance", "Clause"), ("Downstream Recipients", "GrantClause"),
    ("Conditions Imposed by Court Order or Patent Allegation", "RestrictionsClause"),
    ("Geographical Restrictions", "RestrictionsClause"), ("Revised Versions", "VersionClause"),
    ("Incorporation into Other Free Programs", "MiscClause"), ("No Warranty", "DisclaimerClause"),
    ("Limitation of Liability", "LimitationOfLiabilityClause"),
]

CC_2 = [  # Creative Commons 2.0 and 3.0 legal code, sections 1-8
    ("Definitions", "DefinitionClause"), ("Fair Use Rights", "RightToUseClause"), ("License Grant", "GrantClause"),
    ("Restrictions", "RestrictionsClause"), ("Representations, Warranties and Disclaimer", "DisclaimerClause"),
    ("Limitation on Liability", "LimitationOfLiabilityClause"), ("Termination", "TerminationClause"),
    ("Miscellaneous", "MiscClause"),
]


def numbered(starts, sections, first=0):
    return [dict(num=first + i, start=s, title=t, cls=c) for i, (s, (t, c)) in enumerate(zip(starts, sections))]


BATCH = [
    dict(iri="APACHE_V1PT0", slug="apache-v1pt0", spdx="Apache-1.0", clause_prefix="APACHE_V1PT0", end=20, clauses=[
        dict(start=3, title="Redistribution and Use", cls="DistributionClause"),
        dict(start=9, title="Advertising Acknowledgment", cls="AttributionRightsClause"),
        dict(start=11, title="Endorsement", cls="RestrictionsClause"),
        dict(start=13, title="Use of the Apache Name", cls="RestrictionsClause"),
        dict(start=15, title="Acknowledgment in Redistributions", cls="AttributionRightsClause"),
        dict(start=18, title="Disclaimer", cls="DisclaimerClause"),
    ]),
    dict(iri="APACHE_V1PT1", slug="apache-v1pt1", spdx="Apache-1.1", clause_prefix="APACHE_V1PT1", end=20, clauses=[
        dict(start=5, title="Redistribution and Use", cls="DistributionClause"),
        dict(start=11, title="End-User Acknowledgment", cls="AttributionRightsClause"),
        dict(start=15, title="Endorsement", cls="RestrictionsClause"),
        dict(start=17, title="Use of the Apache Name", cls="RestrictionsClause"),
        dict(start=19, title="Disclaimer", cls="DisclaimerClause"),
    ]),
    dict(iri="AGPL_V1PT0", slug="agpl-v1pt0", spdx="AGPL-1.0-only", clause_prefix="AGPL_V1PT0", end=87,
         clauses=numbered([28, 32, 36, 49, 58, 60, 62, 64, 72, 74, 80, 84, 86], GPL2_STYLE)),
    dict(iri="AGPL_V3PT0", slug="agpl-v3pt0", spdx="AGPL-3.0-only", clause_prefix="AGPL_V3PT0", end=214,
         clauses=numbered([28, 46, 60, 67, 72, 77, 90, 115, 140, 150, 154, 162, 181, 186, 192, 202, 206, 210], [
             ("Definitions", "DefinitionClause"), ("Source Code", "DefinitionClause"),
             ("Basic Permissions", "GrantClause"),
             ("Protecting Users' Legal Rights From Anti-Circumvention Law", "ProtectionClause"),
             ("Conveying Verbatim Copies", "DistributionClause"), ("Conveying Modified Source Versions", "ModificationClause"),
             ("Conveying Non-Source Forms", "DistributionClause"), ("Additional Terms", "AdditionalClause"),
             ("Termination", "TerminationClause"), ("Acceptance Not Required for Having Copies", "Clause"),
             ("Automatic Licensing of Downstream Recipients", "GrantClause"), ("Patents", "PatentGrantClause"),
             ("No Surrender of Others' Freedom", "RestrictionsClause"),
             ("Remote Network Interaction; Use with the GNU General Public License", "UsageClause"),
             ("Revised Versions of this License", "VersionClause"), ("Disclaimer of Warranty", "DisclaimerClause"),
             ("Limitation of Liability", "LimitationOfLiabilityClause"),
             ("Interpretation of Sections 15 and 16", "MiscClause")])),
    dict(iri="CC0", slug="cc0", spdx="CC0-1.0", clause_prefix="CC0", end=122, clauses=[
        dict(n=0, start=14, heading="Statement of Purpose", title="Statement of Purpose", cls="Clause"),
        dict(num=1, start=40, title="Copyright and Related Rights", cls="DefinitionClause"),
        dict(num=2, start=63, title="Waiver", cls="Clause"),
        dict(num=3, start=80, title="Public License Fallback", cls="GrantClause"),
        dict(num=4, start=102, title="Limitations and Disclaimers", cls="DisclaimerClause"),
    ]),
    dict(iri="CCBY-LICENSE", slug="ccby", spdx="CC-BY-2.0", clause_prefix="CCBY-2PT0", end=77,
         clauses=numbered([11, 25, 27, 47, 53, 57, 59, 65], CC_2, first=1)),
    dict(iri="CCBY-SA", slug="ccby-sa", spdx="CC-BY-SA-2.0", clause_prefix="CCBY-SA-2PT0", end=81,
         clauses=numbered([11, 27, 29, 49, 57, 61, 63, 69], CC_2, first=1)),
    dict(iri="CCBY-ND", slug="ccby-nd", spdx="CC-BY-ND-3.0", clause_prefix="CCBY-ND-3PT0", end=272,
         clauses=numbered([25, 103, 108, 143, 199, 210, 216, 235],
                          [CC_2[0], ("Fair Dealing Rights", "RightToUseClause")] + CC_2[2:], first=1)),
    dict(iri="CDDL_V1PT0", slug="cddl-v1pt0", spdx="CDDL-1.0", clause_prefix="CDDL_V1PT0", end=120,
         url="https://opensource.org/license/CDDL-1.0",
         clauses=numbered([4, 38, 62, 82, 93, 97, 105, 109, 113, 117], [
             ("Definitions", "DefinitionClause"), ("License Grants", "GrantClause"),
             ("Distribution Obligations", "DistributionClause"), ("Versions of the License", "VersionClause"),
             ("Disclaimer of Warranty", "DisclaimerClause"), ("Termination", "TerminationClause"),
             ("Limitation of Liability", "LimitationOfLiabilityClause"), ("U.S. Government End Users", "Clause"),
             ("Miscellaneous", "MiscClause"), ("Responsibility for Claims", "Clause")], first=1)),
    dict(iri="EUPL_V1PT1", slug="eupl-v1pt1", spdx="EUPL-1.1", clause_prefix="EUPL_V1PT1", end=158,
         url="https://opensource.org/license/EUPL-1.1",
         clauses=numbered([13, 37, 61, 65, 69, 83, 91, 99, 103, 107, 113, 117, 121, 131, 137], [
             ("Definitions", "DefinitionClause"), ("Scope of the rights granted by the Licence", "GrantClause"),
             ("Communication of the Source Code", "SourceCodeGrantClause"), ("Limitations on copyright", "RightToUseClause"),
             ("Obligations of the Licensee", "DistributionClause"), ("Chain of Authorship", "WarrantyClause"),
             ("Disclaimer of Warranty", "DisclaimerClause"), ("Disclaimer of Liability", "LimitationOfLiabilityClause"),
             ("Additional agreements", "AdditionalClause"), ("Acceptance of the Licence", "Clause"),
             ("Information to the public", "Clause"), ("Termination of the Licence", "TerminationClause"),
             ("Miscellaneous", "MiscClause"), ("Jurisdiction", "JuristricationClause"),
             ("Applicable Law", "JuristricationClause")], first=1)
         + [dict(n=16, start=149, heading="Appendix", title="Appendix: Compatible Licences", cls="AdjunctClause")]),
    dict(iri="BOOST-LICENSE", slug="boost", spdx="BSL-1.0", clause_prefix="BOOST", end=8, clauses=[
        dict(start=3, title="Permission", cls="GrantClause"),
        dict(start=5, title="Conditions", cls="AttributionRightsClause"),
        dict(start=7, title="Disclaimer", cls="DisclaimerClause"),
    ]),
    dict(iri="UNLICENSE", slug="unlicense", spdx="Unlicense", clause_prefix="UNLICENSE", end=10, clauses=[
        dict(start=1, title="Public Domain Release", cls="Clause"),
        dict(start=3, title="Permission", cls="GrantClause"),
        dict(start=5, title="Dedication to the Public Domain", cls="Clause"),
        dict(start=8, title="Disclaimer", cls="DisclaimerClause"),
    ]),
    dict(iri="ZLIB-LICENSE", slug="zlib", spdx="Zlib", clause_prefix="ZLIB", end=12,
         url="http://www.zlib.net/zlib_license.html", clauses=[
        dict(start=3, title="Disclaimer", cls="DisclaimerClause"),
        dict(start=5, title="Permission and Conditions", cls="GrantClause"),
    ]),
    dict(iri="WTFPL_V2", slug="wtfpl-v2", spdx="WTFPL", clause_prefix="WTFPL_V2", end=12, clauses=[
        dict(num=0, start=11, title="Permission", cls="GrantClause"),
    ]),
    dict(iri="SIL-OFL_V1PT1", slug="sil-ofl-v1pt1", spdx="OFL-1.1", clause_prefix="SIL-OFL_V1PT1", end=44, clauses=[
        dict(start=11, heading="DEFINITIONS", title="Definitions", cls="DefinitionClause"),
        dict(start=23, heading="PERMISSION & CONDITIONS", title="Permission & Conditions", cls="GrantClause"),
        dict(start=37, heading="TERMINATION", title="Termination", cls="TerminationClause"),
        dict(start=41, heading="DISCLAIMER", title="Disclaimer", cls="DisclaimerClause"),
    ]),
]
