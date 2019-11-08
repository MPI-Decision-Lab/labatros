"""Contains functions for subject computers
"""

import psutil
import subprocess
import webbrowser

def process_exists(name):
    """ Checks if a process with the name starts with the input string exists

    Args:
        name: Name of the process to be looked up

    Returns:
        True of False

    """
    process_list = []

    for proc in psutil.process_iter():
        process_list.append(proc.name())

    return (any(s.startswith(name) for s in process_list))


def run_zleaf(version, servermachine = False, fontsize=12, clientno=False):
    """ Runs z-Leaf with specific parameters. In order this function to work, z-Leafs has to be placed in
    c:\labclient\progs\zleaf\ and in each folder there should be version folders.

    Args:
        version: Folder name of the version to be run

        servermachine: The machine runs z-Tree

        fontsize: Font size of the z-Leaf

        clientno: Client number of the machine. If not provided, client number will be read from ./settings/.clientno.txt

    Returns:
        os.system output: 0 success
    """
    if not servermachine:
        print("No server machine specified")
        return 1
    if not clientno:
        clientno_file = 'C:\\labclient\\settings\\.clientno'
        with open(clientno_file, 'r') as clientno_filehandle:
            clientno = clientno_filehandle.read()

    zleaf_runcommand = 'C:\\labclient\\progs\\zleaf\\' + version + '\\zleaf.exe  /server ' + servermachine + ' /name C' + str(
        clientno) + ' /fontsize ' + str(fontsize)
    if process_exists('zleaf'):
        print("zLeaf is already running")
        return 1
    else:
        print(zleaf_runcommand)
        #os.system(zleaf_runcommand)
        pid = subprocess.Popen(zleaf_runcommand)
        return 0

    # TODO Add main() and sys.args for command line functionality


def kill_process(name, killall = False):

    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == name:
            proc.kill()
            print("killed " + name)
            if not killall:
                return 0

    if not killall:
        print("couldn't find any process as such")
        return 1


def kill_zleaf():
    kill_process("zleaf.exe")


def run_func(modulename,functionname,argumentdict):
#commented out code below because globals() wil not find functions when we call run_func from any other file than this
#    if modulename == '':
#        print(type(functionname))
#        output = globals()[functionname](**argumentdict)
#    elif modulename is not None:
#possible workarounds:
# - change the function that we want to call to a really global (like a built-in function), but this is probably not what we want (use the module builtin to do so)
# - put all functions that we want to use in one file and import it here
    output = getattr(__import__(modulename),functionname)(**argumentdict)
    return(output)

def enter_and_run_func():
    function_name = input("which function do you want to run? (format: module.function)\n")

    module, function = function_name.split(".")

    argument = input("please enter the argument for the function " + function +" from the module " + module +"\n")
    arguments = {'length':int(argument)}
    run_func(module,function,arguments)

	
	
def unpacker(datalist):
    print("unpacking")
    function_name = datalist[0]
    arguments = datalist[1]
    globals()[function_name](**arguments)
  
  
def print_hi(myname, times):
    print(myname + "hi " * times)

  
def print_hello(myname, times):
    print( myname + " hello " * times)

def open_url(url):
    webbrowser.open(url,1)

