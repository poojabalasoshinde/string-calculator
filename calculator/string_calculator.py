class StringCalculator:
    def __init__(self):
        self.call_count = 0

    def add(self, numbers: str) -> int:
        self.call_count += 1
        if numbers == "":
            return 0

    def get_called_count(self) -> int:
        return self.call_count
