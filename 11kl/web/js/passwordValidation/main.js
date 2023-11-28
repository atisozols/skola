function validate(){
  const p = document.getElementById('password')
  if (/[A-Z]/.test(p.value)){
    const errorMessage = document.getElementById('err-msg')
    errorMessage.innerHTML = 'ir Lielais'
  }


}