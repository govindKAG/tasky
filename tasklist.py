import pandas as pd
import sqlite3
import numpy as np
from util import prettyprint
from util import list_to_sql_params

from tabulate import tabulate
pd.set_option('display.max_columns', None)

DB = "taskyData.db"
TABLE = "tasky"
class taskList(object):

    def __init__(self):
        self.connection = sqlite3.connect(DB)


    def add(self, title, due, date_added, date_completed, tag1=None,tag2=None,tag3=None,tag4=None,tag5=None,tag6=None):
        values = {'title':title, 'due':due,'date_added':date_added,'date_completed':date_completed,'tag1':tag1,'tag2':tag2,'tag3':tag3, 'tag4':tag4, 'tag5':tag5, 'tag6':tag6}
        columns = ', '.join(values.keys())
        placeholders = ', '.join('?' * len(values))
        sql = 'INSERT INTO {table} ({}) VALUES ({})'.format(columns, placeholders, table = TABLE)
        with self.connection as cur:
            cur.execute(sql, list(values.values()))


    def view_all(self):
        df = pd.read_sql_query(f"SELECT * FROM {TABLE}", self.connection)
        prettyprint(df)


    def list_all_tags(self, taglist=None):
        taglist = list_to_sql_params(taglist)

        df = pd.read_sql_query( f'''SELECT * FROM {TABLE} WHERE  
                tag1 IN {taglist} OR
                tag2 IN {taglist} OR
                tag3 IN {taglist} OR
                tag4 IN {taglist} OR
                tag5 IN {taglist} OR
                tag6 IN {taglist};
                ''', self.connection)

        prettyprint(df)


    def list_only_tags(self, taglist=None):
        df = pd.read_sql_query(f"SELECT * FROM {TABLE}", self.connection)
        df.replace(np.nan, "", inplace=True)
        df['alltags'] = df['tag1'].astype(str) + df['tag2'].astype(str) + df['tag3'].astype(str) + df['tag4'].astype(str) + df['tag5'].astype(str) + df['tag6'].astype(str) 
        print(df.tag3.dtype)
        prettyprint(df)


#unit test
mainlist = taskList()
mainlist.view_all()
mainlist.list_all_tags(taglist=['easy', 'hard'])
mainlist.list_all_tags(taglist=['hard'])
mainlist.list_all_tags(taglist=['mall'])
mainlist.list_only_tags()

#mainlist.add(title = 'write project report', due='1/1/19', date_added='30/12/18', date_completed= '12/12/12/', tag1 = 'hard', tag2 = 'time consuming', tag3 = 'laptop')
#mainlist.view_all()
#mainlist.add(title = 'buy razors', due='1/1/19', date_added='30/12/18', date_completed= '12/12/12/', tag1 = 'easy', tag2 = 'supermarket')
#mainlist.view_all()
##con = sqlite3.connect('taskyData.db')
#
##values = {'title':"buy some milk", 'due':'1/12/19','date_added':'1/1/19','date_completed':"2/1/19",'tag1':'easy','tag2':'mall','tag3':'urgent'}
##columns = ', '.join(values.keys())
##placeholders = ', '.join('?' * len(values))
##sql = 'INSERT INTO {table} ({}) VALUES ({})'.format(columns, placeholders, table = 'tasky')
#
#print(sql)
#print(values.values())
##with con as cur:
##    cur.execute(sql, list(values.values()))
#
#df = pd.read_sql_query("SELECT * FROM tasky", con)
#print(df.iloc[:,:4])
#
#print(tabulate(df, headers='keys', tablefmt='psql'))
#print(tabulate(df.iloc[:,:4], headers='keys', tablefmt='psql'))
