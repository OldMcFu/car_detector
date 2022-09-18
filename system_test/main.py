from cgi import test
import testVc1234
import pytest

class TestClass():
    def test_method1(self):
        timeLine = [
            ["Hallo ".encode(), 100],
            ["wie ".encode(), 200],
            ["geht ".encode(), 300],
            ["es ".encode(), 200],
            ["dir?".encode(), 100],
        ]
        Obj = testVc1234.TestCases(timeLine)
        assert Obj.executeTests() == 0