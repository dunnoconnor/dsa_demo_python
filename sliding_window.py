def count_unique_substrings(s):
    # accumulator variable to count unique substrings
    count = 0
    # loop through string
    # for each i, if char at i is unique from the char i+1 and i+2, the substring is unique
    for i in range(len(s) - 2):
        first = s[i]
        second = s[i+1]
        third = s[i+2]
        if first != second and first != third and second != third:
            count += 1
    return count