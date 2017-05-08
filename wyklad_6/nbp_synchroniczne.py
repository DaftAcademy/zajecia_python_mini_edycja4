import datetime
import pprint
import time

import requests

URL = 'http://api.nbp.pl/api/exchangerates/tables/{table}/{startDate}/{endDate}/'
TABLE_TYPE = 'C'

START_DATE = datetime.date(2002, 1, 1)
END_DATE = datetime.date(2017, 1, 1)
DELTA = 92


def get_data_from_nbp(table, start_date, end_date):
    START = time.time()
    r = requests.get(
        URL.format(
            table=TABLE_TYPE,
            startDate=start_date.strftime('%Y-%m-%d'),
            endDate=end_date.strftime('%Y-%m-%d')
        ),
        params={'format': 'json'},
    )
    END = time.time()
    print('{} - {} ({} days)'.format(start_date, end_date, (end_date - start_date).days))
    print(r)
    parsed_json = r.json()
    #pprint.pprint(parsed_json)

    print(type(parsed_json))
    print(len(parsed_json))

    print(START, END, END - START)
    

TOTAL_START = time.time()
full_delta = END_DATE - START_DATE
how_many_runs = full_delta.days / DELTA
if int(how_many_runs) < how_many_runs:
    how_many_runs = int(how_many_runs) + 1
start_date = START_DATE
end_date = START_DATE
for run in range(how_many_runs):
    print('{:*^80}'.format(run))
    start_date = end_date
    end_date = start_date + datetime.timedelta(days=DELTA)
    if end_date > END_DATE:
        end_date = END_DATE
    get_data_from_nbp(TABLE_TYPE, start_date, end_date)
    
TOTAL_END = time.time()

print('TOTAL', TOTAL_START, TOTAL_END, TOTAL_END - TOTAL_START)
