class ContaCliente:
    def __init__(self, numero, iof, ir, valor_investido, taxarendimento):
        self.numero = numero
        self.iof = iof
        self.ir = ir
        self.valor_investido = valor_investido
        self.taxarendimento = taxarendimento
        self.tipo_conta = 'cliente'

    def CalculoRendimento(self):
        self.valor_investido += (self.valor_investido * self.taxarendimento)
        self.valor_investido -= (self.valor_investido * (self.iof + self.ir))

    def Extrato(self):
        print(f"O saldo atual da conta {self.tipo_conta} nº {self.numero} é {self.valor_investido:.2f}")