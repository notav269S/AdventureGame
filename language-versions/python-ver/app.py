import random
import colorama
from colorama import Fore, Back, Style
import os
import json

colorama.init()

dataTemp = {
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

save = {}

def prompt(args=''):
    inp = input(f"{Fore.YELLOW + args}>{Fore.LIGHTBLUE_EX}{Style.BRIGHT} ")
    return inp

def log(text):
    print(f"{Fore.LIGHTGREEN_EX}{text}")

os.system('clear')

log('Welcome To Far Land Town Located at the Very North of Your Map. For a Guide on How to Play Enter "help" as the Command When The Prompt Shows Up.')

while True:
    command = prompt().lower()
    if command.split(' ')[0] == "save":
        args = command.split(' ')[1]
        try:
            with open(f'/saves/{args}.json', 'r') as f:
                log("Loaded Save")
                save = json.dump(f)

        except FileNotFoundError:
            log("Save Not Found")