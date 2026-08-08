"""Figures for *Allelonomy*. Each reads the results dict and writes one PNG.

Palette (CVD-checked in a prior validation; line styles and direct labels as
secondary encoding): amber, green, blue, warm gray; red reserved for harm.
"""
from __future__ import annotations

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1a1a1a"
GRID = "#d9d9d9"
AMBER = "#b45309"
GREEN = "#15803d"
BLUE = "#2563eb"
GRAY = "#57534e"
RED = "#b3202c"


def _style(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)


def plot_formation(res: dict, path: str) -> None:
    fo = res["formation"]
    g = np.arange(1, fo["generations"] + 1)
    fig, ax = plt.subplots(figsize=(7.8, 3.7))
    ax.plot(g, fo["sovereign"]["gaps"], "-", color=RED, lw=1.8,
            label="sovereign choice: every affordable move made")
    ax.plot(g, fo["allelonomic"]["gaps"], "-", color=GREEN, lw=1.8,
            label="recursive responsibility: committed lineages stay")
    ax.set_xlabel("generation", fontsize=9)
    ax.set_ylabel("capacity gap between formation sites", fontsize=9)
    ax.set_title("stratification without a planner, and its reduction at a stated cost",
                 fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=8.5, loc="lower right")
    _style(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_exit_voice(res: dict, path: str) -> None:
    ev = res["exit_voice"]
    t = np.arange(1, ev["periods"] + 1)
    fig, ax = plt.subplots(figsize=(7.8, 3.7))
    ax.plot(t, ev["ward"]["quality"], ":", color=GRAY, lw=1.8,
            label="no exit: voice holds the institution")
    ax.plot(t, ev["sovereign"]["quality"], "-", color=RED, lw=1.8,
            label="free exit: the articulate leave, the spiral follows")
    ax.plot(t, ev["allelonomic"]["quality"], "-", color=GREEN, lw=1.8,
            label="accountable exit: contribution and voice retained")
    ax.axvline(10, color=INK, lw=0.9, ls="--")
    ax.text(10.6, 0.9, "the scandal", fontsize=8.5, color=INK)
    ax.set_xlabel("period", fontsize=9)
    ax.set_ylabel("institutional quality", fontsize=9)
    ax.set_ylim(0, 1.05)
    ax.set_title("exit, voice, and who inherits the wreck", fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=8.5, loc="lower left")
    _style(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_epistemics(res: dict, path: str) -> None:
    ep = res["epistemics"]["grid"]
    regimes = ["ward", "sovereign", "herding", "allelonomic", "allelonomic_dominated"]
    labels = ["ward\n(defer)", "sovereign\n(research alone)", "herd\n(no distinction)",
              "allelonomic\n(all 4 conditions)", "allelonomic,\ndominated"]
    cols = ["honest institution", "captured institution"]
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    M = np.array([[ep[r]["honest"], ep[r]["captured"]] for r in regimes])
    im = ax.imshow(M, cmap="RdYlGn", vmin=0.3, vmax=1.0, aspect="auto")
    for i in range(len(regimes)):
        for j in range(2):
            ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center",
                    fontsize=10, color=INK, fontweight="bold")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(cols, fontsize=9)
    ax.set_yticks(range(len(regimes)))
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_title("accuracy of belief by regime; what each condition buys",
                 fontsize=10, color=INK)
    ax.grid(False)
    fig.colorbar(im, ax=ax, fraction=0.035, pad=0.03)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
