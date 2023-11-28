// x = 5
// if(x > 7){
//     console.log(1)
// } else{
//     console.log(0)
// }

// for(let i = 0; i < 10; i += 1){
//     console.log(i)
// }

// i = 0
// while(i < 10){
//     console.log(i)
//     i++ // tas pats, kas i += 1
// }

// function my_function(x){
//     console.log(x*x)
// }

// m = [5, 2, 6, 9, 1, 3]

// m.forEach(my_function);

// m.forEach(element => {
//     console.log(element)
// });

// elementu selectošana, iekšējās vērtības uzstādīšana
myElement = document.getElementsByClassName("tukss")[0]
console.log(myElement)
myElement.innerHTML = "<strong style=\"font-size: 72px\">caw</strong>"


// jaunu elementu izveide, ielikšana dokumentā
headerElement = document.createElement("h1")
headerElement.innerHTML = "Virsraksts"
myElement.append(headerElement)

// persons = ["Atis", "Mārtiņš", "Pēteris"]
// // table -> tr -> td


// // tabulas elem izveide
// tabula = document.createElement("table")

// // katram el no masīva persons
// persons.forEach(element => {

//     // izveidojam rindas elementu un šūnas elementu
//     rinda = document.createElement("tr")
//     shuna = document.createElement("td")

//     // pievienojam stilojumu
//     shuna.style.border = "solid"
//     // background-color -> backgroundColor 
//     shuna.style.backgroundColor = "cyan"
    
//     // ierakstām elementā personu
//     shuna.innerHTML = element

//     // pievienojam šūnu rindai un rindu ieliekam tabulā
//     rinda.append(shuna)
//     tabula.append(rinda)
// });
// document.body.append(tabula)

function krasasMaina(){
    if(myElement.style.backgroundColor == "green"){
        myElement.style.backgroundColor = "red"
    } else{
        myElement.style.backgroundColor = "green"
    }
}

/* <p>innerHTML</p> */
function palielinat(){
    sk = document.getElementById("skaitlis")
    sk.innerHTML = parseInt(sk.innerHTML) + 1
}

function change(){
    elem = document.getElementById("uzd1")
    // elem.style.fontWeight = "700"
    // elem.innerHTML = "<strong>" + elem.innerHTML + "</strong>"
    // classList
}