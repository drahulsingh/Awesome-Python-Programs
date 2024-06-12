def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_cyclic_permutations(n):
    str_n = str(n)
    perms = []
    for i in range(len(str_n)):
        perm = str_n[i:] + str_n[:i]
        perms.append(int(perm))
    return perms

def is_circular_prime(n):
    if not is_prime(n):
        return False
    cyclic_perms = get_cyclic_permutations(n)
    for perm in cyclic_perms:
        if not is_prime(perm):
            return False
    return True

num = 1193
if is_circular_prime(num):
    print(f"{num} is a circular prime")
else:
    print(f"{num} is not a circular prime")