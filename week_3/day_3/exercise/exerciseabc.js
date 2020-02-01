const root = document.getElementById('root');
const abcs = 'abcdefghijklmnopqrstuvwxyz'.split('');
root.style.display = 'flex';
root.style.justifyContent = "space-between";

for (abc of abcs){
	let box = document.createElement("div");
	box.innerText = abc;
	box.style.border = "solid red";
	box.style.fontSize = "30px";
	box.style.padding = "10px";
	box.style.width = "15px";
	box.style.height = "30px";
	box.setAttribute('draggable','true');

	box.addEventListener("dragend", function(event){
		let x = event.clientX;
		let y = event.clientY;
		box.style.left = x + "px";
		box.style.top = y + "px";
		console.log (x, y);

	box.style.position ='absolute';
	})

	root.appendChild(box);

}


