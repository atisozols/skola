const x = document.getElementById("laukums")

const a = 3
const b = 4
for(let i = 0; i < 8; i++){
    for(let j = 0; j < 8; j++){
        if(i + j === a + b || i - j === a - b || i === a || j === b){
            x.innerHTML += "1 "
        } else {
            x.innerHTML += "0 "
        }
    }
    x.innerHTML += "<br>"
}