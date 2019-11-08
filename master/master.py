#!/usr/bin/env python3

import socket
import pickle

hosts = ['127.0.0.1', '127.0.0.1']
specs_list = [{"keyword": "rabbit", "website": "nature.com", "clientno": "client21"},{"keyword": "mouse", "website": "science.com", "clientno": "client21"}]
port = 65432




# This created a lot of troubles because of the string referencing
# We solved it buy creating a new dictionary from scratch instead of assigning it to a new name
def format_command(command, specs):
    my_new_dict = {}
    for key in command[1]:
        my_new_dict[key] = command[1][key].format(**specs)
    return my_new_dict


# We are working on this function
def stream_command(command, machines, machinespecs = None):
    """
    machines: list of machines
    """

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for no, mach in enumerate(machines):
        if machinespecs:
            command_to_run = format_command(command, machinespecs[no])
            print(command)
            print(command_to_run)
        else:
            command_to_run = command

        conn.connect((mach, port))
        data_to_send = command_to_run
        data = pickle.dumps(data_to_send)
        conn.sendall(data)

    conn.close()




zleaf_command = ["run_zleaf", {"clientno": "{clientno}"}]
url_command = ["open_url", {"url": "https://www.google.com/search?q={keyword}&as_sitesearch={website}"}]
stream_command(url_command,hosts, machinespecs = specs_list)




myspecs
"Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])

"https://www.google.com/search?q={keyword}&as_sitesearch={website}".format(**myspecs[0])
#mycommand = ["run_zleaf", {"version":"3-6-7", "servermachine":"PWE00035", "fontsize" : 12, "clientno" : 31}]