def fascinating_num(num):
    if num < 100:
        return False
    
    num_str = str(num)
    multiplied_2 = str(num * 2)
    multiplied_3 = str(num * 3)
    
    concat_result = num_str + multiplied_2 + multiplied_3
    
    all_digits = '123456789'
    for digit in all_digits:
        if concat_result.count(digit) != 1:
            return False
    
    for char in concat_result:
        if char not in all_digits:
            return False
    
    return True

number = int(input("Enter the number to check if it is a fascinating number: "))

if fascinating_num(number):
    print(f"{number} is a fascinating number.")
else:
    print(f"{number} is not a fascinating number.")
