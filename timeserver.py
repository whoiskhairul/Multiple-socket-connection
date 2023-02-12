import socket
from _thread import *
import time, datetime

# is called for sending the ISO-8601 Timestamps
def send_timestamps(connection):
    while True:
        timestamp = str(datetime.datetime.now()) + '\n'
        connection.sendall(timestamp.encode())
        time.sleep(5)

# called for haldling clients
def multi_threaded_client(connection):
    while True:
        send_timestamps(connection)
    connection.close()

def main():
    # Creating server that accepts ipv6 TCP connection
    HOST = ''
    PORT = 55555
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print("---Waiting to listen connections---")

    while True:
        connection, address = s.accept()
        print(f"{address} is connected")

        # for handling multiple clients, threads are used here.
        start_new_thread(multi_threaded_client, (connection, ))

    connection.close()

if __name__ == '__main__':
    main()
