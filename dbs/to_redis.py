# -*- coding:utf-8 -*-
import redis
import json
import time

# import os
# path = os.path.split(os.path.realpath(__file__))[0]
# path2 = os.path.dirname(os.path.abspath(__file__))
# print(path)
# print(path2)


def main():
    port = [6381, 6379, 6380]
    result_list = []
    for i in range(len(port)):
        # conn = redis.Connection()

        try:
            pool = redis.ConnectionPool(max_connections=10, host='192.168.211.20', port=port[i])
            r = redis.Redis(connection_pool=pool)
            print 'check {0}... '.format(port[i])
            result1 = r.hge
            tall('pata-flow-result:5xxxxxx')
            print 'result1:',result1

            result1 = r.hgetall('pata-flow-result:2xxxxxx')
            print 'result1:',result1
            result2 = r.hgetall('pata-flow-result:4xxxxxx')
            print 'result1:', result2
            # import pdb
            # pdb.set_trace()
            result_list.append(method_name(result))
        except Exception as e:
            time.sleep(1)
            pass
            # print('cant find 1xx!')

        try:
            result = r.hgetall('pata-flow-result:1yyyyyy')
            result_list.append(method_name(result))
        except Exception as e:
            pass
            # print('cant find 1yy!')

    print(result_list)


def add_data():
    pool = redis.ConnectionPool(max_connections=10, host='192.168.211.20', port=6381)
    r = redis.Redis(connection_pool=pool)
    e_key = 24739321
    e_field = 100
    e_value = 'hahahhahah'
    r.hset(e_key, e_field, e_value)




def method_name(result):
    res = json.loads(str(result[b'result:-1'], encoding='utf-8'))
    want = (res['userid'], res['app_list_score_ppx'], res['is_value_error'], res['pc_credit_edu'])
    return want


if __name__ == '__main__':
    main()
    # add_data()

