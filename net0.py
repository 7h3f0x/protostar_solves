#!/usr/bin/python
from pwn import *
from ssh import *

p=sh.remote('localhost',2999)
p.recvuntil("'")
integer=p.recvuntil("'")[:-1]
payload=p32(int(integer))
p.sendline(payload)
print p.recvall()
