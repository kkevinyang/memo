# -*- coding:utf-8 -*-
"""
有关数据库连接的类
"""
from impala.dbapi import connect
from impala.util import as_pandas


MAX_RETRY_TIMES = 3


class impala_m:
    def __init__(self, host, user, password, port, auth_mechanism='PLAIN'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.auth_mechanism = auth_mechanism

    def conn(self):
        try:
            self.conn = connect(host=self.host,
                                auth_mechanism=self.auth_mechanism,
                                port=self.port,
                                user=self.user,
                                password=self.password)
        except Exception as e:
            raise e

    def cursor(self):
        try:
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise e

    def execute(self, SQL):
        for times in xrange(4):
            try:
                self.conn()
                self.cursor()
                self.cursor.execute(SQL)
                res = as_pandas(self.cursor)

                return res
            except Exception as e:
                if times >= MAX_RETRY_TIMES:
                    raise e
                else:
                    times += 1
                    continue