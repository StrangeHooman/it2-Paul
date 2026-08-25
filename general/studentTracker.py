from pathlib import Path
import json
import sys

jsonfileDir = str(Path(__file__).resolve()) + "students.json"

print(jsonfileDir)

data = {}

studentInfo = {"Name": None, "Grade": None, "Attendance" : None}

students = {}

mainPath = "Main"
subPath = ""

def startup():
    try:
        with open(jsonfileDir, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {}

        with open(jsonfileDir, "w") as file:
            json.dump(data, file, indent=4)

def addStudent():
    subPath = "/addStudent"

def attendance():
    subPath = "/attendance"

def exit():
    sys.exit()

def defaultFunc():
    print("Unknown command")

def help():
    subPath = "/help"

    print("")

    for key in switcher.keys():
        print(f"{key:>20}")

    print("")
    

switcher = {
    "add student" : addStudent,
    "attendance" : attendance,
    "help" : help,
    "exit" : exit
}

def draw_input():
    return input(mainPath + subPath + "> ")


def main():
    subPath = ""    
    while True:
        command = draw_input()
        func = switcher.get(command, defaultFunc)

        func()

startup()
main()