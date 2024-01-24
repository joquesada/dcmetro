import logging
import os
from netmiko import ConnectHandler

logging.basicConfig(filename = 'HN_TKT6605053-1.log', level = logging.DEBUG)
logger = logging.getLogger('netmiko')


Network_Device3 = {"host": "10.128.221.100",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into access01-mgmt-eat1")
c = ConnectHandler(**Network_Device3)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(1,10),range(33,42)):
    command = c.send_command_timing('interface ethernet 157/1/' + str(e) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX0' + str(g) + ' - IDR TKT6605053' + '\n')
    command = c.send_command_timing('switchport access vlan 3856' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (g,e) in zip(range(10,13),range(42,45)):
    command = c.send_command_timing('interface ethernet 157/1/' + str(e) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(g) + ' - IDR TKT6605053' + '\n')
    command = c.send_command_timing('switchport access vlan 3856' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device4 = {"host": "10.128.221.101",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into access02-mgmt-eat1")
c = ConnectHandler(**Network_Device4)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (f,h) in zip(range(1,10),range(33,42)):
    command = c.send_command_timing('interface ethernet 157/1/' + str(h) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX0' + str(f) + ' - IDR TKT6605053' + '\n')
    command = c.send_command_timing('switchport access vlan 3856' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

command = c.send_command_timing('conf t\n')
for (f,h) in zip(range(10,13),range(42,45)):
    command = c.send_command_timing('interface ethernet 157/1/' + str(h) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(f) + ' - IDR TKT6605053' + '\n')
    command = c.send_command_timing('switchport access vlan 3856' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')

print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

print("done")
