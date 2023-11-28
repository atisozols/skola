fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
        .then(response => response.json())
        .then(response => {
            console.log(response)

            header = document.getElementById("name")
            header.innerHTML = response.drinks[0].strDrink

            img = document.getElementById("imag")
            img.src = response.drinks[0].strDrinkThumb

            desc = document.getElementById("desc")
            desc.innerHTML = response.drinks[0].strAlcoholic + " drink in a " + response.drinks[0].strGlass

            for (let index = 1; index < 16; index++) {
                if(response.drinks[0]["strIngredient" + index]){
                    li = document.createElement("li")
                    li.innerHTML = response.drinks[0]["strIngredient" + index]
                    document.getElementById("list").append(li)

                }
            }
        })
        .catch(err => console.error(err));

        