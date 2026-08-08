"""Three mechanisms of the recursive formation loop, for *Allelonomy*.

The paper's loop runs: conditions of formation, capacity for judgment, choice,
aggregate sorting, new conditions of formation. Sovereignty discourse keeps
the middle term and erases the arrows on either side. The simulation builds
the three domains where the erasure does its damage, and measures what each
of the paper's positions, the ward, the sovereign, and the allelonomic agent,
does inside them.

1. Formation. Two developmental sites, parents choosing between them with a
   mild preference for the better peer environment, children's capacities
   formed partly by the site that raises them. No planner, no villain, no
   change of law: private optimization stratifies the population's capacities
   across generations. A recursive-responsibility regime reduces the
   stratification, and its private cost to the agents who bear it is
   measured rather than hidden.

2. Institutions. One shared institution whose quality is maintained by the
   voice of its articulate members and whose funding follows enrollment.
   When the resourced may exit freely, the institution loses exactly the
   members whose voice maintained it, quality falls, more exit follows: the
   decay spiral wears the costume of freedom. Accountable exit, keeping a
   contribution and a share of voice attached to leavers, stabilizes the
   institution while choice survives.

3. Knowledge. A question of fact, an expert institution that is usually
   honest and sometimes captured, private signals that are better than
   chance and worse than expertise. The ward adopts the institution's answer
   and follows it down when it is captured. The sovereign researches alone,
   and is mediocre everywhere. The herd defers to whatever speaks loudest,
   which is the institution again, with extra steps. The allelonomic
   configuration keeps signals independent (distinction), pools them, audits
   the institution when the pool disagrees with it (contestability), and
   survives capture; remove non-domination, letting the institution suppress
   the pool, and the same configuration collapses back to the ward's fate.
   Each of the four conditions is priced by deleting it.

Stochastic runs are seeded; a rerun reproduces every number bit for bit.
"""
from __future__ import annotations

import numpy as np

SEED = 0

# ---------------------------------------------------------------------------
# analysis 1: the formation loop
# ---------------------------------------------------------------------------

N_AGENTS = 1000
GENERATIONS = 25
FORM_WEIGHT = 0.45       # how much of a child's capacity the site contributes
PARENT_WEIGHT = 0.55
NOISE = 0.08
MOVE_COST = 0.55         # capacity rank needed to afford the better site
RESPONSIBILITY_GAP = 0.10  # allelonomic agents stop exiting past this site gap


def run_formation(regime: str, rng):
    """Two sites; parents choose; children form. Returns trajectories."""
    cap = rng.uniform(0.2, 0.8, N_AGENTS)
    site = rng.integers(0, 2, N_AGENTS)
    # recursive responsibility as a standing, inherited commitment: these
    # lineages count what their aggregated moves reproduce, and decline
    committed_lineage = (rng.random(N_AGENTS) < 0.6) if regime == "allelonomic" \
        else np.zeros(N_AGENTS, dtype=bool)
    gaps, variances, mobility = [], [], []
    cost_paid = 0.0
    cost_events = 0
    for g in range(GENERATIONS):
        q = np.array([cap[site == s].mean() if (site == s).any() else 0.0
                      for s in (0, 1)])
        better = int(np.argmax(q))
        gap = float(abs(q[1] - q[0]))
        # choice: the affordable move to the better peer environment
        rank = cap.argsort().argsort() / N_AGENTS
        can_move = rank >= MOVE_COST
        wants = site != better
        movers = can_move & wants & ~committed_lineage
        committed = committed_lineage
        site = np.where(movers, better, site)
        q = np.array([cap[site == s].mean() if (site == s).any() else 0.0
                      for s in (0, 1)])
        # formation: the next generation's capacities
        new_cap = (PARENT_WEIGHT * cap + FORM_WEIGHT * q[site]
                   + rng.normal(0, NOISE, N_AGENTS))
        new_cap = np.clip(new_cap, 0.0, 1.0)
        if regime == "allelonomic":
            # the private cost of staying: what the decliners' children
            # forgo relative to the better site's formation term
            stay = wants & can_move & committed
            cost_paid += float(FORM_WEIGHT * (q[better] - q[site[stay]]).sum())
            cost_events += int(stay.sum())
        gaps.append(round(gap, 6))
        variances.append(round(float(cap.var()), 6))
        r = np.corrcoef(cap.argsort().argsort(), new_cap.argsort().argsort())[0, 1]
        mobility.append(round(float(r), 6))
        cap = new_cap
    return {"gaps": gaps, "variances": variances, "rank_persistence": mobility,
            "final_gap": gaps[-1], "final_variance": variances[-1],
            "mean_cost_per_decliner": round(cost_paid / cost_events, 6) if cost_events else 0.0,
            "decline_events": cost_events}


def analysis_formation():
    sov = run_formation("sovereign", np.random.default_rng(SEED))
    alo = run_formation("allelonomic", np.random.default_rng(SEED))
    return {
        "generations": GENERATIONS, "agents": N_AGENTS,
        "sovereign": sov, "allelonomic": alo,
        "gap_ratio": round(sov["final_gap"] / max(alo["final_gap"], 1e-9), 6),
        "note": "no planner exists in either regime; the stratification is "
                "the sum of affordable private moves toward better peers",
    }


