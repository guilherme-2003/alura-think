var a = [1, 2, 3]
var b = [3, 2, 1]

let text = ""

let pedro = 0
let paulo = 0

for(i=0; i < a.length; i++){
    if(a[i] > b[i]){
        pedro++
    }
    else if(a[i] < b[i]){
        paulo++
    }
}
text += `Pedro: ${pedro}, Paulo: ${paulo}\n`

function createFile(text){
    fileSystem.writeFile('sample.txt', text, error => {
        if(error) throw error
        console.log("Data was written successfully")
    })
}

createFile(text)