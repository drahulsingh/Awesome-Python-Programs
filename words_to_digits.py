def words_digits(s):
    word_digit = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    words = s.lower().split()
    digits = ''.join(word_digit[word] for word in words if word in word_digit)
    return digits

input_str = "One Zero Three"
print(f"Converted digits: {words_digits(input_str)}")