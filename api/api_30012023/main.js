const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
		'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
	}
};

function go(){
    cityName = document.getElementById("city").value

    fetch('https://weatherapi-com.p.rapidapi.com/forecast.json?q=' + cityName + '&days=3', options)
	.then(response => response.json())
	.then(response => {
        console.log(response)
        
        pElement = document.getElementById("teksts")
        pElement.innerHTML = response.current.condition.text + " in " + response.location.name

        for(let i = 0; i < 3; i = i + 1){
            console.log(i)
            // viena rinda, kurā būs divas šūnas
            rinda = document.createElement("tr")
            datums = document.createElement("td")
            laikapst = document.createElement("td")

            datums.innerHTML = response['forecast']['forecastday'][i]['date']
            laikapst.innerHTML = response.forecast.forecastday[i].day.avgtemp_c + " degrees, " + response.forecast.forecastday[i].day.condition.text

            // pievieno elementus rindai
            rinda.append(datums)
            rinda.append(laikapst)

            // rindu ieliek HTML tabulā
            document.getElementById("tabula").append(rinda)

            

        }
    })
	.catch(err => console.error(err));
}



    