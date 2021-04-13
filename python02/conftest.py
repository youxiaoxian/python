import pytest
from python02.common import get_param

from python02.Calculator import Calculator

# fixture实现set up和tear down
@pytest.fixture(scope='class')
def inicalc_class():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")


# fixture实现参数化
@pytest.fixture(params=get_param()['add_int'], ids=get_param()['ids'])
def get_add_int_param_calc(request):
    return request.param


@pytest.fixture(params=get_param()['add_float'], ids=get_param()['ids'])
def get_add_float_param_calc(request):
    return request.param


@pytest.fixture(params=get_param()['div_int'], ids=get_param()['ids'])
def get_div_int_param_calc(request):
    return request.param


@pytest.fixture(params=get_param()['div_float'], ids=get_param()['ids'])
def get_div_float_param_calc(request):
    return request.param


def pytest_collection_modifyitems(session, config, items: list):
    print("这是收集所有测试用例的方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        print(item.name)
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
        print(item._nodeid)
