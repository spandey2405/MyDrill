__author__ = 'spandey2405'
import test_helper
import argparse
import  sys
import xlsxwriter
import time
import datetime
import os
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H:%M:%S')
st = "Test_Detail/Test_Detail_"+st+".xlsx"

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(st)
worksheet = workbook.add_worksheet()

a = []
c = []
row = 1
col = 0
worksheet.set_column('B:B', 30)
worksheet.write(0, 0,     "Mote ID")
worksheet.write(0, 1, "IPv6")
worksheet.write(0, 2, "Ping Result")
parser = argparse.ArgumentParser()
parser.add_argument("-ip", help="Set Ip")
args = parser.parse_args()
if args.ip:
    BR = args.ip
else:
    print "No Valid Ip Given"
    sys.exit(0)

b = test_helper.get_data(BR,endpoint="/routes")

count = 0
checking = "y"
while (checking == "y"):
    count = 0
    for values_b in b:
        value_b = values_b.split('->')
        value_b = value_b[0]
        if value_b not in c:
            count = 1
            mote_name = raw_input("Mote_Name : %s : " % value_b )
            ping_test = test_helper.ping(value_b)
            worksheet.write(row, col,     mote_name)
            worksheet.write(row, col + 1, value_b)
            worksheet.write(row, col + 2, ping_test)
            row += 1
            mote_value = str(mote_name+"->"+value_b+"->"+ping_test)
            a.append(mote_value)
            c.append(value_b)
            os.system("clear")
            break
    b = test_helper.get_data(BR,endpoint="/routes")
    if count <1:
        print "No New Motes Are found :"

    checking = raw_input("Want To Test More Motes (y/n) >>")
    os.system("clear")


workbook.close()