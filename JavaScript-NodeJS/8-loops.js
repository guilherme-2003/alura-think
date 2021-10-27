console.log(`Trabalhando com condicionais`)
const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`,
)

const idadeComprador = 20
const estaAcompanhada = true
let temPassagemComprada = false
const destino = 'Salvador'
let destinoExiste = false

console.log("Destinos possíveis:")
console.log(listaDeDestinos)

const podeComprar = idadeComprador >= 18 || estaAcompanhada == true

let contador  = 0
while(contador < 3){
    if ((listaDeDestinos[contador]) == destino){
        destinoExiste = true
        break
    }
    contador += 1
}

console.log("Destino existe: ", destinoExiste)

if(podeComprar && destinoExiste){
    console.log("Boa Viagem!")
}else{
    console.log("Desculpe, houve um erro!")
}

for(let i = 0;i< 3 ;cont = i++){
    if(listaDeDestinos[contador] == destino){
        destinoExiste = true
    }
}