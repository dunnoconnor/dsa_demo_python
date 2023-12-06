# Write a function that determines if any permutation of a string is a palindrome
def palindrome_permutation(s):
    # create frequency counter object
    count = {}
    # iterate through input
    for c in s:
        # if current char is a key in counter, increment count
        if c in count:
            count[c] += 1
        else:
            # else add current char as a key in counter
            count[c] = 1
    # count chars with an odd number of occurances
    odd = 0
    for key in count:
        if count[key] % 2 != 0:
            odd += 1
        # if more than one char has an odd count of occurances
        if odd > 1:
            # then the input is not a palindrome
            return False
    return True