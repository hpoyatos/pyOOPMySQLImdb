from model.Pessoa import Pessoa
from model.Database import Database
from dao.PessoaDAO import PessoaDAO
<<<<<<< HEAD
=======

# Instanciar uma objeto do tipo pessoa a partir da classe Pessoa
poyatos = Pessoa(1, "Henrique Poyatos")

print(poyatos)
>>>>>>> 542b90a8a132489d7017df5e9bb3e898c3388124


# Instanciar um objeto chamado db a partir da classe model/Database
db = Database()


#exibir as pessoas que estão lá no banco de dados.
pessoaDAO = PessoaDAO(db.conexao, db.cursor)
pessoas = pessoaDAO.getAll()

for pessoa in pessoas:
  print(pessoa)

keanu = Pessoa(0, "Keanu Reeves")
if pessoaDAO.save(keanu) == True:
  print("Keanu Reeves salvo no MySQL com sucesso!!!!!")
else:
  print("Deu ruim, Keanu...desculpa aí..")

# Será que o código está aqui neste objeto?
print(keanu)