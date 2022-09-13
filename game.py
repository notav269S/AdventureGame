import time
import os
import random
import colorama
from colorama import Fore, Back, Style

X = "idk"

def wait(dur):
    time.sleep(dur)


def clearConsole():
    os.system('clear')

def eat(arg):
    pass

def loading(msg, dur):
    for i in range(1, dur):
        clearConsole()
        print(f"{msg} |")
        wait(0.125)
        clearConsole()
        print(f"{msg} /")
        wait(0.125)
        clearConsole()
        print(f"{msg} -")
        wait(0.125)
        clearConsole()
        print(f"{msg} \\")
        wait(0.125)
        clearConsole()
        print(f"{msg} |")
        wait(0.125)
        clearConsole()
        print(f"{msg} /")
        wait(0.125)
        clearConsole()
        print(f"{msg} -")
        wait(0.125)
        clearConsole()
        print(f"{msg} \\")
        wait(0.125)
        clearConsole()

colorama.init()

