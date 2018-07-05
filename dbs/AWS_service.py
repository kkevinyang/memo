#!/usr/bin/env python
# coding=utf-8
"""
主要是亚马逊的boto服务
"""
import os
import traceback
from boto import s3
from boto.s3.key import Key as s3Key
import settings


class SC(object):
    Game_s3_bucket = 'yangkai-bucket'
    S3_social_image_path = 'social/images'
    Game_s3_access_key = 'AKIAJ63HDSWK3WBF7JSa'
    Game_s3_secret_access_key = 'QdZ1/n92FnswiXjUl00ncXhfmgq43EbajO+dcZ5f'
    Game_s3_image_path = 'images'
    S3_region = 'us-east-2'


def save_pic_to_s3(name, file_str):
    """
    将帖子图片保存到S3，并返回URL
    """
    # 保存S3
    s3_bucket = get_s3_bucket(SC.Game_s3_bucket)
    key = s3Key(s3_bucket)
    key.key = "%s/%s" % (SC.S3_social_image_path, os.path.basename(name))
    # 发送文件
    key.set_contents_from_string(file_str)
    key.close()
    url = 'https://yangkai-bucket.s3.amazonaws.com/social/images/{0}'.format(name)
    return url


def get_s3_bucket(name):
    try:
        bucket_name = 's3_bucket-%s' % name
        if bucket_name not in settings.CACHES['connection']:
            # 建立连接
            auth = {"aws_access_key_id": SC.Game_s3_access_key, "aws_secret_access_key": SC.Game_s3_secret_access_key}
            handler = s3.connect_to_region(region_name=SC.S3_region, **auth)
            # 获取路径
            bucket = handler.get_bucket(name)
            settings.CACHES['connection'][bucket_name] = bucket
        s3_bucket = settings.CACHES['connection'].get(bucket_name)
        if not s3_bucket:
            # 建立连接
            auth = {"aws_access_key_id": SC.Game_s3_access_key, "aws_secret_access_key": SC.Game_s3_secret_access_key}
            handler = s3.connect_to_region(region_name=SC.S3_region, **auth)
            # 获取路径
            bucket = handler.get_bucket(name)
            settings.CACHES['connection'][bucket_name] = bucket
            s3_bucket = settings.CACHES['connection'].get(bucket_name)

        return s3_bucket

    except Exception as e:
        print traceback.format_exc()
        raise e