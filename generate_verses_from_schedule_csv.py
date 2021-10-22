import csv
# Importing BeautifulSoup class from the bs4 module
# need to run "pip install beautifulsoup" and "pip install lxml"

from bs4 import BeautifulSoup
import fnmatch
import os
from string import digits
import re
import json

"""
This file is intended to read a csv file of Date (i.e. 7/21/21)
and Verses (i.e. John 1) and grab the necessary html text 
from the Bible and return the verses required. 
Output will be json file with keys containing the date and values containing the verses for that date.
"""

#Check if a string has numbers
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

#this is the folder which contains the Bible html files
src = 'bible'

"""
The following code creates a dictionary containing book to html file name i.e. "{john: 43-john.html, etc.}"
"""
books_of_the_bible = {}
html_files_of_bible = []

for root, dirnames, filenames in os.walk(src):
	html_files_of_bible = filenames

for each_file in html_files_of_bible:
	book = each_file.split("-")[1]
	if hasNumbers(book):
		book = book[0] + " " + book[1:(len(book))].replace('.html','')
	else:
		book = book[0:(len(book))].replace('.html','')
	books_of_the_bible[book] = each_file

#print(books_of_the_bible)

"""
Here we grab the verses for each day's reading.
"""
reading_plan = {}


counter = 0
first_date = ""
last_date = ""

with open('reading_plan/Sample_Bible_Reading_Program.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
    	if not (row[0]=="Date" or row[1] =="Verses"):
    		if counter == 0:
    			first_date = row[0]
    		last_date = row[0]
    		book = row[1].lower().rstrip(digits).rstrip(" ")
    		m = re.findall(r"\d+\s*$", row[1]); chapter = m[0] if m else 1
    		html_file = books_of_the_bible[book]
    		#print("html file we want to grab from: " + html_file)
    		#print("book is: " + book)
    		#print("chapter is: " + str(chapter))

    		with open(src + "/" + html_file) as fp:
    			soup = BeautifulSoup(fp, 'html.parser')
    			div = soup.findAll("div", {"class": "bible-text"})	
    		reading_plan[row[0]] = div[int(chapter) - 1]
    		counter += 1

"""
Write the reading plan of dictionary {Date: html of verses, 
date: html of verses, etc.} to txt file.
"""

#output_file = "reading_plan" + first_date + "-" + last_date + ".txt"
#f = open(output_file, "a")
#filename = "reading_plan.txt"
#output_file = "reading_plan.csv"
#f = open(filename, "a")
#f.write(str(reading_plan))
#f.close()

with open('reading_plan.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	for key, value in reading_plan.items():
		writer.writerow([key, value])
