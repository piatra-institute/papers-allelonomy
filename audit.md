# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 32 CSL entries. 17 with DOIs resolved through doi.org content negotiation (8 matched automatically in Crossref; balibar2014, collins2002, fricker2007, longino1990, mackenzie2000, nguyen2020, ostrom1990, pettit1999, stiegler1998 assigned by hand from Crossref searches). 15 entered by hand without DOI: arendt1961, boltanski2005, bourdieu1984, castoriadis1987, deleuze1992, dewey1927, hirschman1970, illich1973 (Crossref matched a later edition; DOI dropped), kant1784 (language de to keep German capitalisation), kittay1999, mill1859, mol2008, oneill2002, oreskes2010, polanyi1966.
- Correction: naniwada1993 container "P. M. Minus (ed.), The Ethics of Business in a Global Economy" -> "Thomas W. Dunfee and Yukimasa Nagayasu (eds.), Business Ethics: Japan and the Global Economy" (DOI 10.1007/978-94-015-8183-7_8, pp. 153-171); sources.md updated.
- Title and author normalisation from DOI records (Young, Sloterdijk, Schelling titles; Stiglitz initials; Hardwig page range 335-349).
- claims.yaml: 58 claims (43 computation, 9 source, 2 definition, 1 assumption, 2 interpretation, 1 normative). All model numbers in the abstract and body bound to simulation/output/results.json (run model) except the 0.6 share of committing lineages, the 30 articulate members, the scandal size 0.25 at period 10 and the 66 remaining members, which are model settings not stored in results.json.
- Source statements not bound: Kant (1784), Mill (1859), Arendt (1961), Balibar (2014), Foucault (1982), Bourdieu (1984), Stiegler (1998), Deleuze (1992), Boltanski and Chiapello (2005), Hirschman (1970), Hardwig (1985), Polanyi (1966), Latour (2004), Oreskes and Conway (2010), O'Neill (2002), Longino (1990), Mol (2008), Kittay (1999), Stiglitz (2002), Naniwada (1993), Illich (1973), Castoriadis (1987), Dewey (1927): no retrievable abstract or abstract silent on the attributed point.
- Execution receipt: run id model (uv run python run_all.py); results.json reproduced unchanged; 13 checks pass.
- metadata claims_target: claim-ledger.

## 2026-09-23 — prose revision

Prose rewritten against the house standards. Headings made descriptive (Introduction, Enlightenment and relational autonomy, From self-government to sovereignty, The social production of the chooser, Model design, Sorting and the formation loop, Exit, voice and institutional decline, Epistemic dependence and its conditions, Clinical care, Definition of allelonomy, Objections, Conclusion, Reproducibility).
Values audited: all are Monte Carlo or deterministic simulation outputs with no grid-derived thresholds. The pooled-majority accuracy of 0.87 for 21 signals at 0.62 matches the exact binomial (0.8707). results.json unchanged by figure edits.

## 2026-08-08 — v1, first full draft to publication

Scope: the entire paper, simulation, and evidence base, from the seed chat to publication.

Changes:
  - Sources: 32 entries verified against Crossref, OpenLibrary, or bibliographic records; the term's genealogy (Naniwada 1993, the documented prior use of "allelonomy") verified by chapter DOI. The seed's wider constellation (about thirty further names) cut with reasons logged in sources.md; Schmitt's sovereign-exception line carried in one uncited ordinary-language sentence; Friston omitted per the seed's own stop conditions; Sloterdijk held to one bounded moment.
  - Simulation design iterations logged: the formation equation initially leaked capacity (weights summed to 0.9) and compressed the gap it was meant to show; voice power initially saturated the institution before anyone could be unhappy, and the spiral needed a scandal that actually crosses the exit standard; the responsibility rule failed as a threshold trigger (the sort completes before the gap trips it) and became a standing inherited commitment, which is also the truer rendering of Young's forward-looking responsibility.
  - Voice: draft came in at 0 errors, 1 review-candidate; "honest" thinned from 10 to 6 (the technical regime label retained), "exactly" 4 to 2.

Verification:
  - voice: 0 errors, 0 review-candidates
  - refs: 32 in-text keys, 32 bib entries, 0 missing, 0 unused
  - claims: 286 sim values, 17 decimal claims in prose, 0 without a match
  - build: 12 pages, no missing-character warnings
  - simulation: 13/13 invariants
  - check => PASS
