# SecuRecon
Python Security Reconnaissance Tool for authorized security testing
SecuRecon - Python Security Reconnaissance Tool

SecuRecon is a Python-based security reconnaissance and basic web security assessment tool designed for authorized security testing and cybersecurity labs.

Features

- DNS/IP resolution
- TCP port scanning
- Common service identification
- HTTP/HTTPS connectivity checking
- HTTP security header analysis
- Command-line target selection

Technologies

- Python 3
- Socket
- Requests
- Argparse

Installation

Clone the repository:

git clone https://github.com/Eliyas-111/SecuRecon.git
cd SecuRecon

Install the required dependency:

pip install -r requirements.txt

Usage

Run the tool with an authorized target:

python secorecon.py -t 192.0.2.1

You can also test a domain:

python secorecon.py -t example.com

Example

=============================================
       SECORECON SECURITY SCANNER
=============================================

Target: 192.0.2.1

[+] DNS Resolution
    IP Address: 192.0.2.1

[+] Port Scan
    [+] 22/tcp OPEN - SSH
    [+] 80/tcp OPEN - HTTP

[+] HTTP Security Header Check
    [-] Content-Security-Policy: MISSING
    [+] X-Frame-Options: PRESENT

[+] Scan completed.

Disclaimer

This tool is intended for authorized security testing, cybersecurity labs, and systems for which you have explicit permission to perform security assessments.

Do not scan systems without authorization.

The author does not encourage, support, or take responsibility for unauthorized, illegal, or malicious use of this tool.

You are responsible for obtaining proper permission before testing any domain, IP address, network, or system
