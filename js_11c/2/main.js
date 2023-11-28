more = document.getElementById("more")
more.style.display = "none"

function read_more(){
    // atlasīt elementus
    more = document.getElementById("more")
    dots = document.getElementById("dots")
    btn = document.getElementById("btn")

    if(more.style.display == "none"){
        // nomainīt stilojumu
        more.style.display = "inline"
        dots.style.display = "none"
        btn.innerHTML = "Read less"
    } else{
        // nomainīt stilojumu
        more.style.display = "none"
        dots.style.display = "inline"
        btn.innerHTML = "Read more"
    }
}

side = document.getElementById("side")

function side_menu(){
    if(side.classList.contains("opened")){
        side.classList.remove("opened")
    } else{
        side.classList.add("opened")
    }
}

stavoklis = 0

function switch_color(){
    elementi = document.getElementsByClassName("luksofors")

    krasas = [["red", "black", "black"],
              ["red", "yellow", "black"],
              ["black", "black", "green"],
              ["black", "yellow", "black"]]

    for(let i = 0; i < 3; i+=1){
        elementi[i].style.backgroundColor = krasas[stavoklis][i]
    }
    stavoklis += 1
    stavoklis = stavoklis % 4
}