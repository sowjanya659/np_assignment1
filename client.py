#!/usr/bin/python3

import socket		 	                      
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

from_user   = sys.argv[1]
split       = from_user.split(':')
host        = str(split[0])                           
port        = int(split[1])


s.connect((host, port))                           
                           
print("Connected to :",from_user)
initial_msg = s.recv(1024).decode()
print("\n", initial_msg)
s.send("OK\n".encode())

while(True):
	T=s.recv(1024).decode()
	print(T)
	Y=T.split()
	if len(Y) > 1:
		if Y[0] == "add":
			a = int(Y[1])+int(Y[2])
			a1=str(a)+"\n"
			s.send(a1.encode())
			print("result is ",str(a) )
           
		elif Y[0] == "sub":
			b = int(Y[1])-int(Y[2])
			b1=str(b)+"\n"
			s.send(b1.encode())
			print("result is ", str(b))
          
		elif Y[0] == "mul":
			d = int(Y[1])*int(Y[2])
			a1=str(d)+"\n"
			s.send(a1.encode())
			print("result is ", str(d))
          
		elif Y[0] == "div":
			e = int(Y[1])/int(Y[2])
			a1=str(e)+"\n"
			s.send(a1.encode())   
			print('result is %8.8g' %e)
           
		elif Y[0] == "fadd":
			fa = float(Y[1])+float(Y[2])
			a1=str(fa)+"\n"
			s.send(a1.encode())
			print('result is %8.8g' %fa)
          
		elif Y[0] == "fsub":
			fb = float(Y[1])-float(Y[2])
			a1=str(fb)+"\n"
			s.send(a1.encode())
			print('result is %8.8g'%fb)
            
		elif Y[0] == "fmul":
			fd = float(Y[1])*float(Y[2])
			a1=str(fd)+"\n"
			s.send(a1.encode())
			print('result is %8.8g' %fd)
            
		elif Y[0] == "fdiv":
			fe = float(Y[1])/float(Y[2])
			a1=str(fe)+"\n"
			s.send(a1.encode())
			print('result is %8.8g' %fe)
            
		resp = s.recv(1024).decode()
		print (resp)
	break

        
s.close
