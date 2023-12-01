from model.Pessoa import Pessoa

class PessoaDAO:
    #atributos para guardar a conexão e cursor do banco de dados (seja ele qual for)
    conexao = None
    cursor = None

    # Construtor
    def __init__(self, _conexao, _cursor):
        self.conexao = _conexao
        self.cursor = _cursor


