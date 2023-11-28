const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
		'X-RapidAPI-Host': 'edamam-food-and-grocery-database.p.rapidapi.com'
	}
};

foods = 0

function calories(){
    foodName = document.getElementById("foodName").value
    weight = document.getElementById("weight").value
    fetch('https://edamam-food-and-grocery-database.p.rapidapi.com/parser?ingr=' + foodName, options)
        .then(response => response.json())
        .then(response => {
            console.log(response)
            kcal = response.parsed[0].food.nutrients.ENERC_KCAL
            foods += (kcal * weight)/100
            document.getElementById("output").innerHTML = foods
            list_item = document.createElement("li")
            list_item.innerHTML = foodName
            document.getElementById("list").append(list_item)
        })
        .catch(err => console.error(err));
}