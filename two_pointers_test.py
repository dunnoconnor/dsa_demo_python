from two_pointers import max_profit

def test_max_profit():
    assert max_profit([7,1,5,3,6,4]) == 7, 'Test case 1 failed'
    assert max_profit([1,2,3,4,5]) == 4, 'Test case 2 failed'
    assert max_profit([7,6,4,3,1]) == 0, 'Test case 3 failed'
    print("All tests passed")

test_max_profit()