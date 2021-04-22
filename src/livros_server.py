import sys
import socket
import json
from types import SimpleNamespace
from dto.CreateDto import CreateDTO
from db_aux import DBAux


def create_book(s, db):
    s.send('200'.encode())
    data = s.recv(10000).decode('utf-8')
    print('Received: %s' % data)

    try:
        db.create_book(json.loads(data))

        s.send("Criado com sucesso".encode())
    except:
        s.send("Problema ao criar livro".encode())


def find_book(s, db):
    s.send('200'.encode())
    data = s.recv(10000).decode('utf-8')
    print('Received: %s' % data)
    params = json.loads(data)
    data = db.find_book(params['titulo'], params['autor'])
    s.sendall((bytes(data, encoding='utf-8')))


def find_book_year(s, db):
    s.send('200'.encode())
    data = s.recv(10000).decode('utf-8')
    print('Received: %s' % data)
    params = json.loads(data)
    data = db.find_book_edition(params['edicao'], params['ano'])
    s.sendall((bytes(data, encoding='utf-8')))


def delete_book(s, db):
    s.send('200'.encode())
    data = s.recv(10000).decode('utf-8')
    print('Received: %s' % data)
    try:
        db.delete_book(json.loads(data))
        s.send("Deletado com sucesso".encode())
    except:
        s.send("Problema ao deletar.".encode())


def edit_book(s, db):
    s.send('200'.encode())
    data = s.recv(10000).decode('utf-8')
    print('Received: %s' % data)
    try:
        db.update_book(json.loads(data))
        s.send("Editado com sucesso".encode())
    except:
        s.send("Problema ao editar.".encode())


def main():
    db = DBAux()
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
            create_book(s1, db)
        elif m == 2:
            find_book(s1, db)
        elif m == 3:
            find_book_year(s1, db)
        elif m == 4:
            delete_book(s1, db)
        elif m == 5:
            edit_book(s1, db)
        else:
            s1.send('500'.encode)
            print("OP invalida")

        s1.close()


if __name__ == "__main__":
    main()
