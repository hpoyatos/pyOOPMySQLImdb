#1o. passo: importar o conector
import mysql.connector
import config

class Database:
  conexao = None
  cursor = None

  def __init__(self):
    try:
      #2o. passo: criar o objeto de conexão 
      self.conexao = mysql.connector.connect(
        host="db4free.net",
        user="anima_imdb",
        password=config.senha_mysql,
        database="anima_imdb"
      )

      #3o. passo: criar um cursor
      self.cursor = self.conexao.cursor()
    except mysql.connector.errors.DatabaseError:
      print("Erro na conexão")
