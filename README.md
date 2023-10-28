# DSD_Sistema_Academico

<p> 1 - Crie um ambiente virtual: </p> 
python -m venv venv

<br> <p> 2 - Instale as bibliotecas: </p>
<p> Pyro4: Uma biblioteca para permitir a comunicação entre objetos Python distribuídos. </p>
<p> pip install Pyro4 </p>

<p> reportlab: Uma biblioteca para criar documentos PDF: </p>
<p> pip install reportlab</p>

<br> 3 - Inicialize o server.py com python
<p> Ele ira gerar um código URI; </p> 
<p> Ex: </p> 
<p> URI do servidor: PYRO:obj_1d023c24097a4eaeb715278dcdfa81b6@localhost:52149 </p> 

<p> Copie esse código no código fonte na main() do client.py: </p> 
<p> Ex: </p> 
def main():
    sistema_academico = Pyro4.Proxy("PYRO:obj_1d023c24097a4eaeb715278dcdfa81b6@localhost:52149")

<br> <br> <strong> <p> Se divirta.</p> </strong> 
