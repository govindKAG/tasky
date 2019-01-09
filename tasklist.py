import pandas as pd
import sqlite3
import numpy as np
from util import prettyprint
from util import list_to_sql_params
from util import parse_date
from util import filter_due_date

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


    def list_all_tags(self, taglist=None, due=None):
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
        #concept code for checking due date
        #df['due_list'] = df['due'].apply(lambda x: parse_date(x) <=  parse_date('tomorrow'))
        prettyprint(filter_due_date(df, 'tomorrow'))


    def list_only_tags(self, taglist=None):
        df = pd.read_sql_query(f"SELECT * FROM {TABLE}", self.connection)
        df.replace(np.nan, "", inplace=True)
        df['alltags'] = df['tag1'].astype(str) + '_' + df['tag2'].astype(str) + '_'  + df['tag3'].astype(str) + '_' + df['tag4'].astype(str) + '_' + df['tag5'].astype(str) + '_' + df['tag6'].astype(str) 
        for tag in taglist:
            df = df[df['alltags'].str.contains(tag)] #add exit condition here
        prettyprint(df)


#unit test
mainlist = taskList()
mainlist.view_all()
mainlist.list_all_tags(taglist=['easy', 'hard'])
mainlist.list_all_tags(taglist=['hard'])
mainlist.list_all_tags(taglist=['mall'])
mainlist.list_only_tags(taglist = ['easy','mall'])
mainlist.list_only_tags(taglist = ['hard','laptop'])
mainlist.list_only_tags(taglist = ['hard','easy'])

#mainlist.add(title = 'write project report', due='1/1/19', date_added='30/12/18', date_completed= '12/12/12/', tag1 = 'hard', tag2 = 'time consuming', tag3 = 'laptop')
#mainlist.view_all()
#mainlist.add(title = 'buy razors', due='1/1/19', date_added='30/12/18', date_completed= '12/12/12/', tag1 = 'easy', tag2 = 'supermarket')
#mainlist.view_all()
