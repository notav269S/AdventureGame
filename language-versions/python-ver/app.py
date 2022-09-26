import random
import colorama
from colorama import Fore, Back, Style
import os
import time
import json
import pathlib

curPath = pathlib.Path().resolve()

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
    if command.split(' ')[0] == "load":
        args = command.split(' ')[1]
        try:
            with open(f'{curPath}/language-versions/python-ver/{args}.json', 'r') as f:
                log("Loaded Save")
                save = json.dump(f)
        except FileNotFoundError:
            log("Save Not Found")
    elif command.split(' ')[0] == 'help':
        log("The command prompt involves two words. One, the command(eg. look,overview etc.) and two, the arguments of the word which changes based on the command. If the arguments have more than one word, it is split with an underscore.The game is coded such that you don't have to type a command and be prompted next for the argument, instead it is mixed into a single prompt. Some commands are situation based but they do have a separate message when entered in the wrong circumstance. Commands Include:")


