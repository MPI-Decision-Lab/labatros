from subject_funs import *
import argparse
import json  # (for the string to dictionary conversion)
from inspect import signature  # (to get the signature of a function)

FUNCTION_MAP = {'print_hi': print_hi,
                'print_hello': print_hello,
                'run_zleaf': run_zleaf,
                'kill_process': kill_process,
                'kill_zleaf': kill_zleaf,
                'open_url': open_url}


# create a string for the help page that lists function names together with the arguments this function requires:
args_str = ""
for fun in FUNCTION_MAP:
    args_str += fun + str(signature(FUNCTION_MAP[fun])) + "\n"


# create a parser object:
parser = argparse.ArgumentParser(description='Call function from subject_funs.',
                                 formatter_class=argparse.RawTextHelpFormatter)
# (the formatter_class is needed for a neat output of the string created above)

# fist argument specifies which function we will call:
parser.add_argument('command', choices=FUNCTION_MAP.keys(), help=args_str)
# second argument specifies the input for the function in form of a dictionary
parser.add_argument('-d', '--my-dict', type=json.loads)  # (need json to convert string to dictionary)
args = parser.parse_args()

func = FUNCTION_MAP[args.command]  # get function name
params = args.my_dict  # get function arguments
func(**params)  # call function

# example call: python3 command_line.py print_hi -d '{"myname":"Annika","times":3}'
# python3 command_line.py -h will display help for this file.
#   Below "positional arguments" it will display the set of possible function names
#   and below this the list of function name together with argument keywords (and default values if specified)
#   this function requires.


