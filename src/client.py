from sockets.python2.client import Client


client = Client()
response, addr = client.poll_server("Hello world", server=('127.0.0.1', 11112))
print response, addr