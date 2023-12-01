from model.Pessoa import Pessoa
from model.Database import Database

# Instanciar uma objeto do tipo pessoa a partir da classe Pessoa
poyatos = Pessoa(1, "Henrique Poyatos")

print(poyatos)

# Instanciar um objeto chamado db a partir da classe model/Database
db = Database()


db.cursor.execute("SELECT titulo, ano FROM filme ORDER BY ano")

#5o. passo: pegar a consulta e colocar na variável resultado.. (array)
filmes = db.cursor.fetchall()

for filme in filmes:
  print(filme)