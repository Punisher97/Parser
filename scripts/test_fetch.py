from hhru_parser.methods.http import fetch_text, save_html

url = "https://hh.ru/search/vacancy?text=Ml+engineer&from=suggest_post&area=1&suggestId=8c11578b-cb57-4f1c-828d-39e1686f8004&hhtmFrom=main&hhtmFromLabel=vacancy_search_line"
html = fetch_text(url)
save_html(html, "debug/vacancy.html")
print("saved:", len(html))

