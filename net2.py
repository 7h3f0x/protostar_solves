#!/usr/bin/python
from pwn import *
from ssh import *

p=sh.remote('localhost',2997)
y=[]
y.append(p.recv(4))
y.append(p.recv(4))
y.append(p.recv(4))
y.append(p.recv(4))
payload=0
# add numbers
for i in y:
	payload+=u32(i)
# wrap up to 32bits
payload=payload & 0xffffffff
# since the program uses read
p.sendline(p32(payload))
print p.recvall()