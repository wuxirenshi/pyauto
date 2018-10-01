# -*- coding: utf-8 -*-

import requests


class RequestSession(object):
    def __init__(self):
        self.__api_session = requests.Session()

    def add_header(self, headers):
        self.__api_session.headers.update(headers)

    @property
    def api_session(self):
        return self.__api_session
