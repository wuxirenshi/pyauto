# -*- coding: utf-8 -*-

import pytest
from pyauto.api.order import Order


# 获取测试的域名
@pytest.fixture
def handler(resolve):
    return Order(resolve.get('order'))


# 针对get接口进行测试
def test_get(handler):
    response = handler.get()
    assert response.status_code == 200
    assert response.json()['timeline_url'] == "https://github.com/timeline"
