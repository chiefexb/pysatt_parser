#!/usr/bin/python
#coding: utf8
from lxml import etree
import sys
import pycurl
wr_buf = ''
def write_data( buf ):
	global wr_buf
	wr_buf += buf

def main():
    c = pycurl.Curl()
    c.setopt( pycurl.URL, 'http://skynet-local.net:8099/frql?q=check_pin&pin_code="0000"++status' )
    c.setopt( pycurl.WRITEFUNCTION, write_data )
    c.perform()
    c.close()
    #f=open('new_1.xml')
    #print "OUT",wr_buf
    root=etree.fromstring( wr_buf)
    #root=xml.getroot()	
    rez=root.findall('results')
    str=rez[1].find('streaming')
    svc=str.find('svc')
    evt=svc.find('evt')
    name=evt.find('name').text
    print  name
if __name__ == "__main__":
    main()
