from typing import List, Callable, Optional
import re


class StringCalculator:
    """
    A string-based calculator that supports add, subtract, multiply, divide
    operations using custom or default delimiters in string input.
    """

    def __init__(self):
        self._call_count = 0
        self.add_occurred: Optional[Callable[[str, int], None]] = None

    def _extract_delimiters_and_numbers(
        self, input_string: str
    ) -> tuple[list[str], str]:
        if input_string.startswith("//"):
            delimiter_part, input_string = input_string.split("\n", 1)
            delimiter_part = delimiter_part[2:]
            if delimiter_part.startswith("["):
                delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
            else:
                delimiters = [delimiter_part]
        else:
            delimiters = [",", "\n"]
        return delimiters, input_string

    def _split_numbers(self, numbers: str, delimiters: list[str]) -> list[str]:
        pattern = "|".join(re.escape(d) for d in delimiters)
        return re.split(pattern, numbers)

    def _parse_numbers(self, input_string: str) -> List[int]:
        if not input_string:
            return []

        delimiters, number_string = self._extract_delimiters_and_numbers(input_string)
        parts = self._split_numbers(number_string, delimiters)

        try:
            numbers = [int(n.strip()) for n in parts if n.strip()]
        except ValueError:
            raise ValueError("Invalid number in input")

        self._validate_no_negatives(numbers)
        return [n for n in numbers if n <= 1000]

    def _validate_no_negatives(self, numbers: List[int]) -> None:
        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    def _execute(
        self, input_string: str, operation: Callable[[int, int], int], identity: int
    ) -> int:
        self._call_count += 1
        numbers = self._parse_numbers(input_string)

        if not numbers:
            return identity

        result = numbers[0]
        for num in numbers[1:]:
            result = operation(result, num)

        if self.add_occurred:
            self.add_occurred(input_string, result)

        return result

    def add(self, numbers: str) -> int:
        return self._execute(numbers, lambda a, b: a + b, 0)

    def subtract(self, numbers: str) -> int:
        return self._execute(numbers, lambda a, b: a - b, 0)

    def multiply(self, numbers: str) -> int:
        return self._execute(numbers, lambda a, b: a * b, 1)

    def divide(self, numbers: str) -> int:
        def safe_divide(a: int, b: int) -> int:
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return a // b

        return self._execute(numbers, safe_divide, 0)

    def get_called_count(self) -> int:
        return self._call_count
