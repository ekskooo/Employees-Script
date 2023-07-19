import csv
import sys

csv_file_path = 'employees.csv'
sorted_csv_file_path = 'sorted_employees.csv'


def calculate_average_age():
    ages = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            age = int(row[1])
            ages.append(age)

    if len(ages) > 0:
        average_age = sum(ages) / len(ages)
        print(f"Average age of employees is: {average_age}")
    else:
        print("No employee data found")


def highest_salary():
    highest = 0
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if highest < int(row[2]):
                highest = int(row[2])
    print(f"Highest salary is {highest}")


def lowest_salary():
    lowest = float('inf')
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if lowest > int(row[2]):
                lowest = int(row[2])
    print(f"Lowest salary is {lowest}")


def alphabet_order():
    employees = []
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            employees.append(row)

    sorted_employees = sorted(employees[1:], key=lambda emp: emp[0])

    with open(sorted_csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(employees[:1] + sorted_employees)

    print(f"Sorted CSV file '{sorted_csv_file_path}' created successfully")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "High_salary":
            highest_salary()
        elif sys.argv[1] == "Average_age":
            calculate_average_age()
        elif sys.argv[1] == "Sort_names":
            alphabet_order()
        elif sys.argv[1] == "Low_salary":
            lowest_salary()
        else:
            print("Pass valid argument.")
    else:
        print("Pass exactly 1 argument.")














