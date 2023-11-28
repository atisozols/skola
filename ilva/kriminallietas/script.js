let valueArray = []

class TreeNode {
  constructor(value, left = null, right = null) {
      this.value = value;
      this.left = left;
      this.right = right;
  }
}

function populateArrayWithRandomInt(){
  let counter = 0;
  while(counter < 30){
    let rnd = this.getRandomInt(0,200);
    if (!valueArray.includes(rnd)){
      valueArray[counter]= rnd;
      counter++;
    }
  }
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

function insertIntoBST(root, value) {
  if (!root) {
      return new TreeNode(value);
  }

  if (value < root.value) {
      root.left = insertIntoBST(root.left, value);
  } else {
      root.right = insertIntoBST(root.right, value);
  }

  return root;
}

function createBSTFromArray(arr) {
  if (arr.length===0) return null;
  if (arr.length===1) return new TreeNode(arr[0]);
  const mid = Math.floor(arr.length / 2);
  const left = createBSTFromArray(arr.slice(0, mid));
  const right = createBSTFromArray(arr.slice(mid+1));
  return new TreeNode(arr[mid], left, right);
}

function insertValue(value){
  if(!valueArray.includes(value)){
    valueArray.push(value)
    const root = createBSTFromArray(valueArray);
    const treeContainer = document.getElementById('tree-container');
    treeContainer.innerHTML = ''
    visualizeBST(root, treeContainer);
  }
}

function deleteValue(value){
  if(valueArray.includes(value)){
    const newArray = []
    for(element of valueArray){
      if(element != value){
        newArray.push(element)
      }
    }

    valueArray = newArray
    const root = createBSTFromArray(valueArray);
    const treeContainer = document.getElementById('tree-container');
    treeContainer.innerHTML = ''
    visualizeBST(root, treeContainer);
  }
}
 // !!! Sabalanset koku, sakartojot to
 
let searchPath=[]; //Sagalbā index, caur kuriem meklē target

function search(arr,target) {
  let left=0;
  let right=arr.length-1;
  searchPath = []; //notīra searcpath
  while (left<=right) { //Loop till left is less or equal to right
    let mid=Math.floor((left+right)/2); //Divide uz pusēm, jo vienā pusē būs target
    searchPath.push(mid); //pievieno mid iekš searchPath
    console.log(arr[mid],target);

    //  !!! NENNOSTRĀDĀ :(
    if (arr[mid]===target){
      highlight(searchPath); //iekrāso, kad atrodi
      return mid; // Ja mid elements, ir tas ko meklē, atgriez index
    }
    else if (arr[mid]>target) { //Ja mid ir mazāks par target, tad target ir right pusē no mid
      left=mid+1; //left norāde | +1, lai neskatās uz min
    }
    else {
      right=mid-1;
    }
  }
}

// !!! HIGHLIGHTS only target
function highlight(searchPath) {
  console.log(searchPath);
  const allNodes=document.querySelectorAll('.node');//notīrīt veco highlight
  allNodes.forEach(node=>node.classList.remove('highlight'))

  //Izveidot jaunu highlight ceļu
  searchPath.forEach(index=> {
    const nodeTohighlight=document.getElementById('node-${index}');
    if (nodeTohighlight) {
      nodeTohighlight.classList.add('highlight');
    }
  });
}


function visualizeBST(root, container, side='left') {
  if (!root) {
      return;
  }

  // Create a new node element
  const nodeElement = document.createElement('div');
  nodeElement.className = 'node' + ' ' + side;
  nodeElement.innerText = root.value;

  // Append the node to the container
  container.appendChild(nodeElement);
  const nodeChildren = document.createElement('div');
  nodeChildren.className = 'children'
  nodeElement.append(nodeChildren)

  setTimeout(() => {
    visualizeBST(root.left, nodeChildren, 'left');
    visualizeBST(root.right, nodeChildren, 'right');
  }, 1000);

  // Recursively visualize left and right subtrees
  
}

populateArrayWithRandomInt()
const arr = valueArray
const root = createBSTFromArray(arr);

const treeContainer = document.getElementById('tree-container');
visualizeBST(root, treeContainer);

console.log(root)
