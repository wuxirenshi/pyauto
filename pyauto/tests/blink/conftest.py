# -*- coding: utf-8 -*-

import pytest
from os import path
import yaml
from pyauto.exc import raise_user_exc

current_path = path.dirname(path.abspath(__file__))


# 根据不同的环境获取数据
@pytest.fixture
def resolve(deploy):
    resolve_yaml = yaml.load(file(path.join(current_path, 'blink.yaml')))
    data = resolve_yaml.get(deploy)
    return data if data else raise_user_exc(1000)

