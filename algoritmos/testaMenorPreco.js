var precos = []
var produtos = []
produtos[0] = new Produto("Lamborghini", 1000000)

maisBarato = 0
for(atual = 0; atual <= 4; atual++){
    if(produtos[atual] < precos[maisBarato])
    maisBarato = atual
}

console.log(maisBarato)
console.log("O caror mais barato custa R$" + precos[maisBarato])
