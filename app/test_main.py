import pytest
from main import greeting

tests = [('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга')]


@pytest.mark.parametrize('name,expected', tests)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert greeting(name) == expected


def test_capitalize():
    """Все слова в имени начинаются с большой буквы."""
    name = 'александр сергеевич'
    assert greeting(name) == 'Привет, Александр Сергеевич'


def test_three_words():
    """Все слова в имени начинаются с большой буквы."""
    name = 'иван иванович петров'
    assert greeting(name) == 'Привет, Иван Иванович Петров'
