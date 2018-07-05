# -*- coding:utf-8 -*-
import traceback
import sys
import logging
"""
可用来追踪报错
"""
# log = logging.getLogger('mylogger')
# logging.basicconfig(level=logging.DEBUG)
logging.basicConfig(filename='logger.log', level=logging.INFO)


def except_info(e, params=None):
    """
    异常信息打印
    """
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'lineno': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__,
        'message': exc_value.message,
    }
    a = "Throw Exception:{0}\n params:{1} errmsg:{2}".format(traceback_details, params, str(e))
    # print a
    return a


def log_traceback(e,ex_traceback):
    """
    打印返回栈追踪

    """
    tb_lines = traceback.format_exception(e.__class__,e,ex_traceback)
    tb_text = ''.join(tb_lines)
    # print tb_text
    return tb_text


def err():
    """
    报错函数
    :return: 
    """
    a = ad


if __name__ == '__main__':
    try:
        err()
    except Exception as e:
        error = traceback.format_exc()
        logging.error(error)
        print error

        traceback.print_exc(e)  # 常用打印报错
        logging.info('error!!')
        # 捕获报错信息的三种方式

        # 第一种方式（推荐）：
        error = traceback.format_exc()
        logging.error(error)

        msg = repr(error)  # 字符串报错（适合json返回）

        # # 第二种方式（大致信息）
        # error_info = except_info(e)
        # print 'error_info：%s ' % error_info
        # # 第三种方式--栈追踪：
        # _, _, ex_traceback = sys.exc_info()
        # tb_text = log_traceback(e, ex_traceback)
        # print 'tb_text：%s ' % tb_text



