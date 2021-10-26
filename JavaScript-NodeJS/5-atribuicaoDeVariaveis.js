console.log('Trabalhando com atribuição de variáveis')

const primeiroNome = "Guilherme"
const sobrenome = "Paulela"

console.log(primeiroNome, sobrenome)
console.log(`Meu nome é ${primeiroNome} ${sobrenome}`)

//nome =  nome + sobrenome
// erro porque o const significa constante, logo, o valor da variável não pode mudar

let contador = 0
contador = contador + 1

const nomeCompleto = primeiroNome + sobrenome
console.log(nomeCompleto)

let idade
idade = 17
idade = idade + 1
console.log(idade)