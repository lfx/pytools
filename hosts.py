#!/usr/bin/env python
import commands

def hosts():
	for i in range (1,254):
		x = commands.getoutput('host 192.168.0.'+str(i)).split(' ')[-1]
		if x != '3(NXDOMAIN)':
				print i,x

if __name__ == '__main__':
	hosts()  
