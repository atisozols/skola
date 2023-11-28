const colorSet = [["red", "black", "black"],
                ["red", "orange", "black"],
                ["black", "black", "green"],
                ["black", "orange", "black"]];
                
let selected = 0
setState(selected)

function changeColor(){
    selected++
    setState(selected % 4)
}

function setState(selected){
    for(let i = 0; i < 3; i++){     
        const luks = document.getElementById('a' + i)
        luks.style.backgroundColor = colorSet[selected][i]
    }
}

// function setState(selected){
//     const stopLights = document.getElementsByClassName('luksofors')
//     for(let i = 0; i < 3; i++){
//         stopLights[i].style.backgroundColor = colorSet[selected][i]
//     }
// }





































// let selected = 0;
// setState(selected);

// function setState(selected){
//     for(let i = 0; i < 3; i++){     
//         const luks = document.getElementById('a' + (i+1))
//         luks.style.backgroundColor = colorSet[selected][i]
//     }
// }

// function changeColor(){
//     selected++ 
//     selected  %= colorSet.length
//     setState(selected)
// }

