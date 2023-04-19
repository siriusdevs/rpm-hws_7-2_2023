from config import CITIES_TEMPLATE, HOTELS_TEMPLATE, MAIN_TEMPLATE


def list_to_paragraphs(data: list):
    return ''.join([f'<ul>{value}</ul>' for value in data]) if data else '<p>No data given.</p>'


def hotels(hotels_data: dict) -> str:
    with open(HOTELS_TEMPLATE, 'r') as template:
        values = ''.join([f"<ul>{value['name']}</ul>" for value in hotels_data])
        return template.read().format(values)


def cities(cities_data: dict) -> str:
    with open(CITIES_TEMPLATE, 'r') as template:
        return template.read().format(**cities_data)


def main_page() -> str:
    with open(MAIN_TEMPLATE, 'r') as template:
        return template.read()
