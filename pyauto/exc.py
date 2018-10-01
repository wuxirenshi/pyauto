# -*- coding: utf-8 -*-

TRANSLATIONS = {
    1000: u'测试环境不存在，请重新输入',
}


class PyAutoException(Exception):
    def __init__(self, error_code, err_msg):
        super(PyAutoException, self).__init__(error_code, err_msg)


def raise_system_exc(err_code, err_msg=None):
    """
    Raise SystemException which error message shall be hide from to user.

    :param err_code: Error code defined in thrift.
    """
    raise PyAutoException(
        err_code,
        err_msg or ''
    )


def raise_user_exc(err_code, err_msg=None):
    """
    Raise UserException which error message shall be show to user.

    :param err_code: Error code defined in thrift.
    """
    translation = err_msg or TRANSLATIONS[err_code]
    raise PyAutoException(
        err_code,
        translation
    )
