function createMeme(){
    topText = document.getElementById('top')
    bottomText = document.getElementById('bottom')
    nameText = document.getElementById('name')

    console.log(topText.value, bottomText.value)

    image = document.getElementById("meme")
    image.src = "https://apimeme.com/meme?meme=" + nameText.value + "&top=" + topText.value + "&bottom=" + bottomText.value


}