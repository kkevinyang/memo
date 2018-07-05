# -*- coding: utf-8 -*-
import requests
import json


def post_token(api_url='https://exmail.qq.com:/cgi-bin/token'):
    """
    更新/获取腾讯的Token
    """
    agent_secret = 'NiOmcvhOfJfX99UU1086ZReDlcgS4FzlY4nAADqslBMsxwqk9GyY-LPOI0ROpv-w'
    agent_id = 'shinezonetest'
    print 'agent_id:', agent_id
    print 'agent_secret:', agent_secret

    resp = requests.post('{api_url}?grant_type=client_credentials'
                         '&client_id={client_id}'
                         '&client_secret={client_secret}'.format(api_url=api_url,
                                                                 client_id=agent_id,
                                                                 client_secret=agent_secret),
                         timeout=60)
    json_content = json.loads(resp.content)
    print '{0}'.format(json_content)
    if 'access_token' in json_content and 'token_type' in json_content:
        return '{0} {1}'.format(json_content['token_type'], json_content['access_token'])


def get_token(api_url='https://api.exmail.qq.com/cgi-bin/gettoken'):
    corpid = 'wm1ce1a759e15e8137'
    corpsecret = 'pgPaIdxu6tAt9cZRAB6dBFlLyJhsJsdeu2L6hJuycJQVkS0N7Bjq5sIKMJ2v0btU'
    resp = requests.get('{api_url}?'
                         '&corpid={corpid}'
                         '&corpsecret={corpsecret}'.format(api_url=api_url,
                                                           corpid=corpid,
                                                           corpsecret=corpsecret),
                         timeout=60)
    json_content = json.loads(resp.content)
    print 'json_content:',json_content
    if 'access_token' in json_content and 'token_type' in json_content:
        token = '{0} {1}'.format(json_content['token_type'], json_content['access_token'])
        print token
        return token


def get_part_list(api_url='https://api.exmail.qq.com/cgi-bin/department/list'):
    """
    获取子部门列表
    """
    access_token = 'ZSoDzdxkZ7AnJ59Mwn15cSnU7jsLmURraV2UuIKjAtLX956x_GQU8OQ_B1nQUADAmYjMPKuajKiV-c6NjhwNPg'
    id = '1'
    request_url = '{api_url}?access_token={access_token}&id={id}'.format(api_url=api_url,
                                                                     access_token=access_token,
                                                                     id=id)

    resp = requests.get(request_url, timeout=60)
    json_content = json.loads(resp.content)
    return_dict = modify_part_list(json_content)
    print return_dict


def modify_part_list(json_content):
    """
    将腾讯返回的子部门数据格式处理成旧版的
    要导出的格式：
    {Count": 3,
    "List": [
        {"Value": "部门 a"},
        {"Value": "部门 B"},
        {"Value": "部门 c"}]
    }
    """
    count = 0
    department_list = []
    if 'department' in json_content:
        department_list = json_content['department']
        count = len(department_list)
        for department in department_list:
            department.pop('id', None)
            department.pop('parentid', None)
            department.pop('order', None)
            department['Value'] = department.pop('name', '')
    # 重组的返回字典
    return_dict = {
        "Count": count,
        "List": department_list
    }
    return return_dict

if __name__ == '__main__':
    get_part_list()