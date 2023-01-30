import Conta
from ContaPoupanca import ContaPoupanca

class ContaRemuneradaPoupanca(Conta.Conta, ContaPoupanca):
    def __init__(self, taxaremuneracao, clientes, numero, taxamanutencao):
        Conta.Conta.__init__(self, clientes, numero)
        ContaPoupanca.__init__(self, taxaremuneracao)
        self.taxamanutencao = taxamanutencao

    def remuneraConta(self):
        self._saldo += self._saldo * (self.taxaremuneracao/30)
        self._saldo -= self.taxamanutencao