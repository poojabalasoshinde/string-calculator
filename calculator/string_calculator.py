class StringCalculator:
    def __init__(self):
        self.call_count = 0

    def add(self, numbers: str) -> int:
        self.call_count += 1
        if not numbers:
             return 0
        if numbers.isdigit():
             return int(numbers)
        return  None
    
    
    def get_called_count(self) -> int:
        return self.call_count
