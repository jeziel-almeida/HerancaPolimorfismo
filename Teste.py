from Banco import Banco
from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada

IOF = 0.01
IR = 0.1
taxarendimento = 0.05

banco_1 = Banco(2023, "PagBank")
conta_cliente_1 = ContaCliente(1, IOF, IR, 1000, taxarendimento)
conta_comum_1 = ContaComum(2, IOF, IR, 2000, taxarendimento)
conta_remunerada_1 = ContaRemunerada(3, IOF, IR, 2000, taxarendimento)

banco_1.adicionar_conta(conta_cliente_1)
banco_1.adicionar_conta(conta_comum_1)
banco_1.adicionar_conta(conta_remunerada_1)

banco_1.calcular_rendimento_mensal()
banco_1.imprime_saldo_contas()