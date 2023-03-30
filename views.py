from config import *


def list_to_paragraphs(data: list):
    return ''.join([f'<ul>{value}</ul>' for value in data]) if data else '<p>No data given.</p>'

def cats() -> str:
    with open(CATS_TEMPLATE, 'r') as f:
        return f.read().format(image=cats)
    
def animals(animals_data: dict) -> str:
    with open(ANIMALS_TEMPLATE, 'r') as f:
        print(animals_data)
        return f.read().format(**animals_data)

def main_page() -> str:
    with open(MAIN_TEMPLATE, 'r') as f:
        return f.read()