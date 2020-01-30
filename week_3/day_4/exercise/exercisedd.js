const root = document.getElementById('root');
let box = document.createElement('div');

		box.style.backgroundColor = "red";
		box.style.width = "50px";
		box.style.height = "50px";
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










