#!/usr/bin/python3

import socket		 	            
import sys
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

from_user  = sys.argv[1]
split      = from_user.split(':')	  		    
host       = str(split[0])                     
port       = int(split[1])

s.bind((host, port)) 			    
s.listen(1)

print("Server is active")

A = ["add", "sub", "mul", "div", "fadd", "fsub", "fdiv", "fmul"]

while True:
	c, addr = s.accept() 		    
	print("Connected to :",from_user)
	c.send("TEXT TCP 1.0\n".encode())
	return_msg = c.recv(1024).decode()
	print(return_msg)


	while True:
		X= random.choice(A)
		if X == "add":
			r1 = random.randint(1,100)
			r2 = random.randint(1,150)
			L = X + " " + str(r1) + " " + str(r2)
			addition = r1 + r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ("result is", addition)
			if addition == int(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "sub":
			r1 = random.randint(1,100)
			r2 = random.randint(1,75)
			L = X + " " + str(r1) + " " + str(r2)
			subtraction = r1 - r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ("result is", subtraction)
			if subtraction == int(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "mul":
			r1 = random.randint(1,1000)
			r2 = random.randint(1,1500)
			L = X + " " + str(r1) + " " + str(r2)
			multiplication = r1 * r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ("result is", multiplication)
			if multiplication == int(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "div":
			r1 = random.randint(1,100)
			r2 = random.randint(1,150)
			L = X + " " + str(r1) + " " + str(r2)
			division = r1 / r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ('result is %8.8g' %division)
			if division == float(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "fadd":
			r1 = random.uniform(1,100)
			r2 = random.uniform(1,150)
			L = X + " " + str(r1) + " " + str(r2)
			faddition = r1 + r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ('result is %8.8g' %faddition)
			if faddition == float(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "fsub":
			r1 = random.uniform(1,100)
			r2 = random.uniform(1,75)
			L = X + " " + str(r1) + " " + str(r2)
			fsubtraction = r1 - r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ('result is %8.8g' %fsubtraction)
			if fsubtraction == float(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "fmul":
			r1 = random.uniform(1,100)
			r2 = random.uniform(1,150)
			L = X + " " + str(r1) + " " + str(r2)
			fmultiplication = r1 * r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ('result is %8.8g' %fmultiplication)
			if fmultiplication == float(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

		elif X == "fdiv":
			r1 = random.uniform(1,100)
			r2 = random.uniform(1,150)
			L = X + " " + str(r1) + " " + str(r2)
			fdivision = r1 / r2
			c.send(L.encode())
			answer=c.recv(1024).decode()
			print ('result is %8.8g' %fdivision)
			if fdivision == float(answer):
				c.send("OK\n".encode())
				
			else:
				c.send("ERROR\n".encode())

			

		else:
                   print ("Wrong input bye bye")
		break


c.close()  

