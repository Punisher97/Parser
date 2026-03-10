from pathlib import Path
from hhru_parser.methods.parse_search_page import parse_search_page

html = Path("debug/vacancy.html").read_text(encoding="utf-8")
items = parse_search_page(html)

print("Found:", len(items))
for item in items[:20]:
    print(item)