# -*- coding: utf-8 -*-

from .base import BaseApi


class Delivery(BaseApi):
    def __init__(self, domain):
        super(Delivery, self).__init__(domain)

    def get(self):
        url = self.domain + "/feeds"
        return self.api_session.get(url)