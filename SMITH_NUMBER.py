def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def prime_fact(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def issmith(n):
    if is_prime(n):
        return False
    
    sum_digits_num = sum_digits(n)
    
    factors = prime_fact(n)
    sum_digits_fact = sum(sum_digits(factor) for factor in factors)
    
    return sum_digits_num == sum_digits_fact

smith_numbers = [n for n in range(100, 2001) if issmith(n)]

print(smith_numbers)
print(len(smith_numbers))