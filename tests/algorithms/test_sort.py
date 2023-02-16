from algorithms.sort import get_sorted_list


def test_must_get_sorted_list():
    sorted_list = get_sorted_list(['batman', 'robin', 'coringa'], reverse=False)
    assert sorted_list == ['batman', 'coringa', 'robin']


def test_must_get_reverse_sorted_list():
    sorted_list = get_sorted_list(['batman', 'robin', 'coringa'], reverse=True)
    assert sorted_list == ['robin', 'coringa', 'batman']
