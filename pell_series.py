def pell_series(n):
    pell_numbers = [0, 1]
    for i in range(2, n):
        next_pell = 2 * pell_numbers[i - 1] + pell_numbers[i - 2]
        pell_numbers.append(next_pell)
    return pell_numbers

first_15_pell_numbers = pell_series(15)
print("The first 15 numbers of Pell series are:")
print(first_15_pell_numbers)