class Programa:
    def __init__(self, nome, ano) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome}\n - Ano: {self.ano}\n - Likes: {self._likes}\n'

class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)        
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome}\n - Ano: {self.ano}\n - Duração: {self.duracao} min\n - Likes: {self._likes}\n'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome}\n - Ano: {self.ano}\n - Temporadas: {self.temporadas}\n - Likes: {self._likes}\n'

class Playlist:
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()  
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana:
    print(programa)