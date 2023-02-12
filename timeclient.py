import socket

def main():
    # Creating socket
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    # Connecting to server
    HOST = '::1'
    PORT = 55555
    client_socket.connect((HOST, PORT))

    print(f"Connected to {HOST}:{PORT}")

    try:
        while True:
            # Receive time from the server
            timestamp = client_socket.recv(1024).decode()
            print(timestamp)
    except KeyboardInterrupt:
        # Handle keyboard interrupt
        client_socket.close()
        print(f"Disconnected from {HOST}:{PORT}")

if __name__ == '__main__':
    main()
