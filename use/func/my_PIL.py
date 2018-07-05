# -*- coding:utf-8 -*-
import StringIO
import datetime
from PIL import Image

# now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%M%f')
# name = now + '.png'


def _handle_image(file_str):
    """
    对单个文件进行处理：
            1. 生成缩略图
            2. 测长宽
            3. 存储到S3
            4. 返回file_dict
    """
    # 生成名字
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%M%f')
    file_name = now + '.png'

    # 采用StringIO直接将文件写到内存，省去写入硬盘,并加载进PIL获取尺寸
    imgBuf = StringIO.StringIO(file_str)
    img = Image.open(imgBuf)
    # print 'width, height:',width, height

    # 存到S3并拿到URL
    url = save_pic_to_s3(file_name, file_str)
    print 'url:', url
    # print 'imgBuf:', imgBuf.getvalue()

    thumbnailUrl = create_thumbnail(img, imgBuf)

    imgBuf.close()
    file_dict = {
        'width': img.size[0],
        'height': img.size[1],
        'thumbnailUrl': thumbnailUrl,
        'source': url,
        'type': 1
    }
    return file_dict


def create_thumbnail(img, imgBuf):
    """
    生存缩略图，返回URL
    :return: 
    """
    width, height = img.size[0], img.size[1]
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%M%f')
    thumbnail_name = now + '_thumbnail.png'

    # 生存缩略图存在缓冲区内(全部裁剪成80*80的)
    if width > height:
        offset = int(width - height) / 2
        img = img.transform((height, height), Image.EXTENT, (offset, 0, int(width - offset), height))
    else:
        offset = int(height - width) / 2
        img = img.transform((width, width), Image.EXTENT, (0, offset, width, (height - offset)))
    img.thumbnail((80, 80))

    # 清除缓冲区
    imgBuf.seek(0)
    imgBuf.truncate()
    img.save(imgBuf, 'png')

    # 存到S3并拿到URL
    thumbnailUrl = save_pic_to_s3(thumbnail_name, imgBuf.getvalue())
    return thumbnailUrl