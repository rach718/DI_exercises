
let root = document.getElementById('root');
let ul = document.createElement('ul');
root.appendChild(ul);


function addToList() {
	let item = prompt ("What would you like to add to your shopping list?");
	console.log(item);
	let li = document.createElement('li');
	let textNode = document.createTextNode(item);
	li.appendChild(textNode);
	ul.appendChild(li);
}

function clearAll(){
	ul.remove();
	ul = document.createElement('ul');
	root.appendChild(ul);
}
