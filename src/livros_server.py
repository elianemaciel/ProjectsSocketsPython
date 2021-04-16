import sys
import socket
import json
from types import SimpleNamespace
# from sockets.python2.server import Server
from models.Livros import Livros
from models.Autor import Autor
from models.Edicao import Edicao
from models.LivroAutor import LivroAutor
from models.LivrosTemp import LivrosTemp


# print(Livros.query.all())


# class LivrosServer(Server):
#     def act_on(self, data, addr):
#         # Do something with data (in bytes) and return a string.
#         return data


# server = MyServer(listening_address=('127.0.0.1', 11112))
# server.listen()

m = {"id": 1, "name": "server"}
data = json.dumps(m)

if len(sys.argv) != 2:
  print('%s <porta>' % sys.argv[0])
  sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = int(sys.argv[1])

s.bind((ip, porta))
s.listen(10)

while True:
  s1, end = s.accept()
  msg = s1.recv(10000).decode('utf-8')
  print('Received: %s' % msg)
  dd = json.loads(msg, object_hook=lambda d: SimpleNamespace(**d))
  print(dd.name)
  s1.sendall((bytes(data,encoding='utf-8')))
  s1.close()