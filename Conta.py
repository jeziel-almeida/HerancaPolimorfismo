import datetime
from Extrato import Extrato

class Conta:
  def __init__(self, clientes, numero):
    self.clientes = clientes
    self.numero = numero
    self._saldo = 0
    self.data_abertura = datetime.datetime.today()
    self.extrato = Extrato()

  @property
  def saldo(self):
    return self._saldo
  
  @saldo.setter
  def saldo(self, saldo):
    if saldo < 0:
      print("saldo inválido")
    else:
      self._saldo = saldo

  def depositar(self, valor):
    self._saldo += valor
    self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

  def sacar(self, valor):
    if self._saldo < valor:
      return False
    else:
      self._saldo -= valor
      self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
      return True

  def gerar_extrato(self):
    print(f"Número: {self.numero}\nSaldo: {self._saldo}")

  def transfereValor(self, contaDestino, valor):
    if self._saldo < valor:
      return False
    else:
      contaDestino.depositar(valor)
      self._saldo -= valor
      self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, "Data", datetime.datetime.today()])
    return True

