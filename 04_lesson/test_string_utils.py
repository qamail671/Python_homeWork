import pytest

from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive #"""Позитивный тест: удаление пробелов в начале строки"""
@pytest.mark.parametrize("input_str, expected", [
    ("   hello", "hello"), ("     multiple    spaces", "multiple    spaces"), ("   ", "")])
def test_trim_positive(input_str, expected):
    utils = StringUtils()
    assert utils.trim(input_str) == expected

@pytest.mark.negative #"""Негативный тест: удаление пробелов в начале строки"""
@pytest.mark.parametrize("input_str, expected", [
    ("\thello", "\thello"  ), (" \t \n ", "\t \n "), ("   ", "")])
def test_trim_negative(input_str, expected):
    utils = StringUtils()
    assert utils.trim(input_str) == expected

@pytest.mark.positive #"""Позитивный тест: символ присутствует в строке"""
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("SkyPro", "S", True), ("hello", "o", True)])
def test_contains_positive(input_str, input_sym, expected):
    string_utils= StringUtils()
    assert string_utils.contains(input_str, input_sym) == expected

@pytest.mark.negative  # """Негативный тест: символ присутствует в строке"""
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("SkyPro", "t", False), ("hello", "", False)])
def test_contains_negative(input_str, input_sym, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.positive #"""Позитивный тест: удаление одного символа"""
@pytest.mark.parametrize("input_str, input_sym, string" , [
    ("SkyPro", "S", "kyPro"), ("hello", "o", "hell")])
def test_delete_symbol_positive(input_str, input_sym, string):
    string_utils = StringUtils()
    assert  string_utils.delete_symbol(input_str, input_sym) == string

@pytest.mark.positive  # """Негативный тест: удаление одного символа"""
@pytest.mark.parametrize("input_str, input_sym, string", [
        ("SkyPro", "G", "SkyPro"), ("1.2.3.4", ".", "1234")])
def test_delete_symbol_positive(input_str, input_sym, string):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, input_sym) == string
