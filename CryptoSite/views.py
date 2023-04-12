from config import *


def list_to_paragraphs(message: list):
    return ''.join([f'<ul>{instance}</ul>' for instance in message]) if message else '<p>No data was given.</p>'


def overview(over_view: dict) -> str:
    with open(MARKET_OVERVIEW_TEMPLATE, 'r') as page:
        return page.read().format(**over_view)


def coins_data(coins_info: dict) -> str:
    print(coins_info)
    with open(COINS_TEMPLATE, 'r') as page:
        return page.read().format(**coins_info)


def main_page() -> str:
    with open(MAIN_TEMPLATE, 'r') as page:
        return page.read()
