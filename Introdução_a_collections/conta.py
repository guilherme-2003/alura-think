class Conta:
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return f'[>>Codigo {self._codigo} Saldo {self._saldo}<<]'

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo += 1.01
        self._saldo -= 3