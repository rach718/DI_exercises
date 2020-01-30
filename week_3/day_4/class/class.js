// const root = document.getElementById ('root');
// let btn = document.createElement ('button');
// btn.innerText = "click me!";

// btn.addEventListener('click', function(event){
// 	// 2 arguments in event listerner. (,)
// 	// console.log(event);
// 	// can add another function here - doSomething ()
// 	let body = document.getElementByTagName('body')[0];
// 	// console.log(body); //this is an array, that why add [0] after body. only one body on page, so we do it at index 0. its first element, and will return the body element.
// 	body.style.background ='red';
// })
// or another way:
// btn.addEventListener('click', function(event){
// 	changeColor()
// });
// another way
// btn.addEventListener('click', changeColor{

// function changeColor(){
// 	let body = document.getElementByTagName('body')[0];
// 	body.style.background ='red';
// }

// root.appendChild(btn);

const root = document.getElementById ('root');
const outer = document.createElement ('div');
const inner = document.createElement ('div');
let btn = document.createElement ('button');
btn.innerText = "click me!";
btn.addEventListener('click', myMove);

outer.classList.add("container");
inner.setAttribute('id','animate');


root.appendChild(btn);
root.appendChild(outer);
outer.appendChild(inner);

function myMove() { 
  var elem = document.getElementById("animate");
  var pos = 0;
  
  let timer = setInterval(function() {
    if (pos == 350) {
      clearInterval(timer);
    }
    else {
      pos++;
      elem.style.top = pos + "px";
      elem.style.left = pos + "px";
    }
  }, 5);
}



// function setTime(){
// 	setTimeout(function){
// 		console.log('hello');
// 		{,3000}
// 	}}


 // let id;
 // function setInter(){
 // 	id = setInterval(function(){
 // 		console.log('hello');
 // 	},1000);

 // }
 // function clearInter(){
 // 	clearInterval(id);
 // }

 // pos. absolute inner div-set 0 and change position
 // pos. relative outer div, top and left 0 and 0
