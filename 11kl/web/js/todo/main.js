let i = 0

function add_item(){
  const inputValue = document.getElementById('todo_item').value
  
  const listItem = document.createElement('li')
  listItem.setAttribute('id', 'item' + i.toString());
  listItem.innerHTML = inputValue + "<button onclick='remove_item(" + i + ")'>Remove</button>"
  i++

  const list = document.getElementById('todo')
  list.append(listItem)

  document.getElementById('todo_item').value = ''
}

function remove_item(index){
  const listItem = document.getElementById('item' + index.toString())
  listItem.remove()
}

function clear_list(){
  const list = document.getElementById('todo')
  list.innerHTML = ''
}