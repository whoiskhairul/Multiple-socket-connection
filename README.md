The problem is, we have to write 2 python files:

1. For server: Accepts incoming ipv6 TCP connections on port 55555 and sends Timestamps to the connected clients in a 5 seconds interval.

2. For clients: Will connect to the server and print the timestamps sent by the server.
