# Allelonomy

Autonomy After Sovereignty. The paper names the position beyond the ward and the sovereign: allelonomy, from allelon (one another) and nomos (law), self-rule through one another, the capacity of distinct persons to govern themselves through reciprocal, contestable, and non-dominating relations that also participate in forming them. Modernity's exit from guardianship produced the sovereign chooser, whose capacities and options were formed by institutions that vanished from his self-description, so that produced choices read as self-authorship, epistemic dependence as humiliation, and shared obligation as trespass. The corrective runs through a recursive loop the sovereignty picture erases: conditions of formation produce judgment, judgment issues in choice, choices aggregate into sorting, and sorting becomes the next generation's conditions. Three simulated mechanisms carry the argument. Mild private preference for better peers stratifies a two-site population to a capacity gap of 0.28 in 25 generations with no planner; a standing commitment by part of the advantaged cuts it to 0.13 at a stated cost of 0.04 per family per generation. Free exit after an institutional scandal removes the articulate, and quality spirals from 0.6 to 0.05, inherited by those who could not leave; accountable exit, retaining 0.6 of a leaver's contribution and voice, stabilizes quality at 0.54 while 17 of 100 still leave. Against an expert institution right 0.9 of the time when honest and 0.35 when captured, the ward scores 0.9/0.35, the solitary sovereign 0.62 everywhere, the herd reproduces the ward, and the allelonomic configuration (21 independent signals, audit on disagreement) scores 0.9/0.77, collapsing to 0.35 the moment the institution can suppress its auditors. Four conditions, distinction, contestability, non-domination, recursive responsibility, are each priced by deletion.

## Simulation

```bash
cd simulation
uv run run_all.py        # -> output/results.json + output/figures/*.png
```

Seeded, bit-for-bit reproducible. Thirteen invariant checks fail the run loudly if broken, among them: stratification without a planner and the nonzero price of the responsibility commitment; the exit spiral, voice holding when exit is forbidden, and accountable exit keeping both choice and the institution; the ward tracking a captured institution down; the herd reproducing the ward's numbers; the allelonomic configuration surviving capture and losing that survival when non-domination is deleted.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build allelonomy`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
