import sys
import json
from types import SimpleNamespace
from dto.CreateDto import CreateDTO
from db_aux import DBAux
import xmlrpc.server


def create(data):
    db = DBAux()
    db.create_book(data)
    return "Criado com sucesso"


def find_book(params):
    db = DBAux()
    return db.find_book(params['titulo'], params['autor'])



def find_book_year(params):
    db = DBAux()
    return db.find_book_edition(params['edicao'], params['ano'])


def delete_book(data):
    db = DBAux()
    db.delete_book(data)
    return "Deletado com sucesso"


def edit_book(data):
    db = DBAux()
    db.update_book(data)
    return "Editado com sucesso"



def main():
    db = DBAux()
    if len(sys.argv) != 2:
        print('%s <porta>' % sys.argv[0])
        sys.exit(0)

    porta = int(sys.argv[1])

    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', porta), allow_none=True)
    server.register_function(create, "create")
    server.register_function(find_book, "find_book")
    server.register_function(find_book_year, "find_book_year")
    server.register_function(edit_book, "edit_book")
    server.register_function(delete_book, "delete_book")
    server.serve_forever()



if __name__ == "__main__":
    main()
