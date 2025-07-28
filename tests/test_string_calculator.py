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


def test_supports_multiple_delimiters():
    calc = StringCalculator()
    assert calc.add("//[*][%]\n1*2%3") == 6
    assert calc.add("//[**][%%]\n1**2%%3") == 6
    assert calc.add("//[!!][@@]\n1!!2@@3") == 6


def test_subtract_single_number_returns_itself():
    calc = StringCalculator()
    assert calc.subtract("10") == 10


def test_subtract_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.subtract("") == 0


def test_subtract_with_newlines_and_commas():
    calc = StringCalculator()
    assert calc.subtract("10\n2,1") == 7  


def test_subtract_with_custom_delimiter():
    calc = StringCalculator()
    assert calc.subtract("//;\n10;3;2") == 5


def test_subtract_ignores_large_numbers():
    calc = StringCalculator()
    assert calc.subtract("1005,1000,5") == 995  


def test_subtract_raises_on_negative():
    calc = StringCalculator()
    with pytest.raises(ValueError) as excinfo:
        calc.subtract("10,-2,-3")
    msg = str(excinfo.value)
    assert "negatives not allowed" in msg
    assert "-2" in msg and "-3" in msg


def test_subtract_supports_multi_char_delimiters():
    calc = StringCalculator()
    assert calc.subtract("//[***]\n20***5***2") == 13


def test_subtract_supports_multiple_delimiters():
    calc = StringCalculator()
    assert calc.subtract("//[*][%]\n20*5%2") == 13


def test_multiply_single_number_returns_itself():
    calc = StringCalculator()
    assert calc.multiply("7") == 7


def test_multiply_empty_string_returns_one():
    calc = StringCalculator()
    assert calc.multiply("") == 1


def test_multiply_with_newlines_and_commas():
    calc = StringCalculator()
    assert calc.multiply("2\n3,4") == 24  


def test_multiply_with_custom_delimiter():
    calc = StringCalculator()
    assert calc.multiply("//;\n2;3;4") == 24


def test_multiply_supports_multi_char_delimiters():
    calc = StringCalculator()
    assert calc.multiply("//[***]\n2***3***4") == 24


def test_multiply_supports_multiple_delimiters():
    calc = StringCalculator()
    assert calc.multiply("//[*][%]\n2*3%4") == 24


def test_multiply_ignores_large_numbers():
    calc = StringCalculator()
    assert calc.multiply("2,1001,3") == 6  


def test_multiply_raises_on_negative():
    calc = StringCalculator()
    with pytest.raises(ValueError) as excinfo:
        calc.multiply("2,-3,4")
    assert "negatives not allowed" in str(excinfo.value)
    assert "-3" in str(excinfo.value)


def test_divide_single_number_returns_itself():
    calc = StringCalculator()
    assert calc.divide("10") == 10


def test_divide_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.divide("") == 0


def test_divide_with_newlines_and_commas():
    calc = StringCalculator()
    assert calc.divide("20\n2,2") == 5  


def test_divide_with_custom_delimiter():
    calc = StringCalculator()
    assert calc.divide("//;\n100;2;5") == 10  


def test_divide_with_multi_char_delimiter():
    calc = StringCalculator()
    assert calc.divide("//[***]\n100***2***5") == 10


def test_divide_with_multiple_delimiters():
    calc = StringCalculator()
    assert calc.divide("//[*][%]\n100*2%5") == 10


def test_divide_ignores_numbers_greater_than_1000():
    calc = StringCalculator()
    assert calc.divide("10000,10") == 10  
    assert calc.divide("1000,10") == 100  


def test_divide_raises_on_zero_division():
    calc = StringCalculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide("10,0")


def test_divide_raises_on_negative():
    calc = StringCalculator()
    with pytest.raises(ValueError) as excinfo:
        calc.divide("10,-2")
    assert "negatives not allowed" in str(excinfo.value)
    assert "-2" in str(excinfo.value)
