# -*- coding:utf-8 -*-

import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('SELECT * FROM auth_permission where content_type_id=1')
a=c.fetchone()
if a:
    print 2222
print c.fetchone()
# for i in c.fetchall():
#     print i