from frequencyCounter import palindrome_permutation

def test_palindrome_permutation():
    assert palindrome_permutation('aab') == True, "Error on test case 1"
    assert palindrome_permutation('abc') == False, "Error on test case 2"
    assert palindrome_permutation('a') == True, "Error on test case 3"
    assert palindrome_permutation('abba') == True, "Error on test case 4"
    assert palindrome_permutation('racecar') == True, "Error on test case 5"
    assert palindrome_permutation('python') == False, "Error on test case 6"
    assert palindrome_permutation('') == True, "Error on test case 7"
    print("All tests pass")

test_palindrome_permutation()