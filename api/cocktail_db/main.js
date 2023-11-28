function search_drink(){
  drink = document.getElementById("drink").value

  fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drink)
    .then(response => response.json())
    .then(response => {
      drinks = response.drinks

      drinks.forEach(drink => {
        console.log(drink)
        title = document.createElement("h3")
        title.innerHTML = drink.strDrink
        document.body.append(title)

        image = document.createElement("img")
        image.src = drink.strDrinkThumb
        image.style = "height: 100px"
        document.body.append(image)

        list = document.createElement("ul")
        for(let i = 1; i < 16; i++){
          key = "strIngredient" + i.toString()
          key2 = "strMeasure" + i.toString()
          if(drink[key]){
            list_item = document.createElement("li")
            list_item.innerHTML = drink[key] + " " + drink[key2]
            list.append(list_item)
          }
        }
        document.body.append(list)
      });
    })
    .catch(err => console.error(err));
}