from fibonacci import fibonacci
def test_fibonacci():
    assert fibonacci(1) == 1, "Test case 1 failed"
    assert fibonacci(2) == 1, "Test case 2 failed"
    assert fibonacci(3) == 2, "Test case 3 failed"
    assert fibonacci(4) == 3, "Test case 4 failed"
    assert fibonacci(5) == 5, "Test case 5 failed"
    assert fibonacci(6) == 8, "Test case 6 failed"
    assert fibonacci(7) == 13, "Test case 7 failed"
    assert fibonacci(8) == 21, "Test case 8 failed"
    assert fibonacci(9) == 34, "Test case 9 failed"
    assert fibonacci(10) == 55, "Test case 10 failed"
    print("All tests passed")

test_fibonacci()