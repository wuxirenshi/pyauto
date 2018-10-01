# -*- coding: utf-8 -*-

from pyauto.request.handler import RequestSession


# 基础类，可以进行登陆后token的写入，进行免登陆
class BaseApi(object):
    def __init__(self, domain):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        request_session = RequestSession()
        request_session.add_header(headers)
        self.api_session = request_session.api_session

        self.domain = domain
