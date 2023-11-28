let guess_element = document.getElementById("character");
const word_element = document.getElementById("input");
let word = ''
let guessedLetters = [];

const alphabet = 'abcdefghijklmnopqrstuvwxyz'
const button_div = document.getElementById('alphabet')
for(const letter of alphabet){
    const button = document.createElement('button')
    button.innerHTML = letter
    button.onclick = function(){
        hangman(letter)
    }
    button_div.append(button)
}



function readValue(){
    guessedLetters = []
    const congrats_element = document.getElementById('congrats')
    congrats_element.style.display = 'none'

    word = word_element.value
    if(word.length > 0){
        guessedLetters.push(word[0])
    }
    update()
}

function update(){
    let output = ''
    for(char of word){
        if(guessedLetters.includes(char)){
            output += char
        }
        else{
            output += '+'
        }
    }
    document.getElementById('field').innerHTML = output

    if(output == word){
        const congrats_element = document.getElementById('congrats')
        congrats_element.style.display = 'block'
    }
}

function hangman(guess){
    // const guess = guess_element.value
    if(guess.length > 0){
        guessedLetters.push(guess[0])
    }
    update()
    guess_element.value = ''
}









































// input.addEventListener("keyup", function(event) {
//     if (event.code === "Enter") {
//         event.preventDefault();
//         document.getElementById("btn").click();
//   }
// });

// function setValue(){
//     value = document.getElementById("input").value;
//     document.getElementById("congrats").style.display = "none";
//     known = []
//     const field = document.getElementById("field");
//     field.innerHTML = "";
//     console.log(value);
//     known.push(value[0]);
//     updateValue();
// }

// function updateValue(){
//     const field = document.getElementById("field");
//     field.innerHTML = "";
//     for(let i = 0; i < value.length; i++){
//         let match_count = 0;
//         for(const c of known){
//             if(c === value[i]){
//                 match_count++;
//                 field.innerHTML += c;
//             }
//         }
//         if(match_count === 0){
//             field.innerHTML += " _ ";
//         }
//     }
// }

// function addBukva(){
//     let char = document.getElementById("character").value
//     if(char.length === 1){
//         if(!known.includes(char)){   
//             known.push(char);
//         }
        
//         updateValue();
//         document.getElementById("character").value= '';

//         if(!field.innerHTML.includes("_")){
//             document.getElementById("congrats").style.display = "inline"
//         }
//     }
//     else{
//         console.log('not ok')
//     }
// }