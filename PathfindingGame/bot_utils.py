import argparse
import import_data as dt
def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help="Input file name")
    parser.add_argument('-o', type=str, help="Output file name")
    args = parser.parse_args()
    return str(args.i), str(args.o)
input_file, output_file = run_cli()
def get_bot_index(data,bot_name):
    bot_lst = data['bots']
    index = 0
    for item in bot_lst:
        if item['name'] == bot_name:
            return index
        index += 1

