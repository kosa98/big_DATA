#!/usr/bin/python3

import sys

ck, mk, vk = 0, 0, 0

for line in sys.stdin:
	price = line.strip()
	
	
	if price.isnumeric() == False:
		continue
		print('s')
		
	price = int(price)
	

	ck += 1
	mk += price
	vk += price**2




mk = mk / ck
vk = vk / ck - mk**2


print(ck, mk, vk)
