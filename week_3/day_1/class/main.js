
// let elem = document.getElementById('content');
// console.log(elem.firstElementChild);
// console.log(elem.firstChild);
// console.log(elem.lastElementChild);
// console.log(elem.lastChild);

// console.log(elem.nextElementSibling);
// console.log(elem.nextSibling);

// console.log(elem.previousElementSibling);
// console.log(elem.previousSibling);
// console.log(elem.parentNode);
// console.log(elem.childNodes);


// let elem = document.getElementById('header');
// console.log(elem.parentNode);
// console.log(elem.childNodes); //(elem.children) gives u just the elements.

// let elem = document.getElementById('header');
// for (var i = 0; i <elem.children.length; i++) {
// 	 console.log(elem.children[i].innerText);
// }
// for (var i = 0; i <elem.children.length; i++) {
// 	 elem.children[i].innerText = i + " haha";
// } //CAN CHANGE TEXT OF A NODE


// if i want node name console.log(elem.firstchild.nodeName)

// inner.html gives you the html, and inner.text just gives u text without tags.

// Method	Description
// document.createElement(element)	Create an HTML element
// document.removeChild(element)	Remove an HTML element
// document.appendChild(element)	Add an HTML element
// document.replaceChild(new, old)	Replace an HTML element
// document.write(text)	Write into the HTML output stream





// let elem = document.getElementById('content');
// elem.setAttribute ('width', '100')
// console.log(elem);

// let div1 = document.getElementById('page');
// let att = div1.getAttribute('ziv');
// console.log(att);
// div1.setAttribute('ziv', "ggg"); //setAttribute changes attribute

// let elem = document.getElementById('title');
// console.log (elem.innterText); //get the text

// let elem = document.getElementById('content');
// let myH1 = document.createElement('h1')
// myH1.innterText = "whatever i want";
// elem.appendChild(myH1);


// let elem = document.getElementById('content');
// let arr = {'ziv', 'sara', 'rachel'}
// for (var i = 0; i <arr.length; i++) {
// 	let user = document.createElement('h4') //can put any element youd like to add to html
// 	user.innterText = arr[i] //or "ziv";
// 	elem.appendChild(myH1);
// }

