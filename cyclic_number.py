def is_cyclic_number(num):
    num_str = str(num)
    num_len = len(num_str)
    
    for i in range(1, num_len + 1):
        product = num * i
        product_str = str(product)
        if len(product_str) != num_len or not is_permutation(num_str, product_str):
            return False
    return True

def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)

number = 142857
if is_cyclic_number(number):
    print(f"{number} is a cyclic number")
else:
    print(f"{number} is not a cyclic number")