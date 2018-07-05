# -*- coding:utf-8 -*-
import yaml


def read_yaml(yaml_file):
    '''
    :param yaml_file: 需要读取的yaml文件
    :return: 以dict的格式返回yaml文件中的信息
    '''

    try:
        with open(yaml_file) as f:
            yaml_res = yaml.load(f)
            return yaml_res
    except Exception as e:
        raise e