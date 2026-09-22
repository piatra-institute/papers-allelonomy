# Allelonomy

Autonomy After Sovereignty.

The modern exit from guardianship produced an unintended figure, the sovereign chooser, whose capacities, preferences and options were formed by institutions and technical systems absent from the chooser's self-description. We name a position beyond both the ward and the sovereign. Allelonomy, from Greek *allelon* (one another) and *nomos* (law), is self-rule through one another: the capacity of distinct persons to govern themselves through reciprocal, contestable and non-dominating relations that also help form them. Because cartels are also mutually dependent, we specify four conditions and test each in simulation by deleting it. In a two-site formation loop, mild private preference for better peers stratifies capacities with no planner, reaching a gap of 0.28 by generation 25; a standing commitment by part of the advantaged to stay reduces the gap to 0.13 at a cost of 0.04 per committed family per generation. In an institution maintained by the voice of its articulate members, free exit after a scandal removes those members and quality falls from 0.6 to a floor of 0.05; forbidding exit holds quality at 0.95, and accountable exit, which keeps 0.6 of a leaver's contribution and voice attached, stabilizes it at 0.54 while 17 of 100 members leave. In an epistemic model, deference scores 0.9 under an honest institution and 0.35 under a captured one, solitary research 0.62 in both, and herding matches deference; pooling 21 independent signals with audits scores 0.9 and 0.77, and returns to 0.35 when the institution can suppress the pool.

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

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build allelonomy`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
