import logging
import os
from netmiko import ConnectHandler

logging.basicConfig(filename = 'HN_TKT6605053.log', level = logging.DEBUG)
logger = logging.getLogger('netmiko')

Network_Device = {"host": "10.128.160.21",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k03-eng-dci-eat1")
c = ConnectHandler(**Network_Device)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b) in zip(range(52,61),range(1,10)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX0' + str(b) + ' PORT1 TKT6605053' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600,701-703,705-710' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
  
for (a,b) in zip(range(61,64),range(10,13)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(b) + ' PORT1 TKT6605053' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600,701-703,705-710' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()

Network_Device2 = {"host": "10.128.160.22",
                   "username": "svc.dcmetroscript",
                   "password": "^9Ev@!.^9Vv8Z7Gjka7",
                   "device_type":"cisco_nxos",
    }

print("Initiating SSH into n9k04-eng-dci-eat1")
c = ConnectHandler(**Network_Device2)
c.enable()
print("Initiating the configuration of the physical interfaces")
command = c.send_command_timing('conf t\n')
for (a,b) in zip(range(52,61),range(1,10)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX0' + str(b) + ' PORT2 TKT6605053' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600,701-703,705-710' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
  
for (a,b) in zip(range(61,64),range(10,13)):
    command = c.send_command_timing('interface ethernet 1/' + str(a) + '\n')
    command = c.send_command_timing('description WDC-PRD-H-ESX' + str(b) + ' PORT2 TKT6605053' + '\n')
    command = c.send_command_timing('switchport' + '\n')
    command = c.send_command_timing('switchport mode trunk' + '\n')
    command = c.send_command_timing('switchport trunk allowed vlan 600,701-703,705-710' + '\n')
    command = c.send_command_timing('spanning-tree port type edge trunk ' + '\n')
    command = c.send_command_timing('mtu 9216' + '\n')
    command = c.send_command_timing('vpc orphan-port suspend' + '\n')
    command = c.send_command_timing('no shutdown' + '\n')
    
print("Config is completed, saving config")

command = c.send_command_timing('end' + '\n')
command = c.send_command_timing('copy r s' + '\n')

c.disconnect()


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
