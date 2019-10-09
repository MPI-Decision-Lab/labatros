#!/usr/bin/env python3

import socket
import pickle

hosts = ['127.0.0.1']
port = 65432



mycommand = ["run_zleaf", {"version":"3-6-7", "servermachine":"PWE00035", "fontsize" : 12, "clientno" : 31}]

def stream_command(command, machines):
    """
    machines: list of machines
    """
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for mach in machines:
        conn.connect((mach, port))
        data_to_send = command
        data = pickle.dumps(data_to_send)
        conn.sendall(data)
    conn.close()