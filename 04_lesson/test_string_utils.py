import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("s", "S")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
     ("   skypro", "skypro"),
     ("   sky   pro", "sky   pro"),  # Пробелы внутри не должны удаляться
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
     ("skypro  ", "skypro  "),
     ("", ""),  # Граничный случай: пустая строка
     ("   ", ""),  # Строка только из пробелов
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),  # Символ в начале
    ("SkyPro", "o", True),  # Символ в конце
    ("SkyPro", "U", False),  # Символа нет
    ("SkyPro", "Pro", True),  # Поиск целой подстроки
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "A", False),  # Поиск в пустой строке
    ("SkyPro", "", True),  # Граничный случай: пустая подстрока всегда True в Python
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),    # Удаление одного символа из середины
    ("SkyPro", "Pro", "Sky"),    # Удаление подстроки с конца
    ("banana", "a", "bnn"),      # Удаление сразу нескольких повторяющихся букв
    ("SkyPro", "U", "SkyPro"),   # Символа нет, строка должна остаться прежней
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "A", ""),             # Удаление символа из пустой строки
    ("SkyPro", "", "SkyPro"),  # Попытка удалить пустой символ "" строка не должна измениться
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
