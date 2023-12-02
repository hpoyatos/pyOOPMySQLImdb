from model.Pessoa import Pessoa

class PessoaDAO:
    #atributos para guardar a conexão e cursor do banco de dados (seja ele qual for)
    conexao = None
    cursor = None

    # Construtor
    def __init__(self, _conexao, _cursor):
        self.conexao = _conexao
        self.cursor = _cursor


    # getAll(): ao chamar, o requisitante receberá um array de objetos do tipo Pessoa representando todas as pessoas da tabela pessoa!
    def getAll(self):
        sql = "SELECT id, nome FROM pessoa"

        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()

            pessoas = []
            for linha in resultado:
                pessoa = Pessoa(linha[0], linha[1])
                pessoas.append(pessoa)

            return pessoas
        except Exception as e:
            print(e)

            #return e

    #método save(): recebe um objeto do tipo pessoa e retorna um booleano (deu certo, não deu certo....)
    def save(self, _pessoa):
        sql = f"INSERT INTO pessoa (nome) VALUES ('{_pessoa.nome}')"

        try:
            self.cursor.execute(sql)
            self.conexao.commit()
            _pessoa.id = self.cursor.lastrowid
            return True
        except Exception as e:
            print(e)
            return False
