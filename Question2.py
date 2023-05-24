def is_valid_string(s):
    # Count the frequency of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Count the frequency of frequencies
    freq_count = {}
    for count in char_count.values():
        if count in freq_count:
            freq_count[count] += 1
        else:
            freq_count[count] = 1

    # If there is only one frequency or all frequencies are the same
    if len(freq_count) == 1:
        return "YES"
    return "NO"

# Example usage
s1 = "abc"
result1 = is_valid_string(s1)
print(result1)

s2 = "abccc"
result2 = is_valid_string(s2)
print(result2)