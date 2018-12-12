# -*- coding:utf-8 -*-
import pandas as pd
import json
import decimal
import datetime
import numpy as np
import pandas as pd

import pdb
import simplejson
from impala.dbapi import connect
from impala.util import as_pandas

sql = """
select 
sum(case when product_lable = '城市贷' and duedate_1_op_pess > 0 then 1 else 0 end) / sum(case when product_lable = '城市贷' then 1 else 0 end) duedate_1_op_pess_lid_rt_city,
sum(case when product_lable = '城市贷' and duedate_10_op_pess > 0 then 1 else 0 end) / sum(case when product_lable = '城市贷' then 1 else 0 end) duedate_10_op_pess_lid_rt_city
from fxzc.rctp_all_mt_listing_vintage_tmp_tb
where new_product_name not in ('无效标_其他','无效标_pdl新客','无效标_3c贷','无效标_pdl老客') 
and datediff(now(),adddate(add_months(auditing_date,1),1)) >= 0
and duedate_1_op_pess is not null
group by strleft(auditing_date,10)
order by strleft(auditing_date,10) desc
limit 300
"""

json_1 = [{'num': 1112, 'A': datetime.datetime.now(), 'key3': decimal.Decimal('1.45'), 'a': np.nan}]
# json_1 = [{'a': 12}]


class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        print('obj:', obj)
        if isinstance(obj, decimal.Decimal):
            return float(obj)

        if isinstance(obj, datetime.datetime):
            return obj.__str__()

        return super(ExtendJSONEncoder, self).default(obj)


conn = connect(host='10.2.8.98', auth_mechanism='PLAIN', port=21050, user='zhaozhiyuan', password='zhaozhiyuan')
cursor = conn.cursor()
cursor.execute(sql)
df = as_pandas(cursor)

# column_name = [item[0] for item in cursor.description]
# fetch_res = cursor.fetchall()
# res = [dict(zip(column_name, item)) for item in fetch_res]
# df = pd.DataFrame(json_1)
# pdb.set_trace()
# print('df:', df)
# js = df.to_json(orient='records', date_format='')
js = df.to_json(orient='records', date_format="iso", date_unit='s')

print('js:', js)

# dumps(df.where(pd.notnull(df), None)))

# result = simplejson.dumps(json_1, ignore_nan=True, iso_datetime=True, use_decimal=True)
# # result = json.dumps(json_1, cls=ExtendJSONEncoder, allow_nan=False)
# print('result:', result)
