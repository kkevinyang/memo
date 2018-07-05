# -*- coding: utf-8 -*-
import pandas as pd

df = pd.DataFrame(
    data=[[4263137, 1, '2017-02-01 12:11:13.000000'], [19909478, -1, '2018-01-01 12:11:13.000000']],
    columns=['userid', 'listingid', 'listingtime'])
one_time = "2017-09-01 12:11:13.000000"


dates = pd.to_datetime("today").date() - pd.to_datetime(one_time).date()
print '天数差额是：'
print dates
print dates.days
# print pd.to_datetime(df.listingtime).date()
# print pd.to_datetime("today").date()

# pd.to_datetime("today").date() - pd.to_datetime(row["duedate"]).date()).days