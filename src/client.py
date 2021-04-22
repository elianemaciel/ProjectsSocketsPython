import sys
import socket
import json
from time import sleep
from dto.CreateDto import CreateDTO


def menu():
    print("\n\nDigite:\n")
    print("1 -> Criar livro")
    print("2 -> Consultar livro")
    print("3 -> Consultar por ano e número da edição")
    print("4 -> Remover livro")
    print("5 -> Alteração do Livro")
    print("0 -> Sair")
    d = int(input())
    return d


def create_book():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[1]
    porta = int(sys.argv[2])
    s.connect((ip, porta))

    book_title = input("Informe o titulo do livro:\n")
    book_author = input("Informe o autor do livro\n")
    book_edition = input("Informe a edicao do livro\n")
    book_year = input("Informe o ano do livro\n")
    book = CreateDTO(book_title, book_author, book_edition, book_year)

    s.send('1'.encode())
    msg = int(s.recv(1024))

    print(msg)
    if msg == 200:
        s.sendall((bytes(book.to_json(), encoding='utf-8')))
        msg = s.recv(10000)
        print('Received: %s' % msg.decode('utf-8'))
        s.close()
    else:
        print("OP invalida")
        s.close()


def find_book():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[1]
    porta = int(sys.argv[2])
    s.connect((ip, porta))

    book_title = input("Informe o titulo do livro:\n")
    book_author = input("Informe o autor do livro\n")
    book = CreateDTO(book_title, book_author)

    s.send('2'.encode())
    msg = int(s.recv(1024))
    print(msg)
    if msg == 200:
        s.sendall((bytes(book.to_json(), encoding='utf-8')))
        msg = s.recv(10000)
        print('Received: %s' % msg.decode('utf-8'))
        s.close()
    else:
        print("OP invalida")
        s.close()


def find_book_year():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[1]
    porta = int(sys.argv[2])
    s.connect((ip, porta))

    book_edition = input("Informe a edicao do livro\n")
    book_year = input("Informe o ano do livro\n")
    book = CreateDTO(edition=book_edition, year=book_year)

    s.send('3'.encode())
    msg = int(s.recv(1024))
    print(msg)
    if msg == 200:
        s.sendall((bytes(book.to_json(), encoding='utf-8')))
        msg = s.recv(10000)
        print('Received: %s' % msg.decode('utf-8'))
        s.close()
    else:
        print("OP invalida")
        s.close()


def delete_book():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[1]
    porta = int(sys.argv[2])
    s.connect((ip, porta))

    book_title = input("Informe o titulo do livro:\n")
    book = CreateDTO(book_title)

    s.send('4'.encode())
    msg = int(s.recv(1024))
    print(msg)
    if msg == 200:
        s.sendall((bytes(book.to_json(), encoding='utf-8')))
        msg = s.recv(10000)
        print('Received: %s' % msg.decode('utf-8'))
        s.close()
    else:
        print("OP invalida")
        s.close()


def edit_book():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[1]
    porta = int(sys.argv[2])
    s.connect((ip, porta))

    book_codigo = input("Informe o cógigo do livro:\n")
    book_title = input("Informe o titulo do livro:\n")
    book_author = input("Informe o autor do livro\n")
    book_edition = input("Informe a edicao do livro\n")
    book_year = input("Informe o ano do livro\n")
    book = CreateDTO(book_title, book_author, book_edition, book_year, book_codigo)

    s.send('5'.encode())
    msg = int(s.recv(1024))
    print(msg)
    if msg == 200:
        s.sendall((bytes(book.to_json(), encoding='utf-8')))
        msg = s.recv(10000)
        print('Received: %s' % msg.decode('utf-8'))
        s.close()
    else:
        print("OP invalida")
        s.close()


def main():
    if len(sys.argv) != 3:
        print('%s <ip> <porta>' % sys.argv[0])
        sys.exit(0)

    while(True):
        m = menu()
        if m == 1:
            create_book()
        elif m == 2:
            find_book()
        elif m == 3:
            find_book_year()
        elif m == 4:
            delete_book()
        elif m == 5:
            edit_book()
        else:
            exit()


if __name__ == "__main__":
    main()
