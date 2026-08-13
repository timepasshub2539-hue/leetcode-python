import pytest

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (-5, 5),
    (1000000, 1000000),
])
def test_abs(n, expected):
    assert abs(n) == expected
