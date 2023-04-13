from bot import Bot
import json
import import_data as dt
import time
import timeit
import argparse
from bot_utils import input_file, output_file
from map import *
grid = Map()
data = dt.import_dt(input_file)
index1 = get_bot_index(data, 'tadao')
index2 = get_bot_index(data, 'top')
end_1 = dt.import_dt(input_file)['coin']
end_2 = dt.import_dt(input_file)['coin']
top = Bot(data['bots'][index2]['name'], data['bots'][index2]['pos'], end_2, data['bots'][index2]['status'], data['bots'][index2]['score'], grid)
path_top = top.find_path()
while path_top:
    grid = Map()
    data = dt.import_dt(input_file)
    end_1 = dt.import_dt(input_file)['coin']
    end_2 = dt.import_dt(input_file)['coin']
    tadao = Bot(data['bots'][index1]['name'], data['bots'][index1]['pos'], end_1, data['bots'][index1]['status'], data['bots'][index1]['score'], grid)
    top = Bot(data['bots'][index2]['name'], data['bots'][index2]['pos'], end_2, data['bots'][index2]['status'], data['bots'][index2]['score'], grid)
    top.check_other(tadao)
    path_top = top.find_path()
    print(path_top)
    if path_top == top.end.coor():
        pass
    elif top.status == "move" and len(path_top) >= 2:
        top.move(path_top[-1],path_top[-2])
        top.write_to_json()
    time.sleep(1)
        
