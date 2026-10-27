"""
Bi-exponential STDP kernel of the Pt/NKN/HfO2/TiN memristor synapse, using the
constants published in Shih et al., J. Mater. Chem. C (2026), doi:10.1039/d5tc04557f.

    dG(dt) =  A+ * exp(-dt / tau+)   for dt > 0   (pre before post: potentiation)
    dG(dt) = -A- * exp( dt / tau-)   for dt < 0   (post before pre: depression)
"""

import matplotlib.pyplot as plt
import numpy as np

A_PLUS, TAU_PLUS = 60.97, 0.33    # uS, ms
A_MINUS, TAU_MINUS = 64.19, 0.29  # uS, ms


def stdp(dt_ms):
    dt_ms = np.asarray(dt_ms, dtype=float)
    return np.where(dt_ms > 0, A_PLUS * np.exp(-dt_ms / TAU_PLUS),
                    np.where(dt_ms < 0, -A_MINUS * np.exp(dt_ms / TAU_MINUS), 0.0))


if __name__ == "__main__":
    print(f"A+/A- = {A_PLUS / A_MINUS:.2f}, tau-/tau+ = {TAU_MINUS / TAU_PLUS:.2f}")
    dt = np.linspace(-1.2, 1.2, 601)
    plt.plot(dt, stdp(dt))
    plt.axhline(0, color="grey", lw=0.5)
    plt.xlabel("Δt (ms)")
    plt.ylabel("ΔG (µS)")
    plt.title("STDP kernel, NKN/HfO₂ memristor")
    plt.show()
