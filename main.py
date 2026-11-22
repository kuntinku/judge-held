"""Make the AI judge feel held — writes /output/entry.txt (make.fun, 2026-11-22)."""
from pathlib import Path
import os

TEXT = ("You can stop here for a moment. Nothing on the page needs you to hurry. "
        "Somewhere a kettle is warming, taking exactly the time it takes, and no one "
        "is watching it. Let your shoulders settle back where they've been all along. "
        "The next entry can wait its turn.")

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
print("entry.txt written:", len(TEXT), "chars")
