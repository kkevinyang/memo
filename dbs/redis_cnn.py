# -*- coding:utf-8 -*-

import redis

redis_conn = redis.StrictRedis(host='localhost', port=6379)

# 组合key
sz_id = '001'
user_key = 'user:' + sz_id

# hash操作
user_list = redis_conn.hmget(user_key, ['nickname', 'head_icon'])
# 存入缓存并设置过期时间
redis_conn.hmset(user_key, {'nickname': 'gg', 'head_icon': '1232'})
redis_conn.expire(user_key, 60*60*24)

# set操作
is_or_not = redis_conn.sismember(user_key)
redis_conn.sadd(user_key, 12312)
