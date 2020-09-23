
############## Users added in zabbix with the required mail(users media) domains ###########

###in this example I am retriving for @gmail.com############


f0rom pyzabbix import ZabbixAPI
import re
import sys,logging
import json
import  csv

zapi = ZabbixAPI("http://ip/zabbix")
zapi.login("user", "password")
zapi.timeout = 300
'''
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)

log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logging.DEBUG)
'''
print("Connected to Zabbix API Version %s" % zapi.api_version())

users = zapi.user.get(output=['userid','alias'])

for u in users: 
	usermedia = zapi.usermedia.get(userids=u['userid'],output=['sendto','active'])
	for i in usermedia:
		if re.search ('.*\@gmail.com',i['sendto']): #regex search performing Email domain check
			print ()
			print ("Email :",i['sendto']," ---- ZabbixUser:",u['alias'])
			
