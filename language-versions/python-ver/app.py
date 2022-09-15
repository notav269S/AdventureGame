import random
import colorama
from colorama import Fore, Back, Style
import os

colorama.init()

data = {
    "far_land_town": {
        "places": {
            "curPos": None,
        }
    },
    "forests": {

    },
    "emperial_city": {

    }
}

def prompt(args=''):
    inp = input(f"{Fore.YELLOW + args}>{Fore.LIGHTBLUE_EX}{Style.BRIGHT} ")
    return inp

def log(text):
    print(f"{Fore.LIGHTGREEN_EX}{text}")

os.system('clear')

log('Welcome To Far Land Town Located at the Very North of Your Map. For a Guide on How to Play Enter "help" as the Command When The Prompt Shows Up.')

while True:
    command = prompt()