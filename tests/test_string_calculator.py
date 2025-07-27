from calculator.string_calculator import StringCalculator


def test_returns_zero_for_empty_string():
    calc = StringCalculator()
    result = calc.add("")
    assert result == 0
