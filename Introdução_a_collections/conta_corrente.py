class ContaCorrente:
    def __init__(self, codigo) -> None:
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self) -> str:
        return f'[>>Codigo {self.codigo} Saldo {self.saldo}<<]'