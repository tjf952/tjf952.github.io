# Scanning the Target

## Nmap

### Port Scanning
```bash
# full tcp scan
nmap -Pn -A -p- -T4 10.10.10.1 -o tcp-scan.txt
# full udp scan
nmap -sUV -F -T4 10.10.10.1 -o udp-scan.txt
```

### HTTP Enumeration
```bash
nmap -Pn -T4 -p 80 --script=http-enum 10.10.10.1
```

### Samba Enumeration
```bash
nmap -Pn -T4 --script smb-vuln* -p 139,445 10.10.10.1
nmap -Pn -T4 --script=smb-enum-shares.nse -p 445 10.10.10.1
```

### Network Scanning
```bash
nmap -sn 10.10.10.1/24
nmap -sn 10.10.10.1-253
nmap -sn 10.10.10.*
```

## Ping Sweep

```bash
# linux
for i in {1..254}; do (ping -c 10.10.10.$i | grep "bytes from" &); done
# windows
for /L %i in {1,1,255} do @ping -n 1 -w 200 10.10.10.%i > nul && echo 192.168.1.%i is up.
```

## Netcat (NC)

```bash
nc -nvC $ip $port
```
