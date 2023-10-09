import socket

target_host = "web"
target_ports = [80, 443, 22, 25]  # List of ports to scan

def scan_port(target_host, target_port):
    try:
        # Create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt (adjust as needed)
        client.settimeout(2)
        
        # Attempt to connect to the target host and port
        client.connect((target_host, target_port))
        
        # If the connection is successful, the port is open
        print(f"[+] Port {target_port}/TCP is open")
        
        # Close the socket
        client.close()
    except (socket.timeout, ConnectionRefusedError):
        # If the connection times out or is refused, the port is closed
        print(f"[-] Port {target_port}/TCP is closed")

# Loop through the list of target ports and scan each one
for port in target_ports:
    scan_port(target_host, port)
