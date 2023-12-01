class Pessoa:
  # Atributos
  id = None
  nome = None

  # Método Construtor
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

  # Método __str__ ? (parecido com um método toString()...)
  def __str__(self):
    return f"Objeto do tipo Pessoa -> id: {self.id} nome: {self.nome}"