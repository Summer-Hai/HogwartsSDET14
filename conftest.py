import os
import sys, pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(autouse="true")
def open():
    print("\n【开始计算】")
    print("=============")
    yield ["a", "b", "result"]

    print("=============")
    print("【计算结束】")
