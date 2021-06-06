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
		X = random.choice(V)
		if X == "add":
			x1 = random.randint(1,1000)
			x2 = random.randint(1,1500)
			E = X + " " + str(x1) + " " + str(x2)
			addition = x1 + x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ("result is", addition)
			if addition == int(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "sub":
			x1 = random.randint(1,1500)
			x2 = random.randint(1,1000)
			E = X + " " + str(x1) + " " + str(x2)
			subtraction = x1 - x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ("result is", subtraction)
			if subtraction == int(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "mul":
			x1 = random.randint(1,1000)
			x2 = random.randint(1,1500)
			E = X + " " + str(x1) + " " + str(x2)
			multiplication = x1 * x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ("result is", multiplication)
			if multiplication == int(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "div":
			x1 = random.randint(1,1000)
			x2 = random.randint(1,1500)
			E = X + " " + str(x1) + " " + str(x2)
			division = x1 / x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %division)
			if division == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fadd":
			x1 = random.uniform(1,1000)
			x2 = random.uniform(1,1500)
			E = X + " " + str(x1) + " " + str(x2)
			faddition = x1 + x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %faddition)
			if faddition == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fsub":
			x1 = random.uniform(1,1500)
			x2 = random.uniform(1,1000)
			E = X + " " + str(x1) + " " + str(x2)
			fsubtraction = x1 - x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %fsubtraction)
			if fsubtraction == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fmul":
			x1 = random.uniform(1,1000)
			x2 = random.uniform(1,1500)
			E = X + " " + str(x1) + " " + str(x2)
			fmultiplication = x1 * x2
			client.send(E.encode())
			answer=client.recv(1024).decode()
			print ('result is %8.8g' %fmultiplication)
			if fmultiplication == float(answer):
				client.send("OK\n".encode())
				
			else:
				client.send("ERROR\n".encode())

		elif X == "fdiv":
			x1 = random.uniform(1,1000)
			x2 = random.uniform(1,1500)
			E = X + " " + str(x1) + " " + str(x2)
			fdivision = x1 / x2
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
