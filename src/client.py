import sys
import xmlrpc.client
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


def create_book(servidor):
    book_title = input("Informe o titulo do livro:\n")
    book_author = input("Informe o autor do livro\n")
    book_edition = input("Informe a edicao do livro\n")
    book_year = input("Informe o ano do livro\n")
    book = CreateDTO(book_title, book_author, book_edition, book_year)
    print("%s" % servidor.create(book))


def find_book(servidor):
    book_title = input("Informe o titulo do livro:\n")
    book_author = input("Informe o autor do livro\n")
    book = CreateDTO(book_title, book_author)
    print("%s" % servidor.find_book(book))


def find_book_year(servidor):
    book_edition = input("Informe a edicao do livro\n")
    book_year = input("Informe o ano do livro\n")
    book = CreateDTO(edition=book_edition, year=book_year)
    print("%s" % servidor.find_book_year(book))


def delete_book(servidor):
    book_title = input("Informe o titulo do livro:\n")
    book = CreateDTO(book_title)
    print("%s" % servidor.delete_book(book))

def edit_book(servidor):
    book_codigo = input("Informe o código do livro:\n")
    book_title = input("Informe o titulo do livro:\n")
    book_author = input("Informe o autor do livro\n")
    book_edition = input("Informe a edicao do livro\n")
    book_year = input("Informe o ano do livro\n")
    book = CreateDTO(book_title, book_author, book_edition, book_year, book_codigo)
    print("%s" % servidor.edit_book(book))



def main():
    if len(sys.argv) != 3:
        print('%s <ip> <porta>' % sys.argv[0])
        sys.exit(0)

    ip = sys.argv[1]
    porta = sys.argv[2]

    servidor = xmlrpc.client.ServerProxy('http://' + ip + ':'+ porta)

    while(True):
        m = menu()
        if m == 1:
            create_book(servidor)
        elif m == 2:
            find_book(servidor)
        elif m == 3:
            find_book_year(servidor)
        elif m == 4:
            delete_book(servidor)
        elif m == 5:
            edit_book(servidor)
        else:
            exit()


if __name__ == "__main__":
    main()
