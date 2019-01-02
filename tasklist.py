import pandas as pd
import sqlite3

from tabulate import tabulate
pd.set_option('display.max_columns', None)

class taskList(object):
    def __init__(self):
        self.connection = sqlite3.connect('taskyData.db')
    def add(self, title, due, date_added, date_completed, tag1=None,tag2=None,tag3=None,tag4=None,tag5=None,tag6=None):
        values = {'title':title, 'due':due,'date_added':date_added,'date_completed':date_completed,'tag1':tag1,'tag2':tag2,'tag3':tag3, 'tag4':tag4, 'tag5':tag5, 'tag6':tag6}
        columns = ', '.join(values.keys())
        placeholders = ', '.join('?' * len(values))
        sql = 'INSERT INTO {table} ({}) VALUES ({})'.format(columns, placeholders, table = 'tasky')
        with self.connection as cur:
            cur.execute(sql, list(values.values()))
    def view_all(self):
        df = pd.read_sql_query("SELECT * FROM tasky", self.connection)
        print(tabulate(df, headers='keys', tablefmt='psql'))


mainlist = taskList()
mainlist.view_all()
mainlist.add(title = 'write project report', due='1/1/19', date_added='30/12/18', date_completed= '12/12/12/', tag1 = 'hard', tag2 = 'time consuming', tag3 = 'laptop')
mainlist.view_all()
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
