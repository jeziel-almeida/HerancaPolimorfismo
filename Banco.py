class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, contacliente):
        self.contas.append(contacliente)

    def calcular_rendimento_mensal(self):
        for conta in self.contas:
            conta.CalculoRendimento()

    def imprime_saldo_contas(self):
        for conta in self.contas:
            conta.Extrato()