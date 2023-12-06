from merge_sort import merge_sort
def test_merge_sort():
    assert merge_sort([]) == [], "Error on test case 1"
    assert merge_sort([1]) == [1], "Error on test case 2"
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Error on test case 3"
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Error on test case 4"
    assert merge_sort([-5, -1, -4, 2, 0]) == [-5, -4, -1, 0, 2], "Error on test case 5"
    assert merge_sort([5, 5, 3, 3, 1, 1]) == [1, 1, 3, 3, 5, 5], "Error on test case 6"
    print("All tests pass")

test_merge_sort()