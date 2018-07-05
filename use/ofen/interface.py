# coding=utf8
from __future__ import print_function, absolute_import, division
import sys
import os
import requests
import json
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')


class interface:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __get_response(self, data):
        try:

            response = requests.post(url=self.url, data=data, headers=self.headers, timeout=15).text
            if (response.find("<html>") != -1 and response.find("</html>") != 1) or response == "":
                raise Exception(response)
            response = json.loads(response)
            return response
        except Exception, e:
            exception_info = ''.join([
                '接口:{}连接报错啦！赶紧让开发接口的GGJJ去瞅瞅！'.format(self.get_url()),
                os.linesep,
                '尝试了{}次都没成功，接口估计挂掉啦！'.format(3),
                os.linesep,
                '报错信息:',
                os.linesep,
                str(e.message),
                os.linesep * 2,
                str(traceback.format_exc())
            ])
            raise Exception(exception_info)

    def get_response_params(self, e_s):
        return self.__get_response(*e_s)

    def get_data(self):
        return self.data

    def get_url(self):
        return self.url

    def get_headers(self):
        return self.headers

    def get_single_response(self, data):
        res = self.__get_response(data=data)

        return res

    def get_reponse(self, df_input, field_name):
        self.data = df_input
        raw_output_dict_lst = list()
        if len(df_input) == 0:
            pass
        # 如果需要多次调用接口，则使用多线程完成。
        elif len(df_input) > 1:
            import itertools
            from multiprocessing.dummy import Pool as ThreadPool

            param_lst = df_input[field_name].values.tolist()
            param_lst = itertools.izip(param_lst,
                                      itertools.repeat(self.get_url()),
                                      itertools.repeat(self.get_headers()))

            pool10 = ThreadPool(10)
            raw_output_lst = pool10.map(self.get_response_params, param_lst)
            pool10.close()
            pool10.join()

            for i in xrange(len(raw_output_lst)):
                raw_output_dict = raw_output_lst[i]
                raw_output_dict_lst.append(raw_output_dict)
        # 如果只需要读一次接口，则直接连接读取
        elif len(df_input) == 1:
            raw_output_dict = self.__get_response(df_input[field_name].ix[0])
            raw_output_dict_lst.append(raw_output_dict)

        else:
            pass

        return raw_output_dict_lst
