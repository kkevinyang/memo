# coding=utf8

from db_manager import DbManager

databases = DbManager()


# ----------------------新添加的数据库在此处初始化--------------------------------


# 若有新添加的数据库，先在db_config中添加配置信息后，在下面初始化
# 如：cps_conn = databases.get_one_coon('cps')
# 之后哪里需要用，直接 'from db_manage.db_init import XXXX_conn' 即可
# 使用方法：XXXX_conn.query(<your_sql>)

cps_conn = databases.get_one_coon('cps')


# --------------------需要engine的时候才需要在下面添加------------------------------


# 若是需要直接操作engine，可以在下面进行初始化
# 如：cps_engine = databases.get_one_engine('cps')
# 功能：pd.read_sql(<your_sql>, XXXX_engine)

cps_engine = databases.get_one_engine('cps')


if __name__ == '__main__':
    sql = 'SELECT * from biz.user_mmv_status LIMIT 2'
    results = cps_conn.query(sql)  # 返回包含元组的list
    print(results)
