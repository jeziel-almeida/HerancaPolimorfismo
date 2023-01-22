from Cliente import Cliente
from Conta import Conta
from ContaPoupanca import ContaPoupanca
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")

conta1 = Conta([cliente1, cliente2], 1)
conta1.depositar(2000)

contapoupanca1 = ContaPoupanca(0.1)

contaremunerada1 = ContaRemuneradaPoupanca(0.1, cliente1, 5)
contaremunerada1.depositar(1000)
contaremunerada1.remuneraConta()
contaremunerada1.gerar_extrato()