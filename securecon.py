import socket
import requests
import argparse


# -----------------------------
# DNS Resolution
# -----------------------------
def dns_lookup(target):
    print("\n[+] DNS Resolution")

    try:
        ip = socket.gethostbyname(target)
        print(f"    IP Address: {ip}")
        return ip
    except socket.gaierror:
        print("    [-] Could not resolve target")
        return None


# -----------------------------
# TCP Port Scanner
# -----------------------------
def port_scan(target):
    print("\n[+] Port Scan")

    common_ports = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Proxy"
    }

    for port, service in common_ports.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"    [+] {port}/tcp OPEN - {service}")

        sock.close()


# -----------------------------
# HTTP Security Headers
# -----------------------------
def check_headers(target):
    print("\n[+] HTTP Security Header Check")

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    try:
        response = requests.get(
            target,
            timeout=5,
            allow_redirects=True
        )

        headers = response.headers

        security_headers = {
            "Content-Security-Policy": "CSP",
            "X-Frame-Options": "Clickjacking Protection",
            "X-Content-Type-Options": "MIME Sniffing Protection",
            "Strict-Transport-Security": "HSTS",
            "Referrer-Policy": "Referrer Policy",
            "Permissions-Policy": "Permissions Policy"
        }

        for header, description in security_headers.items():

            if header in headers:
                print(f"    [+] {header}: PRESENT")
            else:
                print(f"    [-] {header}: MISSING")

    except requests.RequestException as error:
        print(f"    [-] HTTP request failed: {error}")


# -----------------------------
# Main
# -----------------------------
def main():

    parser = argparse.ArgumentParser(
        description="SecuRecon - Python Security Reconnaissance Tool"
    )

    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Authorized domain or IP address"
    )

    args = parser.parse_args()

    target = args.target

    print("=" * 45)
    print("       SECORECON SECURITY SCANNER")
    print("=" * 45)

    print(f"\nTarget: {target}")

    ip = dns_lookup(target)

    if ip:
        port_scan(ip)
        check_headers(target)

    print("\n[+] Scan completed.")


if __name__ == "__main__":
    main()
