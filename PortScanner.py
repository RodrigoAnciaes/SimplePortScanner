import socket
import argparse
import pandas as pd
import csv

#read csv file and save variable in dictionary
with open('tcp.csv') as f:
    data = pd.read_csv(f)

#convert dictionary to dataframe
df = pd.DataFrame(data)


def scan_ports(target, start_port, end_port):
    """
    Scan ports on a target IP address within a specified range.

    Args:
        target (str): The target IP address to scan.
        start_port (int): The starting port number of the range.
        end_port (int): The ending port number of the range.

    Returns:
        None

    Raises:
        None
    
    Prints:
        Port number and service name (if available) of any open ports.
    """
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
                if port in df.index:
                    print(f"Port {port}: {df.loc[port]['description']}: Open")
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
# python PortScanner.py [target] [start_port] [end_port