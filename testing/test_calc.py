from pythoncode.calc import Calculator
import pytest


class TestCalc:

    def setup_method(self):
        self.cal = Calculator()
        print("setup_method")

    @pytest.mark.parametrize(("a", "b", "result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5)
    ])
    @pytest.mark.add
    def test_add(self, a, b, result, open):
        # cal = Calculator()
        assert self.cal.add(a, b) == result

    @pytest.mark.parametrize(("a", "b", "result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5),
        (1, 0, 0),
        (0, 1, 0)
    ])
    @pytest.mark.div
    def test_div(self, a, b, result, open):
        cal = Calculator()
        assert self.cal.div(a, b) == result

    @pytest.mark.parametrize(("a", "b", "result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5),
        (1, 0, 0),
        (0, 1, 0)
    ])
    @pytest.mark.sub
    def test_sub(self, a, b, result, open):
        # cal = Calculator()
        assert self.cal.sub(a, b) == result

    @pytest.mark.parametrize(("a", "b", "result"), [
        (1, 2, 3),
        (-1, 2, 1),
        (-1, -2, 3),
        (0, 0, 0),
        (0.5, 3, 3.5),
        (1, 0, 0),
        (0, 1, 0)
    ])
    @pytest.mark.mul
    def test_mul(self, a, b, result, open):
        assert self.cal.mul(a, b) == result
