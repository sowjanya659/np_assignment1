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
			b = int(Y[1])-int(Y[2])
			b1=str(b)+"\n"
			server.send(b1.encode())
			print("result is ", str(b))
          
		elif Y[0] == "mul":
			d = int(Y[1])*int(Y[2])
			a1=str(d)+"\n"
			server.send(a1.encode())
			print("result is ", str(d))
          
		elif Y[0] == "div":
			e = int(Y[1])/int(Y[2])
			a1=str(e)+"\n"
			server.send(a1.encode())   
			print('result is %8.8g' %e)
           
		elif Y[0] == "fadd":
			fa = float(Y[1])+float(Y[2])
			a1=str(fa)+"\n"
			server.send(a1.encode())
			print('result is %8.8g' %fa)
          
		elif Y[0] == "fsub":
			fb = float(Y[1])-float(Y[2])
			a1=str(fb)+"\n"
			server.send(a1.encode())
			print('result is %8.8g'%fb)
            
		elif Y[0] == "fmul":
			fd = float(Y[1])*float(Y[2])
			a1=str(fd)+"\n"
			server.send(a1.encode())
			print('result is %8.8g' %fd)
            
		elif Y[0] == "fdiv":
			fe = float(Y[1])/float(Y[2])
			a1=str(fe)+"\n"
			server.send(a1.encode())
			print('result is %8.8g' %fe)


		response = server.recv(1024).decode()
		print (response)

	break

        
server.close
