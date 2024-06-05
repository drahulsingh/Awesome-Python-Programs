def is_binary(s):
    return all(c in '01' for c in s)

test_str = "101010"
print(f"Is '{test_str}' binary? {is_binary(test_str)}")

test_str = "102010"
print(f"Is '{test_str}' binary? {is_binary(test_str)}")