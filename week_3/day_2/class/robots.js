console.log(robots);
function myButton (){
	let elem = document.getElementById('root');
	elem.classList.add ('box-grid');

	for (robot of robots){
		let box = document.createElement("div");
		let name = document.createElement("h2");
		let image = document.createElement("img");
		let username = document.createElement("h2");
		let email = document.createElement("p");
		elem.appendChild(box);

		image.setAttribute('src',"https://robohash.org/" + robot.id + "?size=200x200");

		box.appendChild(image);
		box.appendChild(name);
		box.appendChild(username);
		box.appendChild(email);

		name.innerText = robot.name;
		username.innerText = robot.username;
		email.innerText = robot.email

		box.classList.add ('box');
		box.classList.add ('box-center');
		




		// console.log(robot.id);
		// console.log(robot.name);
		// console.log(robot.username);
		// console.log(robot.email);
	}
}
function myToggle() {
    let list = document.getElementsByClassName('box');
    for (item of list){
    	item.classList.toggle('box-red');
    }
}

























// // console.log(robots);
// let elem = document.getElementById("root");
// console.log (elem);
// root.className ="box-grid"

// function myButton () {
// // 	for (robot of robots){
// // 		console.log(robot);
// // 		let div = document.createElement('div');
// // 		let  = document.createElement ('id')
// // 	}
// }

// const creatRobots1= ()=> {
// 	console.log (robots);
// 	robots.forEach(item =>{
// 		let box = document.creatElement('div');
// 		let image = document.creatElement('img');
// 		let name = document.creatElement('h2');
// 		let username = document.creatElement('h3');
// 		let email = document.creatElement('p');

		
// 		image.setAttribute('src',"https://robohash.org/" + item.id + "?size=200x200");
// 		name.innerText = item.name;
// 		username.innerText = item.username;
// 		email.innerText = item.email;

// 		box.appendChild(image);
// 		box.appendChild(name);
// 		box.appendChild(username);
// 		box.appendChild(email);

// 		box.classList.add('box');
// 		root.appendChild(box);

// 		// console.log(item.id);
// 		// console.log(item.name);
// 		// console.log(item.username);
// 		// console.log(item.email);
// 		})
// }







// let elem = document.querySelector('#');
// const toggleme = () => {
//   let ul = document.createElement('ul');
//   let li1 = document.createElement('li');
//   let li2 = document.createElement('li');
//   let li3 = document.createElement('li');
//   li1.innerText = 'option 1';
//   li2.innerText = 'option 2';
//   li3.innerText = 'option 3';
//   ul.appendChild(li1);
//   ul.appendChild(li2);
//   ul.appendChild(li3);
//   header.appendChild(ul)
// }