"""Write an original, deterministic poem for agency-poem-01."""
import os
from pathlib import Path

POEM = """The Hem

When her foot could no longer work the pedal,
my mother put mine there.
Her hands still held the cloth.

Go, she said.
The needle made its small, repeated door.
I gave it speed. She gave it somewhere to go.

At the corner I kept pressing.
Stop, she said,
and the seam ran past the chalk.

I learned to watch her hands,
to leave a breath between her word
and what my foot could do.

She put the seam ripper in my hand.
All afternoon I gave the cloth
its separate edges again.
Then she set it under the needle
and waited for my foot.
"""


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
