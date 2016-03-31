A UDP Pinger in Python where packet drop rate is simulated to be 40% and
client can ping server, server echos the message as response and the client
can calculate Round Trip Time on response.

See screenshot to know how the Pinger output looks like.

EXECUTE:
========

To run the server:
`python UDPPingerServer.py <port no>`

Example: `python UDPPingerServer.py 12000`

To run the client:
`python UDPPingerClient.py < server ip address> <server port no>`

Example: `python UDPPingerClient.py 127.0.0.1 12000`
