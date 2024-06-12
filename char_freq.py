def char_freq(s):
    from collections import Counter
    freq = Counter(s)
    min_char = min(freq, key=freq.get)
    max_char = max(freq, key=freq.get)
    return min_char, max_char

input_str = "example string to test frequency"
min_char, max_char = char_freq(input_str)
print(f"Least frequent character: {min_char}")
print(f"Most frequent character: {max_char}")