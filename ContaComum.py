from ContaCliente import ContaCliente

class ContaComum(ContaCliente):
    def __init__(self, numero, iof, ir, valor_investido, taxarendimento):
        super().__init__(numero, iof, ir, valor_investido, taxarendimento)
        self.tipo_conta = 'comum'

    def CalculoRendimento(self):
        self.valor_investido += (self.valor_investido * self.taxarendimento)