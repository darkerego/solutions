"""
In this kata you have to write a method to verify the validity of IPv4 addresses.

Example of valid inputs:

"1.1.1.1"

"127.0.0.1"

"255.255.255.255"

Example of invalid input:

"1444.23.9"

"153.500.234.444"

"-12.344.43.11"

"""

import ipaddress
def ipValidator(ip):
    """
    Using ipaddress instead of re
    """
    _ip = ip.split('.')
    if len(_ip) != 4:
        return False
    for i in _ip:
        if not i.isdigit():
            return False
        if int(i) > 255 or float(i) < 0:
            return False
    if ipaddress.IPv4Address(ip):
        return True
    return False
