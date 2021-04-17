import sys
import socket
import json
from types import SimpleNamespace
from models.Livros import Livros
from models.Autor import Autor
from models.Edicao import Edicao
from models.LivroAutor import LivroAutor
from models.LivrosTemp import LivrosTemp
from dto.CreateDto import CreateDTO


def create_book(s):
  s.send('200'.encode())
  data = s.recv(10000).decode('utf-8')
  print('Received: %s' % data)
  #  TODO ADD SAVE
  s.send("Criado com sucesso".encode())

def find_book(s):
  s.send("TODO ADD".encode)


def find_book_year(s):
  s.send("TODO ADD".encode)


def delete_book(s):
  s.send("TODO ADD".encode)


def edit_book(s):
  s.send("TODO ADD".encode)


def main():
  if len(sys.argv) != 2:
    print('%s <porta>' % sys.argv[0])
    sys.exit(0)

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ip = 'localhost'
  porta = int(sys.argv[1])
  s.bind((ip, porta))
  s.listen(10)

  while(True):
    s1, end = s.accept()
    m = int(s1.recv(1024).decode('utf-8'))
    if m == 1:
      create_book(s1)
    elif m == 2:
      find_book(s1)
    elif m == 3:
      find_book_year(s1)
    elif m == 4:
      delete_book(s1)
    elif m == 5:
      edit_book(s1)
    else:
      s1.send('500'.encode)
      print("OP invalida")

    s1.close()


if __name__ == "__main__":
    main()
