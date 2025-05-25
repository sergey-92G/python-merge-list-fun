
from merge_utils.core import merge_dicts_auto

def test_merge():
    d1 = {'a': 1, 'b': [1], 'c': {'x': 1}, 's': {'python'}}
    d2 = {'a': 2, 'b': [2], 'c': {'y': 2}, 's': {'ai'}}
    result = merge_dicts_auto(d1, d2)
    assert result['a'] == 3
    assert result['b'] == [1, 2]
    assert result['c'] == {'x': 1, 'y': 2}
    assert result['s'] == {'python', 'ai'}
    print("✔ test_merge passed")

def test_custom_strategy():
    d1 = {'a': 10, 'b': 5}
    d2 = {'a': 20, 'b': 15}
    strategy = {'a': lambda x, y: max(x, y)}
    result = merge_dicts_auto(d1, d2, strategy=strategy)
    assert result['a'] == 20
    assert result['b'] == 20
    print("✔ test_custom_strategy passed")

if __name__ == '__main__':
    test_merge()
    test_custom_strategy()
