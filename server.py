import Pyro4
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


@Pyro4.expose
class SistemaAcademico:
    def __init__(self):
        self.alunos = []


    def cadastrar_aluno(self, nome, nota1, nota2):
        aluno = {
            'nome': nome,
            'nota1': nota1,
            'nota2': nota2,
        }
        aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
        aluno['situacao'] = self.calcular_situacao(aluno['media'])
        self.alunos.append(aluno)


    def excluir_aluno(self, nome_aluno):
        for aluno in self.alunos:
            if aluno['nome'] == nome_aluno:
                self.alunos.remove(aluno)
                return True
        return False


    def listar_alunos(self):
        return self.alunos
    

    def calcular_situacao(self, media):
        if media >= 6:
            return 'Aprovado'
        elif media >= 4:
            return 'Recuperação'
        else:
            return 'Reprovado'
        
        
    def exportar(self, arquivo):
        try:
            with open(arquivo, 'w', newline='') as file:
                write = csv.writer(file, delimiter='|')
                write.writerow(['Nome', 'Nota 1', 'Nota 2', 'Media', 'Situação'])
                for aluno in self.alunos:
                    write.writerow([aluno['nome'], aluno['nota1'], aluno['nota2'], aluno['media'], aluno['situacao']])
            return True
        except Exception as e:
            return str(e)
        

    def exportar_pdf(self, arquivo):
        try:
            c = canvas.Canvas(arquivo, pagesize=letter)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "RELATÓRIO DE ALUNOS".center(80, "*"))
            
            y = 740
            for aluno in self.alunos:
                y -= 15
                c.drawString(100, y, f"Nome: "+ f"{aluno['nome']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Nota 1: " + f"{aluno['nota1']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Nota 2: " + f"{aluno['nota2']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Média: " + f"{aluno['media']}".rjust(15, "."))
                y -= 15
                c.drawString(100, y, f"Situação: " + f"{aluno['situacao']}".rjust(15, "."))
                y -= 15
            
            c.drawString(100, y-15, "FIM DO RELATÓRIO".center(80, "*"))
            
            c.save()
            return True
        except Exception as e:
            return str(e)
        

########## FIM DOS MÉTODOS ##########

daemon = Pyro4.Daemon()
uri = daemon.register(SistemaAcademico())

print(f"URI do servidor: {uri}")

daemon.requestLoop()
