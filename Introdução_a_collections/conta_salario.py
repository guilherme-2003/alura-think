from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro) -> bool:
        return self._codigo == outro._codigo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return f'[>>Código {self._codigo} Saldo {self._saldo}<<]'