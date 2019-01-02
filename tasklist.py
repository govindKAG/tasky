import sqlite3
import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
con = sqlite3.connect('taskyData.db')

values = {'title':"buy some milk", 'due':'1/12/19','date_added':'1/1/19','date_completed':"2/1/19",'tag1':'easy','tag2':'mall','tag3':'urgent'}
columns = ', '.join(values.keys())
placeholders = ', '.join('?' * len(values))
sql = 'INSERT INTO {table} ({}) VALUES ({})'.format(columns, placeholders, table = 'tasky')

print(sql)
print(values.values())
#with con as cur:
#    cur.execute(sql, list(values.values()))

df = pd.read_sql_query("SELECT * FROM tasky", con)
print(df.iloc[:,:4])

print(tabulate(df, headers='keys', tablefmt='psql'))
print(tabulate(df.iloc[:,:4], headers='keys', tablefmt='psql'))
