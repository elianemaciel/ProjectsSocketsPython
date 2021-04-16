## Install

- `pip3 install -r requirements.txt`

### Create database

- Criar database no postgresql
- Alterar arquivo `src/models/settings.json`
- `python3 src/dump.py`


### Executar

- python3 src/livros_server.py 6001
- python3 src/client.py localhost 6001