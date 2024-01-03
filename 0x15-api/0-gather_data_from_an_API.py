#!/usr/bin/python3
"""returns to-do list info of an employeeID"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)
    argv_two = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f'{url}/users/{argv_two}').json()
    todos = requests.get(f'{url}/todos?userId={argv_two}').json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for i in completed:
        print("\t {}".format(i))
