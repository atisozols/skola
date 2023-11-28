console.log('cau')
const x = 3
const array = [1, 6, 3, 8, 3, 8, 9]
const sv = "Atis Ozols"


// if(x == 3){
//   console.log('ok')
// } else if(x > 6){
//   console.log('ok1')
// } else{
//   console.log('ok2')
// }

// for(const elem of array){
//   console.log(elem)
// }

// for(let i = 4; i <= 100; i = i * 2){
//   console.log(i)
// }

// let i = 0
// while(i < 10){
//   console.log(i++)
// }

// function manaFunkcija(m){
//   for(const elem of m){
//     console.log(elem)
//   }
// }

// a = [4, 7, 2]

// manaFunkcija(array)

const paragrafs = document.createElement("p")
// let firstName = 'Jānis'
document.body.append(paragrafs)
// paragrafs.innerHTML = 'sveiki, <strong>' + firstName + '</strong>'

// let teksts = ''
// for(const elem of array){
//   teksts = teksts + elem + ' '
// }

// const cipari = document.createElement("p")
// cipari.innerHTML = teksts
// document.body.append(cipari)

let vechi = ['Oskars', 'Kristofers', 'Mārcis', 'Vlass', 'Verners', 'Dmitrijs', 'Danils']

// izveidojam saraksta(<ol>) elementu, 
// lai aizpildītu to ar vārdiem no masīva
const sarakstaElements = document.createElement('ol')
document.body.append(sarakstaElements)

let i = 0
// ņemam katru vērtību no masīva
for (const person of vechi){
  // izveidojam tai <li> elementu
  const listItem = document.createElement('li')

  // ierakstām <li> elementā tekstu
  listItem.innerHTML = person

  // pievienojam gatavo <li> elementu 
  // parent elementam 'sarakstaElements', jeb <ol> elementam
  sarakstaElements.append(listItem)
  // setTimeout(() => {
  //   sarakstaElements.append(listItem)
  // }, i * 1000)
  // i++
}

const textElements = document.getElementsByClassName('text')

for (const textElement of textElements){
  textElement.classList.add('red')
  console.log(textElement.classList)
}

// 0 1 2 3 4 5 6
// let i = 0
// function onPress(){
//   paragrafs.innerHTML = i
//   i++
// }
