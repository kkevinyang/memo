# coding=utf8
"""
数据库的配置文件
使用：需要自定义名称（最好方便区分和记忆的），之后使用时传入改名称即可获取对应连接池

最后生成的格式如下：
database_slave01 = 'mysql://12121@127.0.0.1:3406'
"""
from sqlalchemy.engine.url import URL
import testDev.testfun as testDev


# 从你的总配置中导入debug标识赋值给is_debug，为True时是测试环境（可自行DIY预发布环境配置）
is_debug = testDev.debugdev


# 通用配置（即生产和测试环境一样）
common_setting = {
    # 示例代码
    # 'cps': URL(drivername='mysql', username='user_bg_pata', password="Qq%pAxZJCtfWL^7VsdQ!",
    #            host="12.0.0..1", port=3407, database='info')
}


# ----------------------生产环境和测试环境不一样的，才需要在下面添加-----------------------------------

if is_debug:
    # 测试环境
    databases_setting = {
        # 'db_name': URL(drivername='sqlserver',.......)
    }

else:
    # 生产环境
    databases_setting = {
        # 'db_name': URL(drivername='sqlserver', .......)
    }


databases_setting.update(common_setting)


if __name__ == '__main__':
    print('databases_setting:', databases_setting)


