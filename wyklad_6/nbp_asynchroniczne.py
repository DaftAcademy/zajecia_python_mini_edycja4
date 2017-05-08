import datetime
import pprint
import time
import asyncio
import json

import aiohttp

URL = 'http://api.nbp.pl/api/exchangerates/tables/{table}/{startDate}/{endDate}/'
TABLE_TYPE = 'C'

START_DATE = datetime.date(2002, 1, 1)
END_DATE = datetime.date(2017, 1, 1)
DELTA = 92

def write_to_file(start_date, end_date, contents):
    # https://github.com/python/asyncio/wiki/ThirdParty#filesystem
    fname = 'from_{}_to_{}_results'.format(start_date, end_date)
    with open(fname, 'w') as f:
        json.dump(contents, f)
    

async def get_data_from_nbp(table, start_date, end_date, run):
    print('Dodaję get_data_from_nbp z argumentami: {}'.format((table, start_date, end_date, run)))
    START = time.time()
    
    url = URL.format(
            table=TABLE_TYPE,
            startDate=start_date.strftime('%Y-%m-%d'),
            endDate=end_date.strftime('%Y-%m-%d')
        )
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={'format': 'json'}) as response:
            print('response url: {}'.format(response.url))
            json_response = await response.json()
            END = time.time()
            print('{:*^80}'.format(run))
            print('{} - {} ({} days)'.format(start_date, end_date, (end_date - start_date).days))
            
            print('type(json_response): {}'.format(type(json_response)))
            print('len(json_response): {}'.format(len(json_response)))
            #pprint.pprint(json_response)
            write_to_file(start_date, end_date, json_response)

            print('run: {}, start: {}, end: {}, duration: {}'.format(run, START, END, END - START))
    
    
async def asynchronous():
    futures = []

    full_delta = END_DATE - START_DATE
    how_many_runs = full_delta.days / DELTA
    if int(how_many_runs) < how_many_runs:
        how_many_runs = int(how_many_runs) + 1
    how_many_runs = int(how_many_runs)
    start_date = START_DATE
    end_date = START_DATE
    
    for run in range(how_many_runs):
        start_date = end_date
        end_date = start_date + datetime.timedelta(days=DELTA)
        if end_date > END_DATE:
            end_date = END_DATE  
        futures.append(get_data_from_nbp(TABLE_TYPE, start_date, end_date, run))

    done, _ = await asyncio.wait(futures)

    for future in done:
        try:
            print('future.result(): {}'.format(future.result()))
        except:
            print("Unexpected error: {}".format(traceback.format_exc()))
    

TOTAL_START = time.time()

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
    
TOTAL_END = time.time()

print('TOTAL', TOTAL_START, TOTAL_END, TOTAL_END - TOTAL_START)
