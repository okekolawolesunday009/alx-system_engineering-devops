#!/usr/bin/python3
"""returns to-do list info of an employeeID"""
from sys import argv
import requests
import json

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)
    argv_two = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    try:
        user = requests.get(f'{url}/users/{argv_two}').json()
        todos = requests.get(f'{url}/todos?userId={argv_two}').json()
        json_data = {str(argv_two): [
            {"task": task["title"],
                "completed": task['completed'], "username": user['username']}
            for task in todos]}

        json_file_path = f"{argv_two}.json"
        with open(json_file_path, "w") as jsonfile:
            json.dump(json_data, jsonfile)
        print(f'Data exported to {json_file_path} successfully.')
    except requests.exceptions.RequestException as e:
        print(f"Error fetched data: {e}")
        exit(1)
