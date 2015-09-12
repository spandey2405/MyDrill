__author__ = 'saurabh'

import csv
import time
fieldnames = ['id', 'title', 'filename', 'status', 'fbid']
def write_data(data):

    with open('mikudb.csv', 'a') as csvfile:
        fieldnames = ['id', 'title', 'filename', 'status', 'fbid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)


def get_data():
    with open('mikudb.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print row

time = int(time.time())
# write_data({'title': 'Checking A File', 'filename':"filexyz.png", "status":1, "fbid":"11211121_4564789"})
# get_data()