import sys
import socket
import json

m = {'id': 1, 'name': 'client'}
data = json.dumps(m)


if len(sys.argv) != 3:
  print('%s <ip> <porta>' % sys.argv[0])
  sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = sys.argv[1]
porta = int(sys.argv[2])

s.connect((ip, porta))

s.sendall((bytes(data, encoding='utf-8')))

msg=s.recv(10000)
print('Received: %s' % msg.decode('utf-8'))


s.close()
