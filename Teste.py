from Banco import Banco
from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada

IOF = 0.01
IR = 0.1
taxarendimento = 0.05

banco_1 = Banco(2023, "PagBank")

#* Classe abstrata não pode ser instanciada
# cc1 = ContaCliente(1, IOF, IR, 1000, taxarendimento)

cc2 = ContaComum(1, IOF, IR, 2000, taxarendimento)
cr1 = ContaRemunerada(1, IOF, IR, 2000, taxarendimento)

banco_1.adicionar_conta(cc2)
banco_1.adicionar_conta(cr1)

banco_1.calcular_rendimento_mensal()

banco_1.imprime_saldo_contas()