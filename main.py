from model.Pessoa import Pessoa
from model.Database import Database
from dao.PessoaDAO import PessoaDAO

# Instanciar uma objeto do tipo pessoa a partir da classe Pessoa
poyatos = Pessoa(1, "Henrique Poyatos")

print(poyatos)


# Instanciar um objeto chamado db a partir da classe model/Database
db = Database()


#exibir as pessoas que estão lá no banco de dados.
pessoaDAO = PessoaDAO(db.conexao, db.cursor)
pessoas = pessoaDAO.getAll()

for pessoa in pessoas:
  print(pessoa)

  