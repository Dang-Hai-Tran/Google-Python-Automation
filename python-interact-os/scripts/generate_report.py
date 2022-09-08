#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
	with open(csv_file_location, newline='') as csv_file:
		employee_file = csv.DictReader(csv_file)
		for employee in employee_file:
			print(employee)

file_location = "../data/employees.csv"
read_employees(file_location)
