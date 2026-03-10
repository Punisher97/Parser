from bs4 import BeautifulSoup

def parse_search_page(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    results = []

    cards = soup.find_all("div", id=True)

    for card in cards:
        classes = card.get("class", [])
        if not any("vacancy-card" in el for el in classes):
            continue

        vacancy_id = card.get("id")
        if not vacancy_id or not vacancy_id.isdigit():
            continue

        title_el = card.find(attrs={"data-qa": "serp-item__title-text"})
        company_el = card.find(attrs={"data-qa": "vacancy-serp__vacancy-employer-text"})
        address_el = card.find(attrs={"data-qa": "vacancy-serp__vacancy-address"})

        title = title_el.get_text(" ", strip=True) if title_el else None
        company = company_el.get_text(" ", strip=True) if company_el else None
        address = address_el.get_text(" ", strip=True) if address_el else None

        results.append({
            "vacancy_id": int(vacancy_id),
            "title": title,
            "url": f"https://hh.ru/vacancy/{vacancy_id}",
            "company": company,
            "address": address,
        })

    return results