def is_bouncy_num(num):
    if num < 100:
        return False
    
    num_str = str(num)
    increasing = decreasing = False
    
    for i in range(1, len(num_str)):
        if num_str[i] > num_str[i - 1]:
            increasing = True
        elif num_str[i] < num_str[i - 1]:
            decreasing = True
            
        if increasing and decreasing:
            return True
            
    return False

number = int(input("Enter the no. to check if it is a Bouncy no.: "))

if is_bouncy_num(number):
    print(f"{number} is a Bouncy no.")
else:
    print(f"{number} is not a Bouncy no.")