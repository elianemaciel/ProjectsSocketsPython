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