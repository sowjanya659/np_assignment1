#!/usr/bin/python3

import socket		 	                      
import sys

#opens socket with ip4 version and type of protocol i.e, in this case its TCP.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

#splits the given ip address and port number. display the server information with ip , port no.
#also prints the initial message from the server.

usr_input = sys.argv[1]
split = usr_input.split(':')                                 
ip = str(split[0])                           
port_no = int(split[1])
server.connect((ip, port_no))                           
                           
print("Connected to server :",usr_input)                  
server_msg = server.recv(1024).decode()                      
print("\n", server_msg)                                      
server.send("OK\n".encode())

while(True):
	T=server.recv(1024).decode()
	print(T)
	Y=T.split()
	if len(Y) > 1:
		if Y[0] == "add":
			a = int(Y[1])+int(Y[2])
			a1=str(a)+"\n"
			server.send(a1.encode())
			print("result is ",str(a) )
           
		elif Y[0] == "sub":
			a = int(Y[1])-int(Y[2])
			a1=str(a)+"\n"
			server.send(a1.encode())
			print("result is ", str(a))
          
		elif Y[0] == "mul":
			a = int(Y[1])* int(Y[2])
			a1=str(a)+"\n"
			server.send(a1.encode())
			print("result is ", str(a))
          
		elif Y[0] == "div":
			a = int(Y[1])/int(Y[2])
			a1=str(a)+"\n"
			server.send(a1.encode())   
			print('result is %8.8g' %a)
           
		elif Y[0] == "fadd":
			fa = float(Y[1])+float(Y[2])
			a1=str(fa)+"\n"
			server.send(a1.encode())
			print('result is %8.8g' %fa)
          
		elif Y[0] == "fsub":
			fa = float(Y[1])-float(Y[2])
			a1=str(fa)+"\n"
			server.send(a1.encode())
			print('result is %8.8g'%fa)
            
		elif Y[0] == "fmul":
			fa = float(Y[1])*float(Y[2])
			a1=str(fa)+"\n"
			server.send(a1.encode())
			print('result is %8.8g' %fa)
            
		elif Y[0] == "fdiv":
			fa = float(Y[1])/float(Y[2])
			a1=str(fa)+"\n"
			server.send(a1.encode())
			print('result is %8.8g' %fa)


		response = server.recv(1024).decode()
		print (response)

	break

        
server.close
