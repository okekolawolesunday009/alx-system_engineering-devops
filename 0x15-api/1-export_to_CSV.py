"""returns to-do list info of an employeeID"""
from sys import argv
import requests
import csv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)
    argv_two = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    try:
        user = requests.get(f'{url}/users/{argv_two}').json()
        todos = requests.get(f'{url}/todos?userId={argv_two}').json()

        csv_file_path = f"{argv_two}.csv"
        with open(csv_file_path, "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                csv_row = [
                    argv_two,
                    user['username'],
                    str(task['completed']),
                    task['title']
                ]
                csv_writer.writerow(csv_row)

        print(f"Data exported {csv_file_path} successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
