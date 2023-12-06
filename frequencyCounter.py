# Write a function that determines if any permutation of a string is a palindrome
def palindrome_permutation(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    
    odd = 0
    for key in count:
        if count[key] % 2 != 0:
            odd += 1
        if odd > 1:
            return False
    return True