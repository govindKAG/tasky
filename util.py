import pandas as pd 
from  tabulate import tabulate
import datetime as dt
import dateparser as dp
from timefhuman import timefhuman as nlp

DATE_FORMAT = '%d/%m/%Y'

def prettyprint(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))

def list_to_sql_params(taglist):
    og = taglist
    taglist = tuple(taglist)
    if len(taglist) == 1:
        taglist = "('" + taglist[0] + "')"
    return taglist

def format_date(date):
    return date.strftime(DATE_FORMAT)

def parse_date(description):
    parsed_date = None
    try:
        parsed_date =  nlp(description)
    except:
        print('hit fallback')
        parse_date = dp.parse(description)
    return parsed_date
        

print(parse_date('after 2 days'))
print(parse_date('tomorrow'))
print(parse_date('in 4 days'))
print(parse_date('december 10'))
