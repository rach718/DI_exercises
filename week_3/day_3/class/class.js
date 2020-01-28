const root = document.getElementById('root');
const p = document.getElementById('ptext');
root.classList.add("box");

const body = document.getElementsByTagName('body')[0];

p.addEventListener('mouseenter', function (e){
	createPTag();
})
function createPTag(){
	let p = document.createElement('p');
	p.innerText = '12345';
	body.appendChild(p);
} 

root.setAttribute('draggable','true');//if set to false, cant drag)
root.addEventListener("dragend", function(e){
	let x = e.clientX; //coordinate of x on the screen, left of screen//
	let y = e.clientY; //coordinate of y on the screen, y is the top
	root.style.left = x + 'px';
	root.style.top = y +'px';//if change the css .box to top:50px and left:50 px, itll vhange the position//
	console.log (x, y);
})

p.addEventListener('mouseenter', function(e){
	// root.style.background = 'green'; //line 4 and 5 do the same thing.
	changeColor('green', e.target);
})

p.addEventListener('mouseleave', function(e){
	changeColor('red', e.target);
});

root.addEventListener('mouseenter', function(e){
	// root.style.background = 'green'; //line 4 and 5 do the same thing.
	changeColor('green', e.target);
})

root.addEventListener('mouseleave', function(e){
	changeColor('red', e.target);
})
root.addEventListener('mouseup', function(e){
	changeColor('blue', e.target);
})
root.addEventListener('mousedown', function(e){
	changeColor('yellow', e.target);
})

//one function will do the job!//
function changeColor(color,elem){
 elem.style.background = color;
};


// // function mouseOut() {
//   document.getElementById("box").style.color = "red";
// }

// document.getElementById("box").addEventListener("mouseover", mouseOver);

// document.getElementById("box").addEventListener("mouseout", mouseOut);

// let but  =document.createElement('button');
// but.innerText = 'Click';
// but.setAttribute('class', 'name');
// // but.addEventListener('click',function(alertclick){
// // 	alertclick.target.innerText = "click me"
// // });

// let inp = document.creatElement('input');
// inp.setAttribute('type','text');
// inp.setAttribute('placeholder', 'enter your email');
// inp.setAttribute('id','emailInput');
// console.log(inp);

// butt.addEventListenter('click', function(e){ //value, whatever is inside the bar//
// console.log(e);
// let myInput = document.getElementById('emailInput');
// console.log(myInput.value);
// console.log(myInput);
// })

// rootDiv.appenchild(inp);
// rootDiv.appenchild(but);

// inp.addEventListener('keypress', function(enter){
// 	if (enter.keyCode==13){
// 	// 	enter.target.value = "";
// 		validate(enter.target.value);//validate is calling a differnet funcion//
// 		console.log(this.target.value);
// 		}
// 	})
	
// const validate = (val) =>{
// 	if(val.trim().length ==0){ //trim=trims spaces from a string//
// 		alert('pls enter a valid email');
// 	} 	else{
// 		alert('your email is' + 'val');
// 		}
// 	}


// but.addEventListener('click', function(event){
// 	e.target.innerTExt = 'Click Meeeee!'}); 
	// console.log (e.target);
	// console.log(e.click);
	// console.log(e);//all the methods in the event that was triggered//
	//event, and then function I'm calling, or create a function inside my event listener//
//every function in listener has its own event//
// console.log(event);
// rootDiv.appendChild('Div');
//i trigger onclick, in console ill see everything of the event. type of event, the target, in this case button, we can see everything.//

// let int =document.creatElement('input';)

// but.addEventListener('click', function(event){
// // e.target.innerTExt = 'Click Meeeee!'}); 
// rootDiv.appendChild('Div');

// add a listener to the input and console log the value



