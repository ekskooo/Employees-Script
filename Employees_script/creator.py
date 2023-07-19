import csv

# Define the data to be written to the CSV file
data = [
    ['Name', 'Age', 'Salary'],
    ['John Doe', 30, 5000],
    ['Jane Smith', 35, 6000],
    ['Alex Johnson', 28, 4500],
    ['Emily Brown', 32, 5500]
]

# Specify the file path and name for the CSV file
csv_file_path = 'employees.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")

