__author__ = 'saurabh'

import csv
fieldnames = ['id', 'title', 'filename', 'status', 'fbid']
with open('mikudb.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

