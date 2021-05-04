import json


class CreateDTO:
    def __init__(self, title=False, author=False, edition=False, year=False, codigo=False):
        self.codigo = codigo
        self.titulo = title
        self.autor = author
        self.edicao = edition
        self.ano = year

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
