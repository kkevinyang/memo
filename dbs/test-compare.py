# -*- coding:utf-8 -*-

import redis
import json
import sqlite3

port = [6379, 6380, 6381]
flowlist=[10001,10002,10003,10004,10005,10006,10007,10008,10009]

result_list = []

# conn = sqlite3.connect('db.sqlite3')
conn = sqlite3.connect('history.db')

c = conn.cursor()
# c.execute('SELECT * FROM auth_permission')


def find(flowid):
    for i in range(len(port)):
        # conn = redis.Connection()
        try:
            pool = redis.ConnectionPool(max_connections=10, host='192.168.211.20', port=port[i])
            r = redis.Redis(connection_pool=pool)
            result = r.hgetall('pata-flow-result:%s' % flowid)
            if result:
                return result
        except Exception as e:
            pass
    return False

for flowid in flowlist:
    result = find(flowid)
    if result:
        result = json.loads(result['result:-1'])
        userid = result['userid']
        print 'userid:', userid

        c.execute('select * from usermmvs where userid=%s' % userid)
        a = c.fetchone()
        if a:
            variablejson = json.loads(a[2])
            if variablejson['listingid'] == result['listingid']:
                print u'相等'
            else:
                print u'不相等'
        else:
            print u'usermmvs中不存在'

    else:
        print u'result不存在'


for i in c.fetchall():
    variablejson = i[2]
    print 'variablejson:',variablejson
    variablejson = json.loads(variablejson)

    flowid = variablejson['flowid']
