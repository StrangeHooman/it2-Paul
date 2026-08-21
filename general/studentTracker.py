from pathlib import Path
import json

jsonfileDir = Path.cwd + "/../studentData.json"

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
            json.dump(data)

def main():
    while command != "exit":
        command = input("Main> ")
