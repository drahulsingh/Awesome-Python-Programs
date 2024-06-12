def sum_of_proper_divisors(num):
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
    return divisors_sum

def are_amicable_numbers(num1, num2):
    return (sum_of_proper_divisors(num1) == num2 and 
            sum_of_proper_divisors(num2) == num1)

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

if are_amicable_numbers(num1, num2):
    print(f"{num1} and {num2} are amicable numbers.")
else:
    print(f"{num1} and {num2} are not amicable numbers.")