#!/usr/bin/env python
# coding=utf-8
import os

here = os.path.dirname(os.path.abspath(__file__))
file = os.path.dirname(__file__)
ROOT_DIR = os.path.split(os.path.realpath(__file__))[0]
PARENT_DIR = os.path.abspath(os.path.dirname(__file__)+os.path.sep+"..")
print('here:', here)
print('file:', file)
print('ROOT_DIR:', ROOT_DIR)
print('PARENT_DIR:', PARENT_DIR)
print os.path.abspath(__file__), os.path.dirname(__file__)
"""
[out]:
绝对路径here: C:\git\common
相对路径file: C:/git/common
ROOT_DIR: C:\git\common
PARENT_DIR: C:\git
C:\git\common\use\os_path.py C:/git/common/use
"""