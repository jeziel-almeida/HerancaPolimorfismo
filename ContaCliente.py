from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self, numero, iof, ir, valor_investido, taxarendimento):
        self.numero = numero
        self.iof = iof
        self.ir = ir
        self.valor_investido = valor_investido
        self.taxarendimento = taxarendimento
        self.tipo_conta = 'cliente'

    @abstractmethod
    def CalculoRendimento(self):
        pass

    def Extrato(self):
        print(f"O saldo atual da conta {self.tipo_conta} nº {self.numero} é {self.valor_investido:.2f}")