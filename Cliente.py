class Cliente:
  def __init__(self, cpf, nome, endereco):
    self.cpf = cpf
    self.nome = nome
    self.endereco = endereco

  def info_cliente(self):
    return f"Nome: {self.nome}. Endereço: {self.endereco}"