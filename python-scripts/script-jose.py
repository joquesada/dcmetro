import logging
import os
from netmiko import ConnectHandler

logging.basicConfig(filename = 'HN_TKT6519834.log', level = logging.DEBUG)
logger = logging.getLogger('netmiko')

Network_Device = {"host": "10.188.232.49",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k49-leaf-sjc05")
c = ConnectHandler(**Network_Device)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b,d) in zip(range(1,10),range(1,10),range(10,19)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(b) + ' PORT1 TKT6415730' + '\n')
    command = c.send_command_timing('channel-group ' + str(d) + ' force mode active' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
  
command = c.send_command_timing('conf t\n')
for (a,b,d) in zip(range(10,15),range(10,15),range(19,24)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX' + str(b) + ' PORT1 TKT6415730' + '\n')
    command = c.send_command_timing('channel-group ' + str(d) + ' force mode active' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("done")
print("Initiating configuration of the Port Channels")

for (x,y) in zip(range(10,19),range(1,10)):
    command = c.send_command_timing('interface port-channel' + str(x) + '\n')
    command = c.send_command_timing('shutdown' + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(y) + ' TKT6415730' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 1175-1183' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('no lacp suspend-individual' + '\n')
    command = c.send_command_timing('vpc ' + str(x) + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
for (x,y) in zip(range(19,24),range(10,15)):
    command = c.send_command_timing('interface port-channel' + str(x) + '\n')
    command = c.send_command_timing('shutdown' + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(y) + ' TKT6415730' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 1175-1183' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('no lacp suspend-individual' + '\n')
    command = c.send_command_timing('vpc ' + str(x) + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device2 = {"host": "10.188.232.50",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k50-leaf-sjc05")
c = ConnectHandler(**Network_Device2)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b,d) in zip(range(1,10),range(1,10),range(10,19)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(b) + ' PORT2 TKT6415730' + '\n')
    command = c.send_command_timing('channel-group ' + str(d) + ' force mode active' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (a,b,d) in zip(range(10,15),range(10,15),range(19,24)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(b) + ' PORT2 TKT6415730' + '\n')
    command = c.send_command_timing('channel-group ' + str(d) + ' force mode active' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("done")
print("Initiating configuration of the Port Channels")

for (x,y) in zip(range(10,19),range(1,10)):
    command = c.send_command_timing('interface port-channel' + str(x) + '\n')
    command = c.send_command_timing('shutdown' + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(y) + ' TKT6415730' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 1175-1183' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('no lacp suspend-individual' + '\n')
    command = c.send_command_timing('vpc ' + str(x) + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

for (x,y) in zip(range(19,24),range(10,15)):
    command = c.send_command_timing('interface port-channel' + str(x) + '\n')
    command = c.send_command_timing('shutdown' + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX' + str(y) + ' TKT6415730' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 1175-1183' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('no lacp suspend-individual' + '\n')
    command = c.send_command_timing('vpc ' + str(x) + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()


Network_Device3 = {"host": "10.188.7.193",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into core01-mgmt-sjc05")
c = ConnectHandler(**Network_Device3)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(1,10),range(1,10)):
    command = c.send_command_timing('interface ethernet 171/1/' + str(e) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(g) + ' - IDR TKT6415730' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(10,13),range(27,30)):
    command = c.send_command_timing('interface ethernet 171/1/' + str(e) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX' + str(g) + ' - IDR TKT6415730' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(13,15),range(39,41)):
    command = c.send_command_timing('interface ethernet 171/1/' + str(e) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX' + str(g) + ' - IDR TKT6415730' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')


print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device4 = {"host": "10.188.7.194",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into core02-mgmt-sjc05")
c = ConnectHandler(**Network_Device4)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (f,h) in zip(range(1,10),range(1,10)):
    command = c.send_command_timing('interface ethernet 171/1/' + str(h) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX0' + str(f) + ' - IDR TKT6415730' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (f,h) in zip(range(10,13),range(27,30)):
    command = c.send_command_timing('interface ethernet 171/1/' + str(h) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX' + str(f) + ' - IDR TKT6415730' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (f,h) in zip(range(13,15),range(39,41)):
    command = c.send_command_timing('interface ethernet 171/1/' + str(h) + '\n')
    command = c.send_command_timing('description SC2-SANDBOX-ESX' + str(f) + ' - IDR TKT6415730' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

print("done")
