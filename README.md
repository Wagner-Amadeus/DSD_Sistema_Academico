# DSD_Sistema_Academico

1 - Crie um ambiente virtual:
python -m venv venv

2 - Instale as bibliotecas:
Pyro4: Uma biblioteca para permitir a comunicação entre objetos Python distribuídos.
pip install Pyro4

reportlab: Uma biblioteca para criar documentos PDF:
pip install reportlab

3 - Inicialize o server.py com python
Ele ira gerar um código URI;
Ex:
URI do servidor: PYRO:obj_1d023c24097a4eaeb715278dcdfa81b6@localhost:52149

Copie esse código no código fonte na mains() do client.py:
Ex:
def main():
    sistema_academico = Pyro4.Proxy("PYRO:obj_1d023c24097a4eaeb715278dcdfa81b6@localhost:52149")

Se divirta.