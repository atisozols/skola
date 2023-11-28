// const options = {
// 	method: 'GET',
// 	headers: {
// 		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
// 		'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
// 	}
// };

// fetch('https://free-nba.p.rapidapi.com/teams?page=0', options)
// 	.then(response => response.json())
// 	.then(response => {
//         console.log(response)
//         response.data.forEach(team => {
//             optionElem = document.createElement('option')
//             optionElem.value = team.id
//             optionElem.innerHTML = team.full_name
//             document.getElementById("teams").append(optionElem)
//         });
//     })
// 	.catch(err => console.error(err));

accessToken = "BQALicUfwaiMPf3jB-Tv0n96518vuRjb0enNxRFfxX2KzkTnGroZHIYUt90E9n_bSxdNIpYG0PYdVSVOX3-ZUxHbRAz2fEc5aYvt1gRm1I7aQN5eUN_XaSR0jeJxnyY6wRGhsJLVPJtcsJ7JY0cHLfixkABv3tsfWXYofQqu41PY07xf0qYG5ekx-TcIB-c5YuPiI1YjPSfuR53XqPFpLSNSyLVGaK4RAx2fbqmAolN5xOAaXA"
fetch('https://api.spotify.com/v1/playlists/3BlPvZMg0ZaxOROrYKUwqC', {
            method: 'GET', headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + accessToken
            }
        })
            .then((response) => {
                console.log(response.json().then(
                    (data) => { console.log(data) }
                ));
            });
            

// https://open.spotify.com/user/11139812797?si=0da8f64f775e41cb