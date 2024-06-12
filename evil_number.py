def evil_num(num):
    binary_rep = bin(num)[2:]
    count_of_ones = binary_rep.count('1')
    
    return count_of_ones % 2 == 0

number = int(input("Enter  positive whole no. to check if it is an Evil n: "))

binary_rep = bin(number)[2:]
count_of_ones = binary_rep.count('1')

print(f"Binary Equivalent: {binary_rep}")
print(f"No. of 1's: {count_of_ones}")

if evil_num(number):
    print("Output: Evil Number")
else:
    print("Output: Not an Evil Number")