#!/usr/bin/python3

import sys

ck_ans, mk_ans, vk_ans = 0, 0, 0

for line in sys.stdin:
	ck, mk, vk = (line.strip()).split()

	ck = int(ck)
	mk = float(mk)
	vk = float(vk)


	vk = (vk + mk**2) * ck
	mk = mk * ck

	ck_ans += ck
	mk_ans += mk
	vk_ans += vk


mk_ans = mk_ans / ck
vk_ans = vk_ans / ck_ans - mk_ans**2


print(ck_ans, mk_ans, vk_ans)

