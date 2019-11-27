from subject_funs import *
import argparse
import json

FUNCTION_MAP = {'print_hi': print_hi,
                'print_hello': print_hello}

parser = argparse.ArgumentParser(description='Call function from subject_funs.')
parser.add_argument('command', choices=FUNCTION_MAP.keys())
parser.add_argument('-d', '--my-dict', type=json.loads) #need json to convert string to dictionary

args = parser.parse_args()
print(args)

func = FUNCTION_MAP[args.command]
params = args.my_dict
func(**params)

#example call: python3 command_line.py print_hi -d '{"myname":"Annika","times":3}'


