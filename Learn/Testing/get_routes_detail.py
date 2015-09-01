__author__ = 'spandey2405'
import helper
import argparse
import os,sys
parser = argparse.ArgumentParser()
parser.add_argument("-ipv6", help="Set Ip")
parser.add_argument("-endpoint", help="Set Ip")
parser.add_argument("-ipv4")

args = parser.parse_args()

if args.ipv4:
    BR = args.ip
elif args.ipv6:
    BR = "["+args.ipv6+"]"

else:
    print "No Valid Ip Given"
    BR = "NULL"

if args.endpoint:
    ENDPOINT = args.endpoint
else:
    ENDPOINT = "/routes"

choice = True
os.system("clear")
print "1. Get IPv6 From Mote Name\n2. Get Mote Name From IPV6\n3. Get All Motes Detail From Routes\n5. Draw Graph\n5. Exit\n\n"

class Detail():


    def Get(self):
        choice = int(raw_input(">>\t"))
        if choice == 1:
            os.system("clear")
            self.get_ipv6_from_mote_name()

        elif choice == 2:
            os.system("clear")
            self.get_motename_from_ipv6()

        elif choice == 3:
            os.system("clear")
            self.get_all_motes_detail()

        elif choice == 4:
            os.system("clear")
            self.draw_a_graph()

        elif choice == 5:
            exit()

        else:
            os.system("clear")
            print "false choice"
        self.detail_continue()

    def get_ipv6_from_mote_name(self):
        mote_name = raw_input("Enter Mote Name >>\t")
        IPv6 = helper.get_ipv(mote_name)
        if IPv6 == "NULL":
            print "Mote Not Found In Database"
        else:
            print IPv6

    def get_motename_from_ipv6(self):
        mote_ipv6 = raw_input("Enter Mote ipv6 >>\t")
        Name = helper.get_mote(mote_ipv6)
        if Name == "NULL":
            print "Mote Not Found In Database"
        else:
            print Name

    def get_all_motes_detail(self):
        global BR
        if BR == "NULL":
            BR = raw_input("Enter BR Ip Address >>\t")
        helper.get_motes_from_routes(BR,ENDPOINT)

    def detail_continue(self):
        choice = raw_input("\n\nDo You Wish To Continue (Press c to continue , Press Any Other Key To Exit)")
        os.system("clear")
        print "1. Get IPv6 From Mote Name\n2. Get Mote Name From IPV6\n3. Get All Motes Detail From Routes\n5. Draw Graph\n5. Exit\n\n"
        if choice == "y" or "Y":
            self.Get()
        else:
            self.exit_system()

    def exit_system(self):
        sys.exit(0)

    def draw_a_graph(self):
        global BR
        if BR == "NULL":
            BR = raw_input("Enter BR Ip Address >>\t")
        helper.draw_graph(BR,ENDPOINT)


def init():
    a = Detail()
    a.Get()

if __name__ == '__main__':
    init()