from exemples.json_refactor import Calculator
from contextlib import nullcontext
import pytest

class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, nullcontext()),
            (2, -1, -2, nullcontext()),
            (5, 0, 1, pytest.raises(ZeroDivisionError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res


    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 3),
            (2, -1, 1),
            (5, 5, 10),
        ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res
