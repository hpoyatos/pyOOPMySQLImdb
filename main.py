from model.Pessoa import Pessoa
from model.Database import Database
from dao.PessoaDAO import PessoaDAO

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

