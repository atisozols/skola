
function select_drink(){

    fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
        .then(response => response.json())
        .then(response => {
            header = document.getElementById("dname")
            header.innerHTML = response.drinks[0].strDrink
            console.log(response)
            img.src = ""
            img = document.createElement("img")
            img.src = response.drinks[0].strDrinkThumb
            document.body.append(img)
            for (let index = 1; index < 16; index++) {
                if(response.drinks[0]["strIngredient" + index]){
                document.createElement()
            }
            
        }
    
    })
        .catch(err => console.error(err));
}

