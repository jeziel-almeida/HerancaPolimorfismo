from Cliente import Cliente
from Conta import Conta
from ContaEspecial import ContaEspecial

cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
cliente3 = Cliente("789", "Joana", "Rua H")

conta1 = Conta([cliente1, cliente2], 10)
conta1.depositar(2000)

conta2 = ContaEspecial([cliente3], 20, 2000)
conta2.depositar(1000)
conta2.depositar(100)
conta2.sacar(3200)

conta2.sacar(3000)
conta2.extrato.extrato(conta2.numero)