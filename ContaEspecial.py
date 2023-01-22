from Conta import Conta
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, limite):
        Conta.__init__(self, clientes, numero)
        self.limite = limite

    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            return False
        else:
            self._saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True