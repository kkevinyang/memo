# coding=utf8
import pdb
from sqlalchemy import create_engine


class Conns(object):
    """
    基于sqlalchemy的engine封装
    功能：连接中断重连机制；
         engine内置连接池，可设置连接数，最大连接数和重连时间
        可以通过add_name参数给返回数据添加表头
    使用：实例化后调用query即可获取所有返回结果，不需要创建cursor和close；
    """
    def __init__(self, db_conf):
        self.engine = create_engine(db_conf, pool_size=2, max_overflow=-1, pool_recycle=60*10)

    def query(self, sql, add_name=False, only_one=False):
        """
        从db读取数据
        :param sql: 要执行的sql
        :param add_name: 为True时，在结果上添加表头
        :param only_one: 为True时，只返回一个结果
        返回包含元组的list
        """
        res_proxy = self._execute(sql)

        if not res_proxy:
            return None

        if not res_proxy.returns_rows:
            # 即无返回值，例如update，insert等
            return 'done!'

        if only_one:
            res = res_proxy.fetchone()
        else:
            res = res_proxy.fetchall()

        results = self.__add_name(res_proxy, res) if add_name else res

        return results

    def _execute(self, sql, conn=None):
        """
        直接执行sql
        功能：可用于删除或者修改时执行单条sql

        :param conn: 可指定初始化过的connection来执行sql
        :return: ResultProxy对象或者None
        """
        for i in range(3):
            try:
                if conn:
                    res_proxy = conn.execute(sql)
                else:
                    res_proxy = self.engine.execute(sql)
                return res_proxy
            except Exception as e:
                print('sql execute failed! the error is:', e)
                print('try again...')
                if i > 1:
                    print('sql execute finally failed! the error is:', e)
                    raise e

    def read_sqls(self, sqls, add_name=False):
        """
        执行多条sql
        特点：事务级别的，任一条sql出错内部会自动回滚

        :param sqls: 包含多条sql的list
        :param add_name: 为True时，在结果上添加表头
        :return: 包含多条结果的list
        """
        results_list = []
        with self.engine.begin() as connection:
            for sql in sqls:
                res_proxy = self._execute(sql, connection)

                if not res_proxy:
                    continue
                
                if not res_proxy.returns_rows:
                    # 即无返回值，例如update，insert等
                    return 'done!'

                res = res_proxy.fetchall()

                results = self.__add_name(res_proxy, res) if add_name else res

                results_list.append(results)
        return results_list

    def __add_name(self, res_proxy, naked_res):
        """
        给fetch的结果添加表头
        :param res_proxy: ResultProxy对象
        :param naked_res: 没有表头的结果
        :return: 包装后的结果
        """
        column_name_lst = res_proxy.keys()
        if isinstance(naked_res, tuple):
            results = dict(zip(column_name_lst, naked_res))
        elif isinstance(naked_res, list):
            results = [dict(zip(column_name_lst, item)) for item in naked_res]
        else:
            raise Exception('传入的数据必须是tuple或者list格式的！')
        return results

    def get_engine(self):
        """
        直接拿到对应数据库引擎，可用于pd.read_sql,也可用于自己操作
        doc：http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Engine
        :return: Engine()对象
        """
        return self.engine


if __name__ == '__main__':
    sql = 'SELECT * from biz.user LIMIT 2'
    db_conf = 'mysql://111:1212@127.0.0.1:3406'
    slave01_conn = Conns(db_conf=db_conf)
    pdb.set_trace()

    res2 = slave01_conn.query(sql)  # 返回包含元组的list

    print(res2)
