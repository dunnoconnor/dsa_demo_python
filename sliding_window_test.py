from sliding_window import count_unique_substrings

def test_count_unique_substrings():
    assert count_unique_substrings('xyzzaz') == 1, "Test case 1 failed"
    assert count_unique_substrings('aababcabc') == 4, "Test case 2 failed"
    assert count_unique_substrings('aaabbb') == 0, "Test case 3 failed"
    assert count_unique_substrings('abc') == 1, "Test case 4 failed"
    assert count_unique_substrings('a') == 0, "Test case 5 failed"
    assert count_unique_substrings('') == 0, "Test case 6 failed"
    print("All tests passed")

test_count_unique_substrings()