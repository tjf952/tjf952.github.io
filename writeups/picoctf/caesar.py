#!/usr/bin/python3
import sys
message = input('Enter the string to be decrypted: ')
for key in range(26):
	result = ''
	for c in message:
		if c.isupper(): result += chr((ord(c) + key - 65) % 26 + 65)
		elif c.islower(): result += chr((ord(c) + key - 97) % 26 + 97)
		else: result += c 
	print(f'Using shift {key}: {result}')