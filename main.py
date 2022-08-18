from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

cliente = Cliente("José das Couves", "123.456.789-10", "Aspone")
# print("Cliente de\n nome {},\n CPF {},\n profissão {},\n".format(cliente.nome, cliente.cpf, cliente.profissao))
# #pprint(cliente.__dict__, width = 40)
# cliente.idade = 20
# print("idade {}".format(cliente.__dict__["idade"]))

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self,value):
        if not isinstance(value, int):
            raise ValueError("O valor digitado é do tipo {}. \nO campo agência só pode ter valores de números inteiros.".format(type(value)))
        if value <= 0:
            raise ValueError("a agência deve ser maior que zero")

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self,value):
        if not isinstance(value, int):
            raise ValueError("O valor digitado é do tipo {}. \nO campo número só pode ter valores de números inteiros.".format(type(value)))
        if value <= 0:
            raise ValueError("o número deve ser maior que zero")

        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("o Saldo deve ter valor inteiro")
            return
        if value < 0:
            print("o saldo deve ser maior ou igual a zero")
            return
        self.__saldo = value

    def transferir(self, valor, favorecido, depositario):
        depositario.sacar(valor)
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self):
        self.saldo += valor

def main():
    import sys

    contas = []

    while True:
        try:
            nome = input("Nome do Cliente:\n")
            agencia = int(input("Número da Agencia:\n") )
            numero  = int( input("Número da Conta Corrente\n") )
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)} conta(s) criada(s)')
            sys.exit()


if __name__ == '__main__':
    main()

