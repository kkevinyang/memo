# encoding: utf-8
import pandas as pd
import MySQLdb
mysqlconn={'username': 'xxxxx', 'ip': 'xxxxx',
           'password': 'xxxxxx', 'db': 'xxxxxx', 'port': 3306}
conn = MySQLdb.connect(host=mysqlconn['ip'], user=mysqlconn['username'],
                       passwd=mysqlconn['password'], db=mysqlconn['db'],
                       port=mysqlconn['port'])

cur = conn.cursor()

cur.execute('select * from user_pre_score_var limit 1')
print(cur.fetchall())


def fengzhuang():
    """
    对数据库查询到的数据进行封装后转存dataframe
    """
    final_sql = """
        select 
        cmstr_sou_flag,
        cmcnt_bid_his_sou_app,
        cmcnt_bid_l7d_sou_app,
        cmcnt_bid_l1m_sou_app,
        cmcnt_bid_l3m_sou_app,
        cmcnt_chan_l7d_pus,
        cmcnt_chan_l1m_pus,
        cmcnt_chan_l3m_pus
        from cps_verify_info
    """
    cur.execute(final_sql)
    column_name_lst = [i[0] for i in cur.description]

    res = cur.fetchall()
    print('res:', res)

    sql_output = [dict(zip(column_name_lst, item)) for item in res]
    print('sql_output：', sql_output)
    cur.close()
    conn.commit()
    conn.close()
    df_output = pd.DataFrame.from_records(sql_output)

