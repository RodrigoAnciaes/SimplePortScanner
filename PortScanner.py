import socket
import argparse

well_known_ports = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    465: "SMTPS",
    993: "IMAPS",
    995: "POP3S"
}


def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...")
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout of 0.1 second
            sock.settimeout(0.01)
            # Attempt to connect to the target IP and port
            result = sock.connect_ex((target, port))
            if result == 0:
                if port in well_known_ports:
                    print(f"Port {port} ({well_known_ports[port]}): Open")
                else:
                    print(f"Port {port}: Open")
            sock.close()
        except socket.error:
            print(f"Could not connect to port {port}")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("target", help="IP address or URL to scan")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    args = parser.parse_args()

    # Call the scan_ports function with the provided arguments
    scan_ports(args.target, args.start_port, args.end_port)

# example usage with command line arguments
# python PortScanner.py -h 10.