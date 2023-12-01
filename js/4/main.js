const cart = {}
let total = 0

function add_to_cart(product, price){
  total += price

  if (cart[product]){
    cart[product]++
  }else{
    cart[product] = 1
  }

  const cartElement = document.getElementById('cart')
  cartElement.innerHTML = ''

  const totalElement = document.getElementById('total')
  totalElement.innerHTML = '$' + Math.round(total * 100)/100

  for(product in cart){
    const listItem = document.createElement('li')
    listItem.innerHTML = product + ' ' + cart[product]
    cartElement.append(listItem)
  }


  
}