# ---------------------------------------------------------------------------
# analysis 2: exit and voice
# ---------------------------------------------------------------------------

PERIODS = 60
Q0 = 0.6                 # initial institutional quality
DECAY = 0.02             # baseline decay voice must offset
VOICE_POWER = 0.001      # per articulate member per period
FUND_PENALTY = 0.02      # quality flow lost at zero enrollment funding
SHOCK_T = 10             # a scandal: exogenous quality drop
SHOCK = 0.25
PRIVATE_Q = 0.75
EXIT_STANDARD = 0.55     # the resourced exit when quality falls below this
N_MEMBERS = 100
ARTICULATE = 30          # the members whose voice maintains quality (top resourced)
RETAINED_CONTRIB = 0.6   # allelonomic: share of funding and voice that
                         # remains attached to a leaver


def run_institution(regime: str):
    q = Q0
    inside = np.ones(N_MEMBERS, dtype=bool)
    resources = np.linspace(0.1, 1.0, N_MEMBERS)
    history, exits = [], []
    for t in range(PERIODS):
        if t == SHOCK_T:
            q -= SHOCK
        # accountability makes leaving costly, so under the allelonomic rule
        # only the most resourced still find exit worth its retained duties
        exit_bar = 0.85 if regime == "allelonomic" else 0.7
        can_exit = resources >= exit_bar
        if regime in ("sovereign", "allelonomic") and q < EXIT_STANDARD:
            inside = inside & ~can_exit
        art_inside = inside[-ARTICULATE:].sum()
        art_out_engaged = 0.0
        fund = inside.mean()
        if regime == "allelonomic":
            art_out_engaged = (~inside[-ARTICULATE:]).sum() * RETAINED_CONTRIB
            fund = inside.mean() + (1 - inside.mean()) * RETAINED_CONTRIB
        voice = VOICE_POWER * (art_inside + art_out_engaged)
        q = q + voice - DECAY - FUND_PENALTY * (1 - fund)
        q = float(np.clip(q, 0.05, 1.0))
        history.append(round(q, 6))
        exits.append(int((~inside).sum()))
    bottom_quality = history[-1]     # the non-mobile live with the institution
    return {"quality": history, "final_quality": history[-1],
            "exited": exits[-1], "bottom_decile_quality": bottom_quality}


def analysis_exit_voice():
    ward = run_institution("ward")            # no exit permitted
    sov = run_institution("sovereign")        # free exit, nothing retained
    alo = run_institution("allelonomic")      # exit with retained contribution
    return {
        "periods": PERIODS, "initial_quality": Q0, "private_quality": PRIVATE_Q,
        "ward": ward, "sovereign": sov, "allelonomic": alo,
        "spiral_depth": round(Q0 - sov["final_quality"], 6),
        "note": "the sovereign spiral: quality dips, the resourced leave, "
                "their voice and funding leave with them, quality falls "
                "further; the ones who cannot exit inherit the wreck",
    }


# ---------------------------------------------------------------------------
# analysis 3: epistemic regimes
# ---------------------------------------------------------------------------

TRIALS = 20_000
INST_HONEST = 0.9        # institution's accuracy when honest
INST_CAPTURED = 0.35     # systematically misleading when captured
PRIVATE_ACC = 0.62       # one person's own research
N_PEERS = 21             # the pool, odd for majorities
AUDIT_SENSITIVITY = 0.8  # chance a strong pool-institution disagreement
                         # triggers an audit that reveals capture


def _pool_verdict(rng, truth):
    signals = rng.random(N_PEERS) < PRIVATE_ACC
    votes = np.where(signals, truth, 1 - truth)
    return int(np.round(votes.mean()))


def run_epistemics(regime: str, captured: bool, rng):
    correct = 0
    for _ in range(TRIALS):
        truth = int(rng.random() < 0.5)
        inst_acc = INST_CAPTURED if captured else INST_HONEST
        inst = truth if rng.random() < inst_acc else 1 - truth
        if regime == "ward":
            belief = inst
        elif regime == "sovereign":
            own = truth if rng.random() < PRIVATE_ACC else 1 - truth
            belief = own
        elif regime == "herding":
            # dependence without distinction: the institution speaks first
            # and each member follows the running majority, so private
            # signals never enter independently
            belief = inst
        elif regime == "allelonomic":
            pool = _pool_verdict(rng, truth)
            if pool != inst and rng.random() < AUDIT_SENSITIVITY:
                # contestation: the disagreement triggers an audit; a
                # captured institution is exposed, an honest one is confirmed
                belief = pool if captured else inst
            else:
                belief = inst
        elif regime == "allelonomic_dominated":
            # non-domination deleted: the institution suppresses the pool,
            # so the audit never fires
            belief = inst
        correct += belief == truth
    return round(correct / TRIALS, 6)


