// // Daily Challenge Exercise;
// var fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// fruits.shift();
// {
// console.log(fruits)
// }

// var fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// fruits.sort();
// {
// console.log(fruits);
// }

// var fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// fruits.push ("kiwi");
// {
// console.log(fruits);
// }

// var fruits = ["Banana", "Apples", "Oranges", "Blueberries", "kiwi"];
// fruits.splice(1, 1);
// {
// console.log(fruits);
// }

// var fruits = ["Banana", "Apples", "Oranges", "Blueberries", "kiwi"];
// fruits.reverse();
// {
// console.log(fruits);
// }


// // Exercise 1:
// let x = prompt ("Please choose a number");
// console.log(Number(x)); //convert string that is a # by doing this
// console.log(x%2)
// if (x%2==0){
// 	console.log (x + "is an even number")
// }
// else {
// 	console.log (x + "is not an even number")
// }
   

// Exercise 2:
// let x = Number(prompt ("Please choose a number") );
// let y = Number(prompt ("Please choose a number"));
 // or let x=4
 // let y=5
// if (x>y) {
// 	console.log (x + "greater than" + y);
// }
// else {
// 	console.log (y + "is greater than" + x);
// }


//Exercise 3:
// if (x.toLowerCase()=="french"){
// 	console.log("Bonjour");
// }
// else if (x.toLowerCase()=="english"){
// 	console.log("hello");
// }
// else if (x.toLowerCase()=="hebrew"){
// 	console.log("Shalom");
// }
// else {
// 	console.log(":)");
// }

// switch(x.toLowerCase()){
// 	case "french":
// 	console.log("Bonjour");
// 	break;
// 	case "english":
// 	console.log("Hello");
// 	break;
// 	case "hebrew":
// 	console.log("Shalom");
// 	break;
// 	default:
// 	console.log(":)")

// }


//Exercise 4:
// let x=Number(prompt("What is your grade?"));

// if (x>=90){
// 	console.log ("A");
// }
// else if (x>=80){
// 	console.log("B");
// }
// else if (x>=70){
// 	console.log("C");
// }
// else {
// 	console.log("D");
// }



//Exercise 5:
// let me = ['my','favorite','color',"is","blue"]
// // console.log(me[0] + " " + me[1] + " " + me[2] + " " + me[3]);

// console.log(me.join(' 8 ')) //if x.join then in () place '' and space it " "(" ")



//Exercise 6:
// let x=prompt("blah blah blah");
// console.log( x.substring( x.lastIndexOf("ing"), x.length)) //swimming
//  if ( x.substring( x.lastIndexOf("ing"), x.length) == "ing"){
//  	console.log (x+"ly");
//  }
// 	else if (x.length>=3){
// 	console.log(x + "ing")
// 	}
// 	else {
// 		console.log(x)
// 	}



//Exercise 7:
// let x="I'm bad a not person";

// let a = x.indexOf("not");
// let b = x.indexOf("bad");
	

// if (b>a){
// 	console.log("I'm a good person");
// }
// else {
// 	console.log("who wrote this exercise?")
// }


//Exercise 8:
// let a="test";
// let b = true;
// let c = 789;
// a = "test";



//Exercise 9:
// let person = {
//  	firstName : "John",
//     lastName  : "Doe",
//     age       : 50,
//     eyeColor  : "blue",
//     id:{
//       num:909090,
//       add:{
//         city:'tel aviv'
//       }
// 	}
// }
//   console.log(person.firstName,person.lastName,person.age,person.eyeColor,person.id.num,person.id.add.city);



//Exercise 10:
// function isValidAge(age=10) {
//     return age
// }
// console.log (isValidAge() );


// function whereAmI(username, location) {
//     if (username && location) {
//         return "I am not lost";
//     } else {
//         return "I am totally lost!";
//     }
// }



//Exercise 11:
// //arrow function
// const whereAmI=(username, location)=>{
// 	 if (username && location) {
//         return "I am not lost";
//     } else {
//         return "I am totally lost!";
//     }
// }
// //example
// const x =(a,b) => {

// }



// Exercise 12:
// #1: 5
// #2: 5
// #3: hello
// #4: test
// #5: 2


// Exercise 13:
// #1:
// function experiencePoints() {
// return ( winBattle() ) ?  10  :  1;
// }
//2. nothing happens
//3. "you arrived home"
//4. "you found a river"
//5. nothing happens//