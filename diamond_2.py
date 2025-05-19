from os import system as c
import time
import random
import os

#------------- COLOURS -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
██████╗ ██╗██████╗ ███████╗ █████╗ 
██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║██████╔╝█████╗  ███████║
██╔═══╝ ██║██╔═══╝ ██╔══╝  ██╔══██║
██║     ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
{Y} HACKING WORLD - DIAMOND HACK TOOL
{A}-------------------------------------------------
""")

#------------- LOADING ANIMATION -------------#
def loading(msg):
    for i in range(3):
        print(f"{C}{msg}{'.'*i}")
        time.sleep(0.7)
        c('clear')
        logo()

#------------- DIAMOND HACK FUNCTION -------------#
def diamond_hack():
    logo()
    uid = input(f"{C}[+] Enter Your Free Fire UID: ")
    loading("Connecting to Garena Server")
    print(f"{G}[✓] UID Verified: {uid}")
    time.sleep(1)

    loading("Selecting Diamond Package")
    diamonds = [500, 1000, 3000, 5000]
    for d in diamonds:
        print(f"{Y}[*] Injecting {d} Diamonds...")
        time.sleep(1.2)
    
    loading("Finalizing Transaction")

    for percent in range(0, 101, 10):
        print(f"{C}[*] Inject Progress: {percent}%")
        time.sleep(0.3)
        c('clear')
        logo()

    print(f"{G}[✓] Successfully Injected 10000 Diamonds to UID: {uid}!")
    time.sleep(1)
    print(f"{P}[*] Restart your game to see updated diamonds.")
    input(f"\n{G}And wait 10-12 minit...")

#------------- START TOOL -------------#
diamond_hack()