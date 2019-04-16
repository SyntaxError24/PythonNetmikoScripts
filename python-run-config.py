#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "host": "10.0.1.170",
    "username": "cisco",
    "password": getpass(),
    "device_type": "cisco_ios",
}
# Pulls running config from a Cisco iOS device
net_connect = Netmiko(**cisco1)
command = "show run"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()
