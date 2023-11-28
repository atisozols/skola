const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'b79e23c4a3msh6af2ad981a763dcp1b5e4djsn5c5224e04e76',
		'X-RapidAPI-Host': 'edamam-food-and-grocery-database.p.rapidapi.com'
	}
};


function calories(){
    foodName = document.getElementById('foodName').value
    fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + foodName)
    .then(response => response.json())
    .then(response =>{
        response.drinks.forEach(drink => {
            console.log(drink.strDrink)
        });

        
        recepte = document.getElementById('recept')
        recepte.innerHTML = response.drinks[0].strDrink
        pagatavosana = document.getElementById('pagatavosana')
        pagatavosana.innerHTML = response.drinks[0].strInstructions
        ingredients = document.getElementById('ingr')
        ingredients.innerHTML = response.drinks[0].strIngredient1
        talak  = document.getElementById('ige')
        talak.innerHTML = response.drinks[0].strIngredient2
        talaks  = document.getElementById('ig')
        talaks.innerHTML = response.drinks[0].strIngredient3
        talakss  = document.getElementById('i')
        talakss.innerHTML = response.drinks[0].strIngredient4
        talaksss  = document.getElementById('is')
        talaksss.innerHTML = response.drinks[0].strIngredient5
        talakssss  = document.getElementById('il')
        talakssss.innerHTML = response.drinks[0].strIngredient6

        document.getElementById("attels").src = response.drinks[0].strDrinkThumb
        console.log(response.drinks)})
    .catch(err => console.error(err));
}
