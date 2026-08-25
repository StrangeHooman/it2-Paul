from pathlib import Path
import json
import sys

jsonfileDir = str(Path(__file__).resolve()) + "students.json"

print(jsonfileDir)

data = {}

students = []

studentInfo = {"Name": None, "Grade": None, "Attendance" : None}

students = {}

mainPath = ["Main"]
subPath = [""]

def draw_input(msg = ""):
    return input(mainPath[0] + subPath[0] + "> " + msg)

def readJSON():
    with open(jsonfileDir, "r") as file:
        data = json.load(file)

def writeJSON(data):
    with open(jsonfileDir, "w") as file:
        json.dump(data, file, indent=4)

def startup():
    try:
        readJSON()

    except FileNotFoundError:
        data = {}

        writeJSON

def addStudent():
    subPath[0] = "/addStudent"

    name = draw_input("Student name: ")

    data = {""}



def attendance():
    subPath[0] = "/attendance"

def exit():
    sys.exit()

def defaultFunc():
    print("Unknown command")

def help():
    subPath[0] = "/help"

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

def main():
    subPath[0] = ""    
    while True:
        command = draw_input()
        func = switcher.get(command, defaultFunc)

        func()

startup()
main()