def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def remove_duplicates(lst):
    return list(set(lst))
