let container = document.getElementById('container');
let animate = document.getElementById('animate');
let btn = document.getElementById('button');
btn.addEventListener('click', myMove);


function myMove(){
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



