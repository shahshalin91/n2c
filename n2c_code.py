import json
import xmltodict
import os
import pyeapi							#import arista eapi module
from pycsco.nxos.device import Device   #import cisco nexus module

pyeapi.load_config("~/.pyeapi.conf")	#load config ---- saved in config file (contains host name,ipaddr,password,mode)

eos1 = pyeapi.connect_to("eos-spine1")	#connect to eos-spine1 device
eos2 = pyeapi.connect_to("eos-spine2")  #connect to eos-spine2 device


i = 0			
eos1_lldp = (eos1.enable("show lldp neighbors",encoding="json"))	#command to find neighboring devices of arista devices
eos2_lldp = (eos2.enable("show lldp neighbors",encoding="json"))	#command to find neighboring devices of arista devices

list_size1 = len(eos1_lldp[0].values()[0].values()[4])				#gives the number of neighbor for eos1
list_size2 = len(eos1_lldp[0].values()[0].values()[4])				#gives the number of neighbor for eos2

csco1 = Device(ip="85.190.182.51",username="ntc",password="ntc123")	#loading cisco nexus device1 with ip,username, password
csco2 = Device(ip="31.220.70.5",username="ntc",password="ntc123")	#loading cisco nexus device2 with ip,username, password

get_sh_lldp1 = csco1.show('show lldp neighbors')					# lists the lldp neighbors for cisco device
get_sh_lldp2 = csco2.show('show lldp neighbors')					# lists the lldp neighbors for cisco device

sh_lldp_dict1 = xmltodict.parse(get_sh_lldp1[1])					
sh_lldp_dict2 = xmltodict.parse(get_sh_lldp2[1])					

count_cisco_neighbor_1 = len(sh_lldp_dict1['ins_api']['outputs']['output']['body']['TABLE_nbor']['ROW_nbor'])		#find the count of cisco neighbors for iteration
simple1 = sh_lldp_dict1['ins_api']['outputs']['output']['body']['TABLE_nbor']['ROW_nbor']							#finding the neighbors from the output
count_cisco_neighbor_2 = len(sh_lldp_dict2['ins_api']['outputs']['output']['body']['TABLE_nbor']['ROW_nbor'])		#find the count of cisco neighbors for iteration
simple2 = sh_lldp_dict2['ins_api']['outputs']['output']['body']['TABLE_nbor']['ROW_nbor']							#finding the neighbors from the output

'''parsing to JSON FORMAT'''

d = { "nxos-spine1":[{'neighbor_interface':(simple1[i].values()[2]) , "local_interface":(simple1[i].values()[6]) , "neighbor": (simple1[i].values()[1]) } for i in (xrange(count_cisco_neighbor_1))],
"nxos-spine2":[{'neighbor_interface':(simple2[i].values()[2]) , "local_interface":(simple2[i].values()[6]) , "neighbor": (simple2[i].values()[1]) } for i in (xrange(count_cisco_neighbor_2))],
"eos-spine1":[{'neighbor_interface':(eos1_lldp[0].values()[1].values()[4][i].values()[1]) , "local_interface":(eos1_lldp[0].values()[1].values()[4][i].values()[2]) , "neighbor": (eos1_lldp[0].values()[1].values()[4][i].values()[0]) } for i in (xrange(list_size1))],
"eos-spine2":[{'neighbor_interface':(eos2_lldp[0].values()[1].values()[4][i].values()[1]) , "local_interface":(eos2_lldp[0].values()[1].values()[4][i].values()[2]) , "neighbor": (eos2_lldp[0].values()[1].values()[4][i].values()[0]) } for i in (xrange(list_size2))]}

j = json.dumps(d, indent=4)
f = open("n2c_output.json","wb+")
print >> f,j
f.close()
