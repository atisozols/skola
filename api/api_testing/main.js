const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
		'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
	}
};

function calculate(){
    male = document.getElementById("male").value
    female = document.getElementById("female").value

    fetch('https://love-calculator.p.rapidapi.com/getPercentage?sname='+ male +'&fname=' +female, options)
	.then(response => response.json())
	.then(response => {
        console.log(response)
        document.getElementById('result').innerHTML = response['percentage'] + '%'
        document.getElementById('recom').innerHTML = response['result']
    })
	.catch(err => console.error(err)); 
}