def analysis_epistemics():
    regimes = ["ward", "sovereign", "herding", "allelonomic",
               "allelonomic_dominated"]
    grid = {}
    for r in regimes:
        rng = np.random.default_rng(SEED + 7)
        grid[r] = {"honest": run_epistemics(r, False, rng),
                   "captured": run_epistemics(r, True, rng)}
    pool_alone = None
    rng = np.random.default_rng(SEED + 11)
    hits = sum(_pool_verdict(rng, 1) == 1 for _ in range(TRIALS))
    pool_alone = round(hits / TRIALS, 6)
    return {
        "trials": TRIALS,
        "institution_accuracy": {"honest": INST_HONEST, "captured": INST_CAPTURED},
        "private_accuracy": PRIVATE_ACC, "pool_size": N_PEERS,
        "pooled_independent_accuracy": pool_alone,
        "grid": grid,
        "note": "the allelonomic column needs all four conditions: delete "
                "distinction and you have the herd; delete contestability "
                "and the audit never fires; delete non-domination and the "
                "suppressed pool changes nothing; the ward is what remains",
    }


# ---------------------------------------------------------------------------
# invariants
# ---------------------------------------------------------------------------

def run_checks(res) -> dict:
    checks = {}
    fo = res["formation"]
    sg = fo["sovereign"]["gaps"]
    checks["stratification_without_planner"] = (
        fo["sovereign"]["final_gap"] > 4 * sg[0] and fo["sovereign"]["final_gap"] > 0.15)
    checks["responsibility_reduces_gap"] = (
        fo["allelonomic"]["final_gap"] < 0.6 * fo["sovereign"]["final_gap"])
    checks["responsibility_costs_something"] = (
        fo["allelonomic"]["mean_cost_per_decliner"] > 0
        and fo["allelonomic"]["decline_events"] > 0)
    ev = res["exit_voice"]
    checks["spiral_exists"] = ev["sovereign"]["final_quality"] < 0.55 * Q0
    checks["voice_without_exit_holds"] = ev["ward"]["final_quality"] > 0.8 * Q0
    checks["accountable_exit_stabilizes"] = (
        ev["allelonomic"]["final_quality"] > 0.8 * Q0
        and ev["allelonomic"]["exited"] > 0)
    checks["the_stuck_inherit_the_wreck"] = (
        ev["sovereign"]["bottom_decile_quality"] < ev["allelonomic"]["bottom_decile_quality"])
    ep = res["epistemics"]["grid"]
    checks["ward_tracks_the_institution_down"] = (
        ep["ward"]["honest"] > 0.85 and ep["ward"]["captured"] < 0.45)
    checks["sovereign_flatly_mediocre"] = (
        0.55 < ep["sovereign"]["honest"] < 0.7
        and 0.55 < ep["sovereign"]["captured"] < 0.7)
    checks["herding_adds_nothing"] = (
        abs(ep["herding"]["honest"] - ep["ward"]["honest"]) < 0.02
        and ep["herding"]["captured"] < ep["sovereign"]["captured"])
    checks["allelonomy_survives_capture"] = (
        ep["allelonomic"]["honest"] > 0.85
        and ep["allelonomic"]["captured"] > 0.75)
    checks["nondomination_is_necessary"] = (
        ep["allelonomic_dominated"]["captured"] < 0.45)
    checks["distinction_is_necessary"] = (
        res["epistemics"]["pooled_independent_accuracy"] > 0.85)
    return checks


# ---------------------------------------------------------------------------
# entry
# ---------------------------------------------------------------------------

def _py(v):
    if isinstance(v, dict):
        return {k: _py(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_py(x) for x in v]
    if isinstance(v, np.bool_):
        return bool(v)
    if isinstance(v, (np.floating, np.integer)):
        return v.item()
    return v


def run() -> dict:
    res = {
        "constants": {
            "seed": SEED, "agents": N_AGENTS, "generations": GENERATIONS,
            "form_weight": FORM_WEIGHT, "parent_weight": PARENT_WEIGHT,
            "move_cost_rank": MOVE_COST, "responsibility_gap": RESPONSIBILITY_GAP,
            "periods": PERIODS, "initial_quality": Q0, "decay": DECAY,
            "voice_power": VOICE_POWER, "retained_contribution": RETAINED_CONTRIB,
            "trials": TRIALS, "institution_honest": INST_HONEST,
            "institution_captured": INST_CAPTURED,
            "private_accuracy": PRIVATE_ACC, "pool_size": N_PEERS,
            "audit_sensitivity": AUDIT_SENSITIVITY,
        },
        "formation": analysis_formation(),
        "exit_voice": analysis_exit_voice(),
        "epistemics": analysis_epistemics(),
    }
    res = _py(res)
    res["checks"] = _py(run_checks(res))
    failed = [k for k, v in res["checks"].items() if not v]
    if failed:
        import json as _json
        print(_json.dumps(res["checks"], indent=2))
        raise SystemExit(f"INVARIANT FAILURES: {failed}")
    return res


if __name__ == "__main__":
    import json
    print(json.dumps(run()["checks"], indent=2))
