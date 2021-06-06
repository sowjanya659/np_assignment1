#!/usr/bin/python3

import socket		 	            
import sys
import random

#opens socket with ip4 version and type of protocol i.e, in this case its TCP.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#splits the given ip address and port number. display the server state.

usr_input = sys.argv[1]
split = usr_input.split(':')	  		    
ip = str(split[0])                     
port_no = int(split[1])

server.bind((ip, port_no)) 			    
server.listen(1)

print("Server is listening")

V = ["add", "sub", "mul", "div", "fadd", "fsub", "fmul", "fdiv"]

#diplay the client information and send initial msg about the protocol type and version.
#choose the operation, values randomly from the given range and executes according to the operation.

while True:
	client, addr = server.accept() 		    
	print("Connected to client :",usr_input)
	client.send("TEXT TCP 1.0\n".encode())
	client_msg = client.recv(1024).decode()
	print(client_msg)


	while True:
		X = input("choose one of the operation (add, sub, mul, div, fadd, fsub, fmul, fdiv): ")
		if X == "add":
			r1 = random.randint(1,1000)
			r2 = random.randint(1,1500)
			E = X + " " + str(r1) + " " + str(r2)
			addition = r1 + r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ("result is", addition)
			if addition == int(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "sub":
			r1 = random.randint(1,1500)
			r2 = random.randint(1,1000)
			E = X + " " + str(r1) + " " + str(r2)
			subtraction = r1 - r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ("result is", subtraction)
			if subtraction == int(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "mul":
			r1 = random.randint(1,1000)
			r2 = random.randint(1,1500)
			E = X + " " + str(r1) + " " + str(r2)
			multiplication = r1 * r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ("result is", multiplication)
			if multiplication == int(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "div":
			r1 = random.randint(1,1000)
			r2 = random.randint(1,1500)
			E = X + " " + str(r1) + " " + str(r2)
			division = r1 / r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %division)
			if division == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fadd":
			r1 = random.uniform(1,1000)
			r2 = random.uniform(1,1500)
			E = X + " " + str(r1) + " " + str(r2)
			faddition = r1 + r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %faddition)
			if faddition == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fsub":
			r1 = random.uniform(1,1500)
			r2 = random.uniform(1,1000)
			E = X + " " + str(r1) + " " + str(r2)
			fsubtraction = r1 - r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %fsubtraction)
			if fsubtraction == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fmul":
			r1 = random.uniform(1,1000)
			r2 = random.uniform(1,1500)
			E = X + " " + str(r1) + " " + str(r2)
			fmultiplication = r1 * r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %fmultiplication)
			if fmultiplication == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fdiv":
			r1 = random.uniform(1,1000)
			r2 = random.uniform(1,1500)
			E = X + " " + str(r1) + " " + str(r2)
			fdivision = r1 / r2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %fdivision)
			if fdivision == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

			

		else:
                   print ("wrong option: select the proper operation from the list ")
		break


client.close()  
