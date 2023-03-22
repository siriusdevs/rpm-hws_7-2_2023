"""Some functions that helps to work main code."""


from config import *


def list_to_paragraphs(data: list):
    """
    Do list to paragraphs.

    Args:
        data: list - data_list

    Returns:
        str - result of list_to_paragraphs
    """
    return ''.join([f'<ul>{value}</ul>' for value in data]) if data else '<p>No data given.</p>'


def weather(weatherr: dict) -> str:
    """
    Open weather template.

    Args:
        weatherr: dict - weather

    Returns:
        str - result of weather
    """
    with open(WEATHER_TEMPLATE, 'r') as file:
        return file.read().format(**weatherr)
    
    
def chuck(joke: dict) -> str:
    """
    Open chuck template.

    Args:
        joke: dict - joke

    Returns:
        str - result of chuck
    """
    with open(CHUCK_TEMPLATE, 'r') as file:
        return file.read().format(**joke)
    
    
def students(students_data: dict) -> str:
    """
    Open students template.

    Args:
        students_data: dict - students data

    Returns:
        str - result of students
    """
    with open(STUDENTS_TEMPLATE, 'r') as file:
        return file.read().format(**students_data)


def trees(trees_data: dict) -> str:
    """
    Open trees template.

    Args:
        trees_data: dict - trees data

    Returns:
        str - result of trees
    """
    with open(TREES_TEMPLATE, 'r') as file:
        return file.read().format(**trees_data)
    
    
def main_page() -> str:
    """
    Open main template.

    Args:

    Returns:
        str - result of main_page
    """
    with open(MAIN_TEMPLATE, 'r') as file:
        return file.read()
