import pandas as pd 
from  tabulate import tabulate

def prettyprint(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))

def list_to_sql_params(taglist):
    og = taglist
    taglist = tuple(taglist)
    if len(taglist) == 1:
        taglist = "('" + taglist[0] + "')"
    return taglist
