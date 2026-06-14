def max_vowels_in_substring(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_in_substring = 0

    for j in range(k):
        if s[j] in vowels:
            vowels_in_substring += 1
    max_vowels = vowels_in_substring
    
    for i in range(k, len(s)):
        if s[i] in vowels:
            vowels_in_substring += 1
        if s[i-k] in vowels:
            vowels_in_substring -= 1
        max_vowels = max(vowels_in_substring, max_vowels)

    return max_vowels