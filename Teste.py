from Cliente import Cliente
from Conta import Conta
from ContaPoupanca import ContaPoupanca
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")

conta1 = Conta([cliente1, cliente2], 1)
conta1.depositar(2000)

contapoupanca1 = ContaPoupanca(0.1)

contaremunerada1 = ContaRemuneradaPoupanca(0.5, cliente1, 707, 5.99)
contaremunerada1.depositar(1000)
print('Valor inicial da conta remunerada:')
contaremunerada1.gerar_extrato()
contaremunerada1.remuneraConta()
print('\nResultado de uma conta remunerada em um mês\nTaxa de remuneração: 0.5 ao dia\nTaxa de manutenção: 5.99 ao mês\n')
contaremunerada1.gerar_extrato()