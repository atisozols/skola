// kā piekļūstam HTML elementiem, izmantojot JS, 
//kā nomainām elementu tekstuālo saturu vai stilojumu

const title = document.getElementById("virsraksts")

title.innerHTML = "<i>Čau</i>"
title.style.color = "blue"
title.style.backgroundColor = "red"
 
// kā izveidojam elementus, 
 
const p_elements = document.createElement("p")
p_elements.innerHTML = "Atis Ozols"
document.body.append(p_elements)

//parent elementa izveide
const saraksts = document.createElement("ul")

// pirma li elementa izveide
const elem1 = document.createElement("li")
elem1.innerHTML = "Marcis Misencnkovns"

// otra li elem izveide
const elem2 = document.createElement("li")
elem2.innerHTML = "Deivids"

// pievienosana sarakstam
saraksts.append(elem1)
saraksts.append(elem2)

//saraksta pievienosana html
document.body.append(saraksts)


// pogas un funkciju palaišanu, 
// nospiežot pogu

let skaits = 0
const count = document.getElementById("count")
count.innerHTML = skaits

function plusOne(){
    skaits += 1
    count.innerHTML = skaits
}