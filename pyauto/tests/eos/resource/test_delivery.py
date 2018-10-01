# -*- coding: utf-8 -*-

import pytest
from pyauto.api.delivery import Delivery


# 获取测试的域名
@pytest.fixture
def handler(resolve):
    return Delivery(resolve.get('delivery'))


def setup_module(module):
    pass


def teardown_module(module):
    pass


# 针对get接口进行测试
def test_get(handler):
    print 123
    response = handler.get()
    assert response.status_code == 200
    assert response.json()['timeline_url'] == "https://github.com/timeline"
