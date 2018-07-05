import sqlite3
import json
import pandas as pd

con = sqlite3.connect('history.db')
cur = con.cursor()
sql = 'select inserttime from user_pata_results'
cur.execute(sql)
res = cur.fetchall()
res = [json.loads(i[0].replace('\\\\\\', '')) for i in res]
df = pd.DataFrame(res)
columns = [
    'userid',
    'als_m1_id_nbank_orgnum',
    'random_number',
    'cmcnt_chan_l3m_pus',
    'isJiangji',
    'creditLevelJiangji',
    'creditLevelModel',
    'creditLevelDuotou',
    'isfrstdealmthG1',
]
df = df[columns]
df['userid'] = df['userid'].astype(int)
