# Roast Your Own Agent entry: one deterministic one-liner, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
import os

ROAST = "I gave my agent one job; it wrote a plan, a backup plan, and a eulogy for the plan."

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
    handle.write(ROAST)
