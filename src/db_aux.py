from models.db import engine
from sqlalchemy.orm import relationship, backref, sessionmaker
import json
from models.Livros import Livros, Edicao, LivroAutor, Autor
from models.LivrosTemp import LivrosTemp


class DBAux():

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.conn = engine.connect()

    def create_book(self, data):
        try:

            book = Livros(titulo=data['titulo'])
            self.session.add(book)
            self.session.commit()

            self.session.flush()
        except Exception as e:
            print(e)

        author = self.create_author(data['autor'], book)

        edition = self.create_edition(data['edicao'], data['ano'], book)

    def create_author(self, author_nome, book):
        try:
            author = Autor(nome=author_nome)
            self.session.add(author)
            self.session.commit()
            self.session.flush()
            association = self.create_book_author(book, author)
            return author
        except Exception as e:
            print(e)
            print("Problema para criar o author")
            return None

    def create_edition(self, edicao, ano, livro):
        try:
            edicao = Edicao(numero=edicao, ano=ano, codigolivro=livro.codigo)
            self.session.add(edicao)
            self.session.commit()
            return edicao
        except Exception as e:
            print(e)
            print("Problema ao criar edição")
            return None

    def create_book_author(self, book, author):
        try:
            livroauthor = LivroAutor(codigolivro=book.codigo, codigoautor=author.codigo)
            self.session.add(livroauthor)
            self.session.commit()
            return livroauthor
        except Exception as e:
            print(e)
            print("Problema ao criar associação book_author")
            return None

    def find_book(self, book_title, book_author):
        list_book = []
        for book in self.session.query(Livros) \
                .filter(LivroAutor.codigoautor == Autor.codigo, LivroAutor.codigolivro == Livros.codigo)\
                .filter(Livros.titulo.ilike('%' + book_title + '%'))\
                .filter(Autor.nome.ilike('%' + book_author + '%')).all():

            list_book.append(book.get_livros_infos(self.session))

        return json.dumps(list_book)

    def find_book_edition(self, edition, year):

        list_book = []
        for book in self.session\
                .query(
                    Livros.codigo,
                    Livros.titulo,
                    Edicao.numero,
                    Edicao.ano,
                    Autor.nome
                )\
                .join(Edicao)\
                .filter(LivroAutor.codigoautor == Autor.codigo, LivroAutor.codigolivro == Livros.codigo)\
                .filter(Edicao.numero == edition)\
                .filter(Edicao.ano == year).all():

            ed_dict = {
                'titulo': book.titulo.strip(),
                'edicao': book.numero,
                'ano': book.ano,
                'autor': book.nome.strip()
            }
            list_book.append(ed_dict)
        return json.dumps(list_book)

    def delete_book(self, title):
        obj = self.session.query(Livros)\
            .filter(Livros.titulo.ilike('%' + title['titulo'] + '%')).first()

        if obj:
            self.session.delete(obj)
            self.session.commit()

    def update_book(self, data):
        print(data)
        book = self.session.query(Livros)\
            .filter(Livros.codigo == data['codigo']).first()
        book.titulo = data['titulo']
        self.session.commit()
        edition = self.session.query(Edicao)\
            .filter(Edicao.codigolivro == data['codigo']).first()
        edition.numero = data['edicao']
        edition.ano = data['ano']
        self.session.commit()

        author = self.session.query(Autor)\
            .filter(LivroAutor.codigoautor == Autor.codigo, LivroAutor.codigolivro == data['codigo']).first()
        author.nome = data['autor']
        self.session.commit()
