import logging
import os
from netmiko import ConnectHandler

logging.basicConfig(filename = 'HN_TKT6523584.log', level = logging.DEBUG)
logger = logging.getLogger('netmiko')

Network_Device = {"host": "10.128.163.52",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k05-leaf-eat1")
c = ConnectHandler(**Network_Device)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b,d) in zip(range(15,32),range(41,59),range(15,32)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-HADOOP1-ESXi-' + str(b) + ' PORT1 TKT6523584' + '\n')
    command = c.send_command_timing('channel-group ' + str(d) + ' force mode active' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
  

print("done")
print("Initiating configuration of the Port Channels")

for (x,y) in zip(range(15,32),range(41,59)):
    command = c.send_command_timing('interface port-channel' + str(x) + '\n')
    command = c.send_command_timing('shutdown' + '\n')
    command = c.send_command_timing('description WDC-HADOOP1-ESXi-' + str(y) + ' TKT6523584' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 1021,1034,1101,3176,3212,3250,3889,3891,3895,3911,3934,3949' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('no lacp suspend-individual' + '\n')
    command = c.send_command_timing('vpc ' + str(x) + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device2 = {"host": "10.128.163.53",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k06-leaf-eat1")
c = ConnectHandler(**Network_Device2)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b,d) in zip(range(15,32),range(41,59),range(15,32)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-HADOOP1-ESXi-' + str(b) + ' PORT2 TKT6523584' + '\n')
    command = c.send_command_timing('channel-group ' + str(d) + ' force mode active' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("done")
print("Initiating configuration of the Port Channels")

for (x,y) in zip(range(15,32),range(41,59)):
    command = c.send_command_timing('interface port-channel' + str(x) + '\n')
    command = c.send_command_timing('shutdown' + '\n')
    command = c.send_command_timing('description WDC-HADOOP1-ESXi-' + str(y) + ' TKT6523584' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 1021,1034,1101,3176,3212,3250,3889,3891,3895,3911,3934,3949' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('no lacp suspend-individual' + '\n')
    command = c.send_command_timing('vpc ' + str(x) + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

print("done")
