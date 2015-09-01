__author__ = 'spandey2405'


import test_helper
import helper

def get_motes_detail(BR):

    b = test_helper.get_data(BR)
    c= []
    for values_b in b:
        value_b = values_b.split('->')
        value_b = value_b[0]
        if value_b not in c:
            c.append(value_b)

    for mote in c:
        mote_ipv6 = mote
        print "Mote Name : %s\tMote IPv6 : %s" % (helper.get_mote(mote_ipv6),mote_ipv6)
