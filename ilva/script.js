// class Helper {
//   getRandomInt(min, max) {
//     min = Math.ceil(min);
//     max = Math.floor(max);
//     return Math.floor(Math.random() * (max - min) + min);
//   }

//   getArrayOfRandomInt(){
//     let arr=[];
//     let counter = 0;
//     while(counter < 30){
//       let rnd = this.getRandomInt(0,200);
//       if (!arr.includes(rnd)){
//         arr[counter]= rnd;
//         counter++;
//       }
//     }
//     return arr;
//   }
// }

// class BstNode {
//   constructor(value){
//     this.value = value;
//     this.left = null;
//     this.right = null;
//     this.element = null;
//   }
// }

// class SelfBalancingBst {
//   constructor(nodeArray) {
//     this.nodeArray = nodeArray;
//     this.nodeRoot = null;
//     this.htmlRoot = document.getElementById("root")

//     this.build()
//   }

//   resetPathStyle() {
//     let elements = document.querySelectorAll('.tree div')
//     elements.forEach((element) => {
//       element.classList.remove('active')
//     })
//   }

//   search(value) {
//     this.resetPathStyle()
//     let start = this.nodeRoot
//     start.element.classList.add('active')

//     while (start !== null && start.value !== value) {
//       if (value >= start.value) {
//         start = start.right
//       } else {
//         start = start.left
//       }

//       if (start !== null)
//         start.element.classList.add('active')
//     }

//     if (start === null) {
//       this.resetPathStyle()
//       alert("Not found")
//     }

//     return start
//   }

//   insert(value) {
//     if (this.nodeArray.includes(value)) return
//     this.nodeArray.push(value)
//     this.build()
//   }

//   remove(value) {
//     if (!this.nodeArray.includes(value)) return
//     let index = this.nodeArray.indexOf(value);
//     if (index !== -1) {
//       this.nodeArray.splice(index, 1);
//     }
//     this.build()
//   }

//   sortNodes(){
//     this.nodeArray.sort((a,b)=>a-b);
//   }

//   build(){
//     this.sortNodes()

//     let start=0;
//     let end=this.nodeArray.length-1;
//     let root=Math.floor((start + end)/2);
//     this.nodeRoot = new BstNode(this.nodeArray[root]);

//     this.htmlRoot.innerHTML = ''
//     let dataHtml = document.createElement("div");
//     dataHtml.dataset.data = this.nodeArray[root]
//     dataHtml.innerHTML = `<span>${this.nodeArray[root]}</span>`;
//     this.htmlRoot.append(dataHtml)
//     this.nodeRoot.element = dataHtml

//     let minArray = this.nodeArray.slice(0, root);
//     let maxArray = this.nodeArray.slice(root+1);

//     let list = document.createElement("ul");
//     let leftItem = document.createElement("li");
//     list.append(leftItem);
//     this.nodeRoot.left = this.buildSubNode(minArray, leftItem)

//     let rightItem = document.createElement("li");
//     list.append(rightItem);
//     this.nodeRoot.right = this.buildSubNode(maxArray, rightItem)

//     this.htmlRoot.append(list);
//   }

//   buildSubNode(values, htmlRoot){
//     let start=0;
//     let end=values.length-1;

//     let root=Math.floor((start + end)/2);
//     let subNode = new BstNode(values[root]);

//     if (values.length <= 0) return subNode

//     let dataHtml = document.createElement("div");
//     dataHtml.dataset.data = values[root]
//     dataHtml.innerHTML = `<span>${values[root]}</span>`;
//     htmlRoot.append(dataHtml)
//     subNode.element = dataHtml

//     let minArray = values.slice(0, root);
//     let maxArray = values.slice(root + 1);

//     let list = document.createElement("ul");

//     if (minArray.length > 0) {
//       let leftItem = document.createElement("li");
//       subNode.left = this.buildSubNode(minArray, leftItem);
//       list.append(leftItem);
//     }

//     if (maxArray.length > 0) {
//       let rightItem = document.createElement("li");
//       subNode.right = this.buildSubNode(maxArray, rightItem);
//       rightItem.classList.add('right')
//       list.append(rightItem);
//     }

//     if (minArray.length > 0 || maxArray.length > 0)
//       htmlRoot.append(list);

//     return subNode;
//   }
// }

// let helper = new Helper()
// let balancingBst = new SelfBalancingBst(helper.getArrayOfRandomInt())

// console.log(balancingBst)
let valueArray = []

class TreeNode {
  constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
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
  if (!arr || arr.length === 0) {
      return null;
  }

  const root = new TreeNode(arr[0]);

  for (let i = 1; i < arr.length; i++) {
      insertIntoBST(root, arr[i]);
  }

  return root;
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


// Example usage:
populateArrayWithRandomInt()
const arr = valueArray
const root = createBSTFromArray(arr);

const treeContainer = document.getElementById('tree-container');
visualizeBST(root, treeContainer);

console.log(root)
