const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
		'X-RapidAPI-Host': 'instagram-profile1.p.rapidapi.com'
	}
};

function setImage(image_url){
    document.getElementById("image").src = image_url
}

function getUserData(){
    username = document.getElementById("name").value

    fetch('https://instagram-profile1.p.rapidapi.com/getprofile/' + username, options)
        .then(response => response.json())
        .then(response => {
            console.log(response)
            setImage(response["profile_pic_url_hd"])
        })
        .catch(err => console.error(err));
}