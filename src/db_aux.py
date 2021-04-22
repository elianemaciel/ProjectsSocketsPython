from models.db import engine
from sqlalchemy.orm import relationship, backref, sessionmaker
import json
from models.Livros import Livros, Edicao
from models.Autor import Autor
from models.LivroAutor import LivroAutor
from models.LivrosTemp import LivrosTemp


class DBAux():

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.conn = engine.connect()

    def create_book(self, data):
        author = self.find_or_create_author(data.autor)
        book = Livros(titulo=data.titulo)
        session.add(book)
        session.commit()

        edition = self.create_edition(data.edicao, book)
        livroautor = self.create_book_author(book, author)

    def find_or_create_author(self, autor):
        query = self.session.query(Autor).filter(Autor.nome == autor).first()

        if len(query):
            return query[0]
        else:
            autor = Autor(nome=autor)
            self.session.add()
            self.session.commit()

    def create_edition(self, edicao, ano, livro):
        edicao = Edicao(numero=edicao, ano=ano, codigolivro=livro.codigo)
        self.session.add(edicao)
        self.session.commit()
        return edicao

    def create_book_author(self, book, author):
        livroautor = LivroAutor(codigolivro=book.codigo, codigoautor=autor.codigo)
        self.session.add(livroautor)
        self.session.commit()
        return edicao

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
        obj = self.session.query(Livros).filter(Livros.titulo.like('%' + title.titulo)).first()
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

        autor = self.session.query(Autor)\
            .filter(LivroAutor.codigoautor == Autor.codigo, LivroAutor.codigolivro == data['codigo']).first()
        autor.nome = data['autor']
        self.session.commit()
