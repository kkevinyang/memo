# coding=utf8
import pdb

from conns import Conns
from db_config import databases_setting
from .utils import Singleton


class DbManager(Singleton):
    """
    数据库配置管理器
    功能：mysql,sqlserver等多种数据库通用；
        可以获取到对应engine
    使用：在全局中实例化一次即可（有多个进程除外），提前用get_one_coon初始化各个db连接
        之后默认用query()即可执行sql
    """
    def __init__(self):
        self.conns = {db_name: Conns(db_conf) for db_name, db_conf in databases_setting.iteritems()}
        print('init conns all done!')
        print('db infos:', self.conns)

    def get_one_coon(self, db_name):
        """
        获取连接对象
        """
        conn = self.conns.get(db_name, None)
        if not conn:
            raise Exception('db_config中没有 {} 这个数据库！'.format(db_name))
        return conn

    def get_one_engine(self, db_name):
        """
        获取engine对象
        """
        return self.get_one_coon(db_name).get_engine()


if __name__ == '__main__':
    sql = 'SELECT * from biz.user_mmv_status LIMIT 2'
    databases = DbManager()
    slave01_conn = databases.get_one_coon('slave01')
    pdb.set_trace()

    results = slave01_conn.query(sql)  # 返回包含元组的list

    print(results)


