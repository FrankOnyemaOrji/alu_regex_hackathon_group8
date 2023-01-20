#!/usr/bin/python3
import re
IP_Address = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')

IP_Address_search = input("Enter text>> ")
IP_Address_match = IP_Address.search(IP_Address_search)
print(IP_Address_match)

IP_Address_matches = IP_Address.finditer(IP_Address_search)

for IP_Address_match in IP_Address_matches:
    print(f"Your IP Address found are {IP_Address_match.group()}")