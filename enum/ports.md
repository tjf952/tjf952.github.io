# Port Enumeration

## === Samba (SMB) ===

```bash
# smbmap
smbmap -H 10.10.10.1
# enum4linux
enum4linux -a 10.10.10.1
# smbclient
smbclient -L 10.10.10.1 -N
smbclient //10.10.10.1/directory -U guest
```

## === MySQL ===

```bash
# mysql
mysql -h 10.10.10.1 -u username -p password
# sqsh
sqsh -S 10.10.10.1 -U username -P "password"
```