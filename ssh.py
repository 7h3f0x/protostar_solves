from pwn import *
import os

IP = "172.16.152.130"

os.system('ssh-keygen -f "' + os.path.expanduser('~/.ssh/known_hosts') + '" -R ' + IP)
protostar_addr=IP
username='user'
password='user'
sh=ssh(username,protostar_addr,password=password)
