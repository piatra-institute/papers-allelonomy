"""Orchestrator: reproduces every number and all three figures in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/*.png. Seeded; a rerun
reproduces every number bit for bit. A failed invariant fails the run.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))

    from figures import plot_formation, plot_exit_voice, plot_epistemics
    plot_formation(results, str(OUT / "figures" / "formation.png"))
    plot_exit_voice(results, str(OUT / "figures" / "exit_voice.png"))
    plot_epistemics(results, str(OUT / "figures" / "epistemics.png"))

    fo = results["formation"]
    print(f"formation: sovereign gap {fo['sovereign']['final_gap']}, "
          f"allelonomic {fo['allelonomic']['final_gap']}, "
          f"cost/decliner/generation {fo['allelonomic']['mean_cost_per_decliner']}")
    ev = results["exit_voice"]
    print(f"exit-voice: ward {ev['ward']['final_quality']}, sovereign "
          f"{ev['sovereign']['final_quality']} ({ev['sovereign']['exited']} exited), "
          f"allelonomic {ev['allelonomic']['final_quality']} "
          f"({ev['allelonomic']['exited']} exited)")
    ep = results["epistemics"]["grid"]
    for r, v in ep.items():
        print(f"  {r}: honest {v['honest']}, captured {v['captured']}")
    print("pooled independent:", results["epistemics"]["pooled_independent_accuracy"])
    print("checks:", f"{sum(results['checks'].values())}/{len(results['checks'])}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
