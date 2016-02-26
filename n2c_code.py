import json
from pycsco.nxos.device import Device as CISCO
from pyeapi import connect_to as ARISTA

def get_arista_neighbors(device):
    output = device.enable('show lldp neighbors')
    KEY_MAP = dict(neighborDevice='neighbor', neighborPort='neighbor_interface', port='local_interface')
    device_neighbors = output[0]['result']['lldpNeighbors']
    neighbors_list = []
    for neighbor in device_neighbors:
        temp = {}
        for vendor_key, vendor_value in neighbor.iteritems():
            normalized_key = KEY_MAP.get(vendor_key)
            if normalized_key:
                temp[normalized_key] = str(vendor_value)
        neighbors_list.append(temp)
    return neighbors_list

def get_cisco_neighbors(device):
    cisco_dev = device.show('show lldp neighbors')
    output = xmltodict.parse(cisco_dev[1])
    KEY_MAP = dict(neighborDevice='chassis_id', neighborPort='port_id', port='l_port_id')
    device_neighbors = output['ins_api']['outputs']['output']['body']['TABLE_nbor']['ROW_nbor']
    neighbors_list = []
    for neighbor in device_neighbors:
        temp = {}
        for vendor_key, vendor_value in neighbor.iteritems():
            normalized_key = KEY_MAP.get(vendor_key)
            if normalized_key:
                temp[normalized_key] = str(vendor_value)
        neighbors_list.append(temp)
    return neighbors_list

def load_cisco_devices():

#CREATE a file having 4 parameters  devicename,ip,username,password per line  separated by comma Eg nxos-spine1,85.190.182.51,ntc,ntc123

    read_cisco = open("cisco_nxos_dev.txt","rb+")
    file_lines = read_cisco.readlines()
    cisco_devices = []
    cisco_details = []
    for line in (file_lines):
        cisco_details = line.split(",")
        cisco_devices.append(cisco_details[0])
        CISCO(ip=str(cisco_details[1]),username=str(cisco_details[2]),password=str(cisco_details[3].rstrip("\n")))
    return cisco_devices

def load_arista_devices():

#loads the devices from the config file

    read_arista = open(".pyeapi.conf","rb+")
    file_lines = read_arista.readlines()
    arista_devices = []
    for line in file_lines:
        if line.startswith("[connection"):
            node = line.split(":")
            arista_devices.append(node[1].rstrip("]\n"))
    read_arista.close()
	
    return arista_devices

	
def main():
    neighbors = {}
    cisco_devices = load_cisco_devices()
    arista_devices = load_arista_devices()
    for dev in arista_devices:
        node = ARISTA(dev)
        neighbors[dev] = get_arista_neighbors(node)
    for dev in cisco_devices:
        neighbors[dev] = get_arista_neighbors(node)
    print json.dumps(neighbors, indent=4)
if __name__ =="__main__":
    main()
