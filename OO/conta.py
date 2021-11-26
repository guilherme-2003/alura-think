class Conta:

    def __init__(self, numero, titular, saldo, limite): 
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de $ {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_do_saque):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_do_saque <= valor_disponivel_para_saque 

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor de R$ {valor} ultrapassou o limite de R$ {self.__limite}")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_do_banco():
        return '001'

    @staticmethod
    def codigo_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}