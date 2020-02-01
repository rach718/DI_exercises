let root = document.getElementById('root');
let h1 = document.createElement('h1');
let input = document.createElement('input');
let btn = document.createElement('button');
let btnClear = document.createElement('button')
let ul = document.createElement('ul');


h1.innerText = "Shopping List";
btn.innerText = "Add Item To List";
btnClear.innerText = "Clear All";

function item(){
	if (input.value !== " "){
		let li=document.createElement("li");
		li.innerText = input.value;
		console.log(item);
		ul.appendChild(li);	
	}
		input.value = ''; 
}	

	function clearAll(){
		ul.innerHTML = "";		
	}
	// function ClearAll(){
	// 	let allItems = document.querySelectorAll("li");
	// 	for (var i=0; i<allItems.length;i++){
	// 		allItems[i].remove();
	// 	}
	// } --
	
root.appendChild(h1);
root.appendChild(input);
root.appendChild(btn);
root.appendChild(btnClear);
root.appendChild(ul);

btn.addEventListener('click', item);
btnClear.addEventListener('click', clearAll);

// function clearAll(){
// 	ul.remove();
// 	ul = document.createElement('ul');
// 	}
// 	for (clear of ul){
// 	clear[i].remove();
// 	}
// }
	

	// for (itemToRemove of li){
	// 	itemToRemove.remove(itemToRemove.length-1);
	// }
 //        var itemToRemove = document.getElementById(li);
 //        itemToRemove.removeChild(itemToRemove.childNodes);


	
	// ul.remove();
	// ul = document.createElement('ul');
	// }
// create and item that selects all the li.

