let dropdowns = document.getElementById("select")
colors = ["red", "green", "blue", "orange"]


colors.forEach(color => {
    // izveido option elementu
    option_element = document.createElement("option")

    // iedod elementam vērtības
    option_element.value = color
    option_element.innerHTML = color

    // elementu pievieno parent elementam ar append
    dropdowns.append(option_element)
});



function setBg(){
    i = dropdowns.selectedIndex
    document.body.style.backgroundColor = dropdowns.options[i].value
}

// pārbaudīt, vai parole satur lielo burtu, mazo un simbolu
// kā arī ir garumā vismaz 8
function validate(){
    input_el = document.getElementById("passw")
    let password = input_el.value
    liel_sk = 0
    maz_sk = 0
    simb_sk = 0

    for(let i = 0; i < password.length; i += 1){
        if(password.charCodeAt(i) > 96 && password[i].charCodeAt() < 123){
            maz_sk += 1
        }
        if(password.charCodeAt(i) > 64 && password[i].charCodeAt() < 91){
            liel_sk += 1
        }
        if(password.charCodeAt(i) > 32 && password[i].charCodeAt() < 65){
            simb_sk += 1
        }
    }
    if(liel_sk > 0 &&
         maz_sk > 0 &&
          simb_sk > 0 &&
           password.length > 7){
             document.getElementById("msg").innerHTML = "Password set!"
             document.getElementById("msg").style.color = "black"
           } else{
            document.getElementById("msg").innerHTML = "Password doesn't meet the requirements!"
            document.getElementById("msg").style.color = "red"
        }
}