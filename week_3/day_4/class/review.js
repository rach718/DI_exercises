let root = document.getElementById('root');
let h1 = document.createElement('h1');
let ul = document.createElement('ul');
let li1 = document.createElement('li');
let li2 = document.createElement('li');
let li3 = document.createElement('li');
let input1 = document.createElement('input');
let input2 = document.createElement('input');
let input3 = document.createElement('input');
let btn = document.createElement('button');
let p = document.createElement('p');

h1.innerText = "Mad Libs";
li1.innerText = "Name";
li2.innerText = "Adjective";
li3.innerText = "Verb";
btn.innerText = "Generate";



root.appendChild(h1);
root.appendChild(ul);
root.appendChild(btn);
ul.appendChild(li1);
ul.appendChild(li2);
ul.appendChild(li3);
li1.appendChild(input1);
li2.appendChild(input2);
li3.appendChild(input3);
root.appendChild(p);

	function generate(){
		if ((input1.value || input2.value || input3.value) !== ""){
		let span = document.createElement('SPAN');
		let sentence = document.createElement('p');
		sentence.innerText = "generate story:" + input1.value + " is " + input2.value + " and " + input3.value + " home"; 
		span.appendChild(sentence);
		root.appendChild(span)
	}
	}	
	
	btn.addEventListener('click', generate);