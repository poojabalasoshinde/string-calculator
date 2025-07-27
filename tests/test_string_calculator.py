from calculator.string_calculator import StringCalculator


def test_returns_zero_for_empty_string():
    calc = StringCalculator()
    result = calc.add("")
    assert result == 0


def test_returns_number_when_single_number_passed():
    calc = StringCalculator()
    result = calc.add("1")
    assert result == 1
