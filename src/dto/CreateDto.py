import json

class CreateDTO:
  def __init__(self, title, author, edition, year):
    self.title = title
    self.author = author
    self.edition = edition
    self.year = year

  def to_json(self):
     return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
