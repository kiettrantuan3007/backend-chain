from bot import Bot
import import_data as dt
import time
import timeit
from bot_utils import input_file, output_file
from map import *
grid = Map()
data = dt.import_dt(input_file)
index1 = get_bot_index(data, 'tadao')
index2 = get_bot_index(data, 'top')
end_1 = dt.import_dt(input_file)['coin']
end_2 = dt.import_dt(input_file)['coin']
tadao = Bot(data['bots'][0]['name'], data['bots'][0]['pos'], end_1, data['bots'][0]['status'], data['bots'][0]['score'], grid)
path_tadao = tadao.find_path()
while path_tadao:
    grid = Map()
    data = dt.import_dt(input_file)
    end_1 = dt.import_dt(input_file)['coin']
    end_2 = dt.import_dt(input_file)['coin']
    tadao = Bot(data['bots'][0]['name'], data['bots'][0]['pos'], end_1, data['bots'][0]['status'], data['bots'][0]['score'], grid)
    top = Bot(data['bots'][1]['name'], data['bots'][1]['pos'], end_2, data['bots'][1]['status'], data['bots'][1]['score'], grid)
    tadao.check_other(top)
    path_tadao = tadao.find_path()
    print(path_tadao)
    if path_tadao == tadao.end.coor():
        pass
    elif tadao.status == "move" and len(path_tadao) >= 2:
        tadao.move(path_tadao[-1],path_tadao[-2])
        tadao.write_to_json()
    time.sleep(1)

        
