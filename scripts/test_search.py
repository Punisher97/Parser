from hhru_parser.methods.search import collect_vacancy_urls

items = collect_vacancy_urls("Data Scientist", 20)

print(len(items))

for item in items[:5]:
    print(item)