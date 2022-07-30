import calculator
import pytest

class TestClass():
    @pytest.mark.parametrize(
    ("n", "expected"), [(1, 2), (2, 3)])
    @pytest.mark.linux
    @pytest.mark.test_id(1501)
    def test_method1(self, n, expected):
        assert calculator.add(n, 1) == expected

    @pytest.mark.test_id(1502)
    def test_method2(self):
        assert calculator.sub(1, 1) == 0