import pytest
products = [(2, 3,6 ), (1, 99, 99), (0, 99, 0)]

@pytest.mark.parametrize('a, b, product', products)
def test_multi(a, b, product):
    assert a * b == product