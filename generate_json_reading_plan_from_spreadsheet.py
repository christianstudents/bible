import csv
import requests

"""
This file is intended to read a csv file of Date (i.e. 7/21/21)
and Verses (i.e. John 1) and call the LSM API to generate a 
json file of the verses requested.
"""

json_string = ""

with open('reading_plan/Sample_Bible_Reading_Program.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
    	if not (row[0]=="Date" or row[1] =="Verses"):
    		json_string += requests.get("https://api.lsm.org/recver.php?String=" + row[1] + "&Out=json").text
    		line_count += 1
    print(json_string)
    print(f'Processed {line_count} lines.')