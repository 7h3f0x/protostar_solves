#!/usr/bin/python
from pwn import *
from ssh import *

p=sh.remote('localhost',2998)
x=p.recv()
payload=u32(x)
p.sendline(str(payload))
print p.recvall()