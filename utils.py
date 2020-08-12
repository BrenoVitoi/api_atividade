from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Souza',idade=30)
    print(pessoa)
    pessoa.save()
# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Souza').first()
    print(pessoa.idade)
# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Oliveira').first()
    #pessoa.idade = 21
    pessoa.nome = 'Breno'
    pessoa.save()
# Exclui dados na tabela passoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Souza').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
