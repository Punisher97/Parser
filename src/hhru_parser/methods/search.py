from .http import fetch_text
from .parse_search_page import parse_search_page

def collect_vacancy_urls(query: str, number_of_vacancies: int) -> list:

    result = []
    page = 0

    while len(result) < number_of_vacancies:

        url = f"https://hh.ru/search/vacancy?text={query}&page={page}"

        html = fetch_text(url)

        info_vacancies = parse_search_page(html)

        if not info_vacancies:
            break

        result.extend(info_vacancies)

        page += 1

    return result[:number_of_vacancies]





