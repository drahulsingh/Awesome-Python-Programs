class Armstrong:
    def __iter__(self):
        return self._generate_armstrong_numbers()
    
    def _generate_armstrong_numbers(self):
        for number in range(100, 1000):
            digits = [int(digit) for digit in str(number)]
            if sum(digit ** 3 for digit in digits) == number:
                yield number

armstrong_numbers = Armstrong()

for num in armstrong_numbers:
    print(num)