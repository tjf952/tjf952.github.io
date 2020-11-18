<p align="center">
  <img src="images/queen-small.png"> 
</p>

## Welcome to my Gameboard

In my search to take better notes on my progress through penetration testing, I have decided to use [GitHub Pages](https://pages.github.com/). So this book will have a collection of commands and methodologies that I have used in the 80+ boxes I have _pwned_ over the past _x_ time. For myself, it will serve as my notebook as I complete multiple pentesting certifications i.e. [VHL](https://www.virtualhackinglabs.com/), [OSCP](https://www.offensive-security.com/pwk-oscp/), [OSWP](https://www.offensive-security.com/wifu-oswp/), etc.

### Methodology

Every pen-tester needs a checklist to run through. After running through many boxes and constantly refining my process of finding and exploiting vulnerabilities, I have simplified my process to the following steps:

#### Methodology Checklist

1. Scoping
  - Define criteria
  - Test initial connections
  - Analyze given information
2. [Reconnaissance](recon/alpha.md)
  - Information gathering and discovery
  - Device and OS enumeration
  - Port scanning
  - Network sniffing
3. [Enumeration](enum/bravo.md)
  - Advanced port scanning
  - Common vulnerability scripts
  - Common enumeration scripts
  - Manual enumeration if possible
4. Vulnerability Assessment
  - Vulnerability detection and analysis
  - Vulnerability locating i.e. exploitdb, github, searchsploit
  - Data validation
  - Configuration management
5. Exploitation
  - OS specific: [Linux](vuln/charlie.md) or [Windows](vuln/delta.md)
  - Vulnerability testing and verification
  - False positives and false negatives elimination
6. Analysis
  - Shell or root access
  - Access and persistence
  - Consolidate findings
  - [Report](writeups/echo.md) completion

### Other Stuff

This will be a work in progress so it will be updated every so often. Here is a list of interesting sites that have always helped me as well:
- [GTFOBins](https://gtfobins.github.io/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/)
- [B0F for OSCP](http://strongcourage.github.io/2020/04/19/bof.html)

### Support or Contact

Have something to say? Noticed a devastingly dumb mistake by yours truly and want to help me out? Message me on Discord [JoGo952#9149](https://discord.com/) and I'll do my best to get back to you.

You can check out my github [here](https://github.com/tjf952)... though it's not that interesting yet...

### Test Links

- [Scanning](recon/scan.md)
- [Web](enum/web.md)
- [Ports](enum/ports.md)
- [Vulnerabilities](vuln/vuln.md)
- [Passwords](vuln/password.md)
- [Linux](exploit/linux.md)
- [Windows](exploit/windows.md)
