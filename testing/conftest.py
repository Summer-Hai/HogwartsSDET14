import os
import sys, pytest, requests, yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def pytest_addoption(parser):
    mygroup = parser.getgroup("summer")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = '../datas/test/data.yml'

    elif myenv == 'dev':
        datapath = '../datas/dev/data.yml'

    else:
        datapath = '../datas/st/data.yml'

    with open(datapath) as f:
        data = yaml.safe_load(f)

        return myenv, data


@pytest.fixture()
def open1():
    print("\n【开始计算】")
    print("=============")
    yield
    print("\n=============")
    print("【计算结束】")

# def pytest_generate_tests(metafunc:"Metafunc") -> None:
#     if "param" in metafunc.fixturenames:
#         metafunc.parametrize("param",metafunc.module.mydatas,
#                              ids=metafunc.module.myids,
#                              scope='function')
