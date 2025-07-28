from calculator.string_calculator import StringCalculator
import pytest


def test_returns_zero_for_empty_string():
    calc = StringCalculator()
    result = calc.add("")
    assert result == 0


def test_returns_number_when_single_number_passed():
    calc = StringCalculator()
    result = calc.add("1")
    assert result == 1


def test_returns_sum_of_two_numbers():
    calc = StringCalculator()
    result = calc.add("1,2")
    assert result == 3


def test_returns_sum_of_unknown_quantity_of_numbers():
    calc = StringCalculator()
    result = calc.add("1,2,3,4,5")
    assert result == 15


def test_returns_sum_when_newline_used_as_delimiter():
    calc = StringCalculator()
    result = calc.add("1\n2,3")
    assert result == 6


def test_returns_sum_using_custom_single_char_delimiter():
    calc = StringCalculator()
    result = calc.add("//;\n1;2")
    assert result == 3


def test_raises_exception_for_negative_number():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="negatives not allowed: -1"):
        calc.add("-1")


def test_raises_exception_with_all_negative_numbers():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="negatives not allowed: -2, -4"):
        calc.add("1,-2,3,-4")


def test_returns_how_many_times_add_was_called():
    calc = StringCalculator()
    calc.add("1,2")
    calc.add("3")
    assert calc.get_called_count() == 2


def test_ignores_numbers_greater_than_1000():
    calc = StringCalculator()
    assert calc.add("2,1001") == 2
    assert calc.add("1000,2") == 1002
    assert calc.add("1234\n1") == 1


def test_supports_delimiter_of_any_length():
    calc = StringCalculator()
    assert calc.add("//[***]\n1***2***3") == 6
