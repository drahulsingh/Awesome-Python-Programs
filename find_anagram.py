def anagrams(s):
    from collections import defaultdict
    words = s.lower().split()
    sorted_words = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        sorted_words[sorted_word].append(word)
    
    anagram_pairs = [group for group in sorted_words.values() if len(group) > 1]
    return anagram_pairs

input_str = "Welcome on earth and in our heart"
anagrams = anagrams(input_str)
for pair in anagrams:
    print(" ".join(pair))