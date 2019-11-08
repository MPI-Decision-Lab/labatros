#SERVERMACHINES = [{"name": "Control Pc", "address": "PWE00034"}, {"name": "Lab Manager PC", "address": "PWE00035"}]
SERVERMACHINES = [["Control Pc", "PWE00034"], ["Lab Manager PC", "PWE00035"]]

clientno_file = r'C:\labclient\.clientno.txt'

default_servermachine = 1
current_servermachine = SERVERMACHINES[1]
