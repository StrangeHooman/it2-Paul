from pathlib import Path
import json
import sys

jsonfileDir = str(Path(__file__).resolve()) + "students.json"

print(jsonfileDir)

data = {}

studentInfo = {"Name": None, "Grade": None, "Attendance" : None}

students = {}

def startup():
    try:
        with open(jsonfileDir, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {}

        with open(jsonfileDir, "w") as file:
            json.dump(data, file, indent=4)

def addStudent():
    None

def attendance():
    None

def exit():
    sys.exit()

def defaultFunc():
    print("Unknown command")

switcher = {
    "add student" : addStudent,
    "attendance" : attendance,
    "exit" : exit
}

def main():
    while True:
        command = input("Main> ")
        func = switcher.get(command, defaultFunc)

        func()

startup()
main()