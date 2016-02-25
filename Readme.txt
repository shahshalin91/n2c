The Repository consists of python code and its output for  the following coding excercise

Question:

Use NX-API on the Cisco devices and eAPI on the Arista devices.
In terms of libraries, you'll want to use pycsco and pyeapi,
 for Cisco and Arista, respectively.  pycsco and pyeapi both
 have GitHub pages, so you can learn how to use their libraries.


I'd like you to build a Python a script that gathers the LLDP neighbors for each device. 
 Final object should be a dictionary with 4 key value pairs.  Each key should be the hostname
 of the device and the value for each should be a list of dictionaries (neighbors). 
 Each neighbor/dictionary should have 3 keys, which are:  neighbor, neighbor_interface, and local_interface. 
For example, it should look like this..note that the example is showing 2 devices, but yours should have all 4. 

 At least you can see what the final data type looks like:


{
    "nxos-spine1": [
        {
            "neighbor_interface": "Eth2/1", 
            "local_interface": "Eth2/1", 
            "neighbor": "nxos-spine2.ntc.com"
        }, 
        {
            "neighbor_interface": "Eth2/2", 
            "local_interface": "Eth2/2", 
            "neighbor": "nxos-spine2.ntc.com"
        }, 
        {
            "neighbor_interface": "Eth2/3", 
            "local_interface": "Eth2/3", 
            "neighbor": "nxos-spine2.ntc.com"
        }, 
        {
            "neighbor_interface": "Eth2/4", 
            "local_interface": "Eth2/4", 
            "neighbor": "nxos-spine2.ntc.com"
        }
    ], 
    "nxos-spine2": [
        {
            "neighbor_interface": "Eth2/1", 
            "local_interface": "Eth2/1", 
            "neighbor": "nxos-spine1.ntc.com"
        }, 
        {
            "neighbor_interface": "Eth2/2", 
            "local_interface": "Eth2/2", 
            "neighbor": "nxos-spine1.ntc.com"
        }, 
        {
            "neighbor_interface": "Eth2/3", 
            "local_interface": "Eth2/3", 
            "neighbor": "nxos-spine1.ntc.com"
        }, 
        {
            "neighbor_interface": "Eth2/4", 
            "local_interface": "Eth2/4", 
            "neighbor": "nxos-spine1.ntc.com"
        }
    ]
