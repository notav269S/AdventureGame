import random
import colorama
from colorama import Fore, Back, Style
import os
import json
import pathlib

colorama.init()

directory = pathlib.Path(__file__).parent.resolve()

dataTemp = {
    "far_land_town": {
        "town_square": {
            "curPos": False,
            "explored": False,
            "desc": "A Fountain lies in front of you. Some people walk around the green environment with snowy mountains visible accross the horizon. A sign stands before you and a poster is on your right."
        },
        "busy_street": {
            "curPos": False,
            "explored": False,
            "desc": "The street you are looking at is packed with people, traders and high ranked workers. A sign is in front of you with a man in black staring at you.",
            "interactables": ["sign", "man_in_black", ""]
        }
    }
}

saveData = {}

def prompt(args=''):
    inp = input(f"{Fore.YELLOW + args}>{Fore.LIGHTBLUE_EX}{Style.BRIGHT} ")
    return inp

def log(text):
    print(f"{Fore.LIGHTGREEN_EX}{text}")

os.system('clear')

log('Welcome To Far Land Town Located at the Very North of Your Map. For a Guide on How to Play Enter "help" as the Command When The Prompt Shows Up.')

while True:
    command = prompt().lower()
    if command.split(' ')[0] == "load":
        try:
            args = command.split(' ')[1]
        except:
            print("You haven't put a save name, enter the save name to load it")
        try:
            with open(f'{directory}/saves/{args}.json', 'r') as f:
                log("Loaded Save")
                saveData = f.read()
        except FileNotFoundError:
            log("Save Not Found")
    elif command.split(' ')[0] == 'look':
        try:
            args = command.split(' ')[1]
        except:
            pass
        