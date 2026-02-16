import pymupdf4llm

md_text = pymupdf4llm.to_markdown("1CONCEITOS_BASICOS_DA_ROBOTICA.pdf")

import pathlib

pathlib.Path("1CONCEITOS_BASICOS_DA_ROBOTICA.md").write_bytes(md_text.encode())


