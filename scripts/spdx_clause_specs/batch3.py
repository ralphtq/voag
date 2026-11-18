# Batch 3: short permissive licences. Clause boundaries are line numbers in the SPDX text files.
# "num" is the licence's own section number; "heading" is an unnumbered heading line to drop;
# "n" sets the clause number; "end" is the first line after the last clause; "url" replaces voag:url.


def cl(start, title, cls, **kw):
    return dict(start=start, title=title, cls=cls, **kw)


MS_LICENCE = [  # Microsoft Shared Source licences: three numbered sections
    ("Definitions", "DefinitionClause"), ("Grant of Rights", "GrantClause"),
    ("Conditions and Limitations", "RestrictionsClause"),
]

BATCH = [
    dict(iri="BSD-ORIGINAL-LICENSE", slug="bsd-original", spdx="BSD-4-Clause", clause_prefix="BSD-ORIGINAL", end=15, clauses=[
        cl(3, "Redistribution and Use", "DistributionClause"),
        cl(9, "Advertising Acknowledgment", "AttributionRightsClause"),
        cl(12, "Endorsement", "RestrictionsClause"),
        cl(14, "Disclaimer", "DisclaimerClause")]),
    dict(iri="CLEAR-BSD-LICENSE", slug="clear-bsd", spdx="BSD-3-Clause-Clear", clause_prefix="CLEAR-BSD", end=15,
         url="https://spdx.org/licenses/BSD-3-Clause-Clear.html", clauses=[
        cl(6, "Redistribution and Use", "DistributionClause"),
        cl(12, "Endorsement", "RestrictionsClause"),
        cl(14, "No Patent License and Disclaimer", "DisclaimerClause")]),
    dict(iri="NCSA-LICENSE", slug="ncsa", spdx="NCSA", clause_prefix="NCSA", end=16,
         url="https://opensource.org/license/NCSA", clauses=[
        cl(7, "Permission and Conditions", "GrantClause"),
        cl(15, "Disclaimer", "DisclaimerClause")]),
    dict(iri="X11-LICENSE", slug="x11", spdx="X11", clause_prefix="X11", end=13, clauses=[
        cl(5, "Permission", "GrantClause"),
        cl(7, "Conditions", "AttributionRightsClause"),
        cl(9, "Disclaimer", "DisclaimerClause"),
        cl(11, "Use of the X Consortium Name", "RestrictionsClause")]),
    dict(iri="XFREE86-LICENSE_V1PT1", slug="xfree86-v1pt1", spdx="XFree86-1.1", clause_prefix="XFREE86_V1PT1", end=17, clauses=[
        cl(6, "Permission and Conditions", "GrantClause"),
        cl(16, "Disclaimer", "DisclaimerClause")]),
    dict(iri="W3C_SOFTWARE-LICENSE", slug="w3c-software", spdx="W3C", clause_prefix="W3C_SOFTWARE", end=25, clauses=[
        cl(5, "License", "GrantClause", heading="License"),
        cl(17, "Disclaimers", "DisclaimerClause", heading="Disclaimers"),
        cl(23, "Use of Names and Trademarks", "RestrictionsClause")]),
    dict(iri="JSON-LICENSE", slug="json", spdx="JSON", clause_prefix="JSON", end=12, clauses=[
        cl(5, "Permission", "GrantClause"),
        cl(7, "Conditions", "AttributionRightsClause"),
        cl(9, "Good, not Evil", "UsageClause"),
        cl(11, "Disclaimer", "DisclaimerClause")]),
    dict(iri="GNU-ALL-PERMISSIVE-LICENSE", slug="gnu-all-permissive", spdx="FSFAP", clause_prefix="GNU-ALL-PERMISSIVE", end=2, clauses=[
        cl(1, "Permission", "GrantClause")]),
    dict(iri="OPEN-SSL-LICENSE", slug="open-ssl", spdx="OpenSSL", clause_prefix="OPEN-SSL", end=49,
         url="http://www.openssl.org/source/license.html", clauses=[
        cl(5, "Redistribution and Use", "DistributionClause"),
        cl(11, "Advertising Acknowledgment", "AttributionRightsClause"),
        cl(13, "Endorsement", "RestrictionsClause"),
        cl(15, "Use of the OpenSSL Name", "RestrictionsClause"),
        cl(17, "Acknowledgment in Redistributions", "AttributionRightsClause"),
        cl(19, "Disclaimer", "DisclaimerClause"),
        cl(21, "Original SSLeay License", "AdjunctClause")]),
    dict(iri="PHP-LICENSE_V3PT01", slug="php-v3pt01", spdx="PHP-3.01", clause_prefix="PHP_V3PT01", end=21, clauses=[
        cl(5, "Redistribution and Use", "DistributionClause"),
        cl(11, "Endorsement", "RestrictionsClause"),
        cl(13, "Use of the PHP Name", "RestrictionsClause"),
        cl(15, "Revised Versions", "VersionClause"),
        cl(17, "Acknowledgment in Redistributions", "AttributionRightsClause"),
        cl(19, "Disclaimer", "DisclaimerClause")]),
    dict(iri="ZEND-LICENSE_V2PT0", slug="zend-v2pt0", spdx="Zend-2.0", clause_prefix="ZEND_V2PT0", end=19, clauses=[
        cl(4, "Redistribution and Use", "DistributionClause"),
        cl(10, "Endorsement", "RestrictionsClause"),
        cl(12, "Revised Versions", "VersionClause"),
        cl(14, "Acknowledgment in Redistributions", "AttributionRightsClause"),
        cl(16, "Advertising Acknowledgment", "AttributionRightsClause"),
        cl(18, "Disclaimer", "DisclaimerClause")]),
    dict(iri="ZOPE-PUBLIC-LICENSE_V2PT0", slug="zope-public-v2pt0", spdx="ZPL-2.0", clause_prefix="ZOPE-PUBLIC_V2PT0", end=23,
         url="https://opensource.org/license/ZPL-2.0", clauses=[
        cl(7, "Redistribution and Use", "DistributionClause"),
        cl(13, "Endorsement", "RestrictionsClause"),
        cl(15, "Trademarks", "RestrictionsClause"),
        cl(17, "Modification Notices", "ModificationClause"),
        cl(19, "Disclaimer", "DisclaimerClause", heading="Disclaimer")]),
    dict(iri="ZOPE-PUBLIC-LICENSE_V2PT1", slug="zope-public-v2pt1", spdx="ZPL-2.1", clause_prefix="ZOPE-PUBLIC_V2PT1", end=22,
         url="http://old.zope.org/Resources/ZPL/", clauses=[
        cl(7, "Redistribution and Use", "DistributionClause"),
        cl(13, "Endorsement", "RestrictionsClause"),
        cl(15, "Trademarks", "RestrictionsClause"),
        cl(17, "Modification Notices", "ModificationClause"),
        cl(19, "Disclaimer", "DisclaimerClause", heading="Disclaimer")]),
    dict(iri="MS-PL", slug="ms-pl", spdx="MS-PL", clause_prefix="MS-PL", end=23,
         url="https://opensource.org/license/MS-PL",
         clauses=[dict(num=i + 1, start=s, title=t, cls=c) for i, (s, (t, c)) in enumerate(zip([5, 8, 13], MS_LICENCE))]),
    dict(iri="MS-RL", slug="ms-rl", spdx="MS-RL", clause_prefix="MS-RL", end=31,
         url="https://opensource.org/license/MS-RL",
         clauses=[dict(num=i + 1, start=s, title=t, cls=c) for i, (s, (t, c)) in enumerate(zip([5, 14, 19], MS_LICENCE))]),
    dict(iri="MS-LPL", slug="ms-lpl", spdx="MS-LPL", clause_prefix="MS-LPL", end=25,
         url="https://spdx.org/licenses/MS-LPL.html",
         clauses=[dict(num=i + 1, start=s, title=t, cls=c) for i, (s, (t, c)) in enumerate(zip([5, 8, 13], MS_LICENCE))]),
    dict(iri="PYTHON-LICENSE_V2PT0PT1", slug="python-v2pt0pt1", spdx="Python-2.0", clause_prefix="PYTHON_V2PT0PT1", end=73,
         clauses=[dict(num=i + 1, start=s, title=t, cls=c) for i, (s, (t, c)) in enumerate(zip([3, 5, 7, 9, 11, 13, 15, 17], [
             ("Parties", "DefinitionClause"), ("License Grant", "GrantClause"), ("Derivative Works", "ModificationClause"),
             ("Disclaimer of Warranty", "DisclaimerClause"), ("Limitation of Liability", "LimitationOfLiabilityClause"),
             ("Termination", "TerminationClause"), ("No Agency or Endorsement", "RestrictionsClause"),
             ("Acceptance", "Clause")]))]
         + [cl(20, "BeOpen Python Open Source License Agreement", "AdjunctClause", n=9),
            cl(39, "CNRI Open Source License Agreement", "AdjunctClause", n=10),
            cl(66, "CWI License Agreement", "AdjunctClause", n=11)]),
    dict(iri="PYTHON-LICENSE_V1PT6B1-TO-V2PT1", slug="python-v1pt6b1-to-v2pt1", spdx="CNRI-Python",
         clause_prefix="PYTHON_V1PT6B1-TO-V2PT1", end=25,
         clauses=[dict(num=i + 1, start=s, title=t, cls=c) for i, (s, (t, c)) in enumerate(zip([7, 9, 13, 15, 17, 19, 21, 23], [
             ("Parties", "DefinitionClause"), ("License Grant", "GrantClause"), ("Derivative Works", "ModificationClause"),
             ("Disclaimer of Warranty", "DisclaimerClause"), ("Limitation of Liability", "LimitationOfLiabilityClause"),
             ("Termination", "TerminationClause"), ("Governing Law", "JuristricationClause"),
             ("Acceptance", "Clause")]))]),
    dict(iri="UNICODE-LICENSE", slug="unicode", spdx="Unicode-DFS-2016", clause_prefix="UNICODE", end=23, clauses=[
        cl(3, "Scope", "DefinitionClause"),
        cl(11, "Copyright and Permission Notice", "GrantClause", heading="COPYRIGHT AND PERMISSION NOTICE"),
        cl(20, "Disclaimer", "DisclaimerClause"),
        cl(22, "Use of Names", "RestrictionsClause")]),
]
