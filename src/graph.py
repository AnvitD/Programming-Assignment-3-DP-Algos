import time
import os
import csv
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR   = os.path.dirname(SCRIPT_DIR)  
DATA_DIR   = os.path.join(ROOT_DIR, "tests")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")

sys.path.insert(0, SCRIPT_DIR)
from main import parse_input, find_highest_value_lcs

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def benchmark(filepath: str):
    with open(filepath) as f:
        text = f.read()
    values, A, B = parse_input(text)
    start = time.perf_counter()
    val, seq = find_highest_value_lcs(values, A, B)
    elapsed = time.perf_counter() - start
    return len(A), len(B), val, seq, elapsed


def write_output(in_filepath: str, val: int, seq: str):
    out_filepath = in_filepath.replace(".in", ".out")
    with open(out_filepath, "w") as f:
        f.write(f"{val}\n{seq}\n")
    return out_filepath


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(DATA_DIR, "*.in")))
    if not files:
        return

    rows = []
    print(f"{'File':<35} {'|A|':>6} {'|B|':>6} {'MaxVal':>8} {'|Subseq|':>9} {'Time(s)':>10} {'Output'}")
    print("-" * 100)
    for fp in files:
        na, nb, val, seq, t = benchmark(fp)
        out_path = write_output(fp, val, seq)
        rows.append((os.path.basename(fp), na, nb, val, len(seq), t))
        print(f"{os.path.basename(fp):<35} {na:>6} {nb:>6} {val:>8} {len(seq):>9} {t:>10.6f}   → {out_path}")

    with open(os.path.join(RESULTS_DIR, "timings.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "len_A", "len_B", "max_value", "subseq_len", "time_sec"])
        w.writerows(rows)

    labels = [r[0].replace(".in", "") for r in rows]
    times  = [r[5] for r in rows]
    sizes  = [r[1] for r in rows]  

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(sizes, times, marker="o", color="#2563eb", linewidth=2, markersize=6)
    for s, t, lbl in zip(sizes, times, labels):
        ax.annotate(lbl, (s, t), textcoords="offset points", xytext=(4, 4), fontsize=7)
    ax.set_xlabel("String length n", fontsize=12)
    ax.set_ylabel("Runtime ", fontsize=12)
    ax.set_title("HVLCS Runtime", fontsize=14)
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plot_path = os.path.join(RESULTS_DIR, "runtime_plot.png")
    plt.savefig(plot_path, dpi=150)
    print(f"\nPlot saved to {plot_path}")
    print(f"Timings saved to {os.path.join(RESULTS_DIR, 'timings.csv')}")


if __name__ == "__main__":
    main()
