# -*- coding: utf-8 -*-

import pytest


# 获取需要运行的环境
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="alta",
        help="environ in [alpha, alta, altb, altc]"
    )


@pytest.fixture
def deploy(request):
    return request.config.getoption("--env")
