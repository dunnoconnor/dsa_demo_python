from binary_search import binary_search

def test_binary_search():
    assert binary_search([2,3,4,10,40,45], 10) == 3
    assert binary_search([2,3,5,10,13,40,60], 13) == 4
    assert binary_search([2,3,4,10,40,45], 50) == -1
    assert binary_search([2,3,5,10,13,40,60], 50) == -1
    print("All tests passed")
    
test_binary_search()