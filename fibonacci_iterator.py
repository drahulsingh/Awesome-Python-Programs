class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            if self.count == 0:
                self.count += 1
                return self.a
            elif self.count == 1:
                self.count += 1
                return self.b
            else:
                self.count += 1
                next_value = self.a + self.b
                self.a, self.b = self.b, next_value
                return next_value
        else:
            raise StopIteration

n = int(input("Enter number of Fibonacci terms to generate: "))
fibonacci_iterator = Fibonacci(n)

for num in fibonacci_iterator:
    print(num)