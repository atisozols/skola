const options = {
	method: 'GET',
	headers: {
		Accept: 'application/hal+json',
		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
		'X-RapidAPI-Host': 'matchilling-tronald-dump-v1.p.rapidapi.com'
	}
};



function display_quote(){
    fetch('https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote', options)
        .then(response => response.json())
        .then(response => {
            document.getElementById("text").innerHTML = response["value"]
        })
        .catch(err => console.error(err));
}