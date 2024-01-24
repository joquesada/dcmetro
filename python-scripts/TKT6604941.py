import logging
import os
from netmiko import ConnectHandler

logging.basicConfig(filename = 'HN_TKT6605053.log', level = logging.DEBUG)
logger = logging.getLogger('netmiko')

Network_Device = {"host": "10.188.7.174",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k01-eng-dci-sjc05")
c = ConnectHandler(**Network_Device)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b) in zip(range(34,43),range(1,10)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description SC2-PRD-H-ESX0' + str(b) + ' PORT1 TKT6604941' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600-603,605-611' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
  
for (a,b) in zip(range(43,46),range(10,13)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(b) + ' PORT1 TKT6604941' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600-603,605-611' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device2 = {"host": "10.188.7.175",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k02-eng-dci-sjc05")
c = ConnectHandler(**Network_Device2)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b) in zip(range(34,43),range(1,10)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description SC2-PRD-H-ESX0' + str(b) + ' PORT2 TKT6604941' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600-603,605-611' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
  
for (a,b) in zip(range(43,46),range(10,13)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(b) + ' PORT2 TKT6604941' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600-603,605-611' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()


Network_Device3 = {"host": "10.188.7.177",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into access01-mgmt-sjc05")
c = ConnectHandler(**Network_Device3)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(1,10),range(25,34)):
    command = c.send_command_timing('interface ethernet 185/1/' + str(e) + '\n')
    command = c.send_command_timing('description SC2-PRD-H-ESX0' + str(g) + ' - IDR TKT6604941' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(10,13),range(34,37)):
    command = c.send_command_timing('interface ethernet 185/1/' + str(e) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(g) + ' - IDR TKT6604941' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device4 = {"host": "10.188.7.176",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into access02-mgmt-sjc05")
c = ConnectHandler(**Network_Device4)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(1,10),range(25,34)):
    command = c.send_command_timing('interface ethernet 185/1/' + str(e) + '\n')
    command = c.send_command_timing('description SC2-PRD-H-ESX0' + str(g) + ' - IDR TKT6604941' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(10,13),range(34,37)):
    command = c.send_command_timing('interface ethernet 185/1/' + str(e) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(g) + ' - IDR TKT6604941' + '\n')
    command = c.send_command_timing('switchport access vlan 100' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

print("done")
