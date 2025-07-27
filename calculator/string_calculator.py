class StringCalculator:
    def __init__(self):
        self.call_count = 0

    def add(self, numbers: str) -> int:
        self.call_count += 1

        if not numbers:
            return 0

        delimiters = [",", "\n"]
        
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            custom_delim = delimiter_line[2:]
            delimiters.append(custom_delim)
        
        
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")

        parts = numbers.split(",")
        return sum(int(n) for n in parts if n)

    def get_called_count(self) -> int:
        return self.call_count
