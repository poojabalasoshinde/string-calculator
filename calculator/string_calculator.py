class StringCalculator:
    def __init__(self):
        self.call_count = 0

    def _extract_delimiters_and_numbers(self, input_str: str):
        delimiters = [",", "\n"]
        if input_str.startswith("//"):
            delimiter_line, input_str = input_str.split("\n", 1)
            custom_delim = delimiter_line[2:]
            delimiters.append(custom_delim)
        return delimiters, input_str

    def add(self, numbers: str) -> int:
        
        self.call_count += 1
        
        if not numbers:
            return 0
        delimiters, numbers = self._extract_delimiters_and_numbers(numbers)

        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")

        parts = numbers.split(",")
        number_list = [int(n) for n in parts if n]

        negatives = [str(n) for n in number_list if n < 0]

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(negatives)}")

        return sum(number_list)

      
    def get_called_count(self) -> int:
        return self.call_count
