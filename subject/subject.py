# first of all import the socket library 
import socket  
import pickle              
import os
import psutil
from subject_funs import *
# next create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
print("Socket successfully created")

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
       


#available_commands = {300:"print_hi", 301:"print_hello"}

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind((HOST, PORT))         
print("socket binded to %s" %(PORT))
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")        
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print('Got connection from', addr)
   
   #c.send(pickle.dumps("list of available functions:"))
   #c.send(pickle.dumps(available_commands))
   # send a thank you message to the client.  
   
   data = c.recv(1024)
   received_data = pickle.loads(data)
   print(received_data)
   unpacker(received_data)
   
   #if message in available_commands: 
   #   locals()[message](n)
   #   c.send(pickle.dumps('Status 0'))   
   #else:
  #    c.send(pickle.dumps(HOST + '- didnt understand what you want. sorry'))   
  #    print("somebody asked me something that i dont understand")
   # Close the connection with the client 
   c.close() 
