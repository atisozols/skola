// and - &&; or - ||
let record = [0, 0, 0]
function rps(move){
  const computerMove = getRandomInt(3)
  // console.log("you played", move, "comp played", computerMove)
  const outputElement = document.getElementById('result')

  if(move == computerMove){
    outputElement.innerHTML = "Draw"
    record[1]++
  } 
  else if(
    (move == 0 && computerMove == 2) || 
    (move == 1 && computerMove == 0) ||
    (move == 2 && computerMove == 1)
    ){
      outputElement.innerHTML = "<strong>You won</strong>"
      record[0]++
    }
  else{
    outputElement.innerHTML = "You lost"
    record[2]++
  }
  const recordOutput = document.getElementById('record')
  recordOutput.innerHTML = record[0] + '-' + record[1] + '-' + record[2]	
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
