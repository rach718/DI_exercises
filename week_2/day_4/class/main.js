// //iterate arrays//
// let basket =["orange", 'kiwi', 'apple', 'grapes']
// for (let x=0; x<basket.length; x++) {
// 	console.log(basket[x]);
// }

//this will give you the elements//
// for (i in basket){
// 	console.log(basket[i])
// }

// for (i in basket){
// 	console.log(i)
// }

// for (elem of basket){
// 	console.log(elem);
// }

// basket.forEach(elem =>{
// 	console.log(elem) //the element is the value//
// }
// )

// basket.forEach((elem, x)=>{
// 	console.log(x) //will get the index//
// }
// )

// for (i in basket){
// 	console.log(basket[i])
// }


// //iterate objects//can only use the "in" with objects
// let detailedBasket = {
// 	apples:5,
// 	oranges:20,
// 	grapes:1000
// }
// // //iterating the key, the key is the item// javascript is converting the object to an array//
// // for (item in detailedBasket){
// // 	console.log(item);
// // 	console.log(detailedBasket[item]); //this one gives you the index value//can interchange item for x, or i or wtvr)//	
// // // }


// // object.keys(obj) // keys
// // object.values(obj) //values
// // object.entries(obj) //keys and values

// // ex; username: rachelj, password: 1234
// // username is the key, password is the valueif its an array we can use the forEach loop//

// Object.keys(detailedBasket).forEach( key => {
// 	console.log( key);
// }
// );

// Object.values(detailedBasket).forEach(key =>{
// 	console.log( key);
// }
// );

// Object.entries(detailedBasket).forEach(key =>{
// 	console.log( 'enteries', key);
// }
// );


// for (var i = 0; i < arr.length; i++){
// 	console.log(arr[i]);
// }
//    

// // have to have the end condition in the while, and increment at the end.
// let arr = [5,8,9,3];
// while(i < arr.length){
// 	console.log(arr[i]);
// 	i++;
// }

//first do whats inside the do-do what u want at least once.
//if while false do what's in the {} 
//it's for false conditions. wont use it alot.

// let arr = [5,8,9,3];
// for (var i = 0; i < arr.length; i++){
// console.log(arr[i]);
// }
    
// let arr = [5,8,9,3];
// let x=0;
// while(x<arr.length){
// 	console.log(x);
// 	x++;
// }

// let y = 0
// do{
// 	console.log(y);
// 	y++;
// }
// while(y<4)
// 	for (var i = 0; 5<5; i++){
// 	}
// 	console.log(5);


//DAILY CHALLENGE//
// let Arr = [5,0,9,1,7,4,2,6,3,8];

// for (let i = 0; i < Arr.length; i++){
//     for (let a = 0; a < Arr.length; a++)
//         if (Arr[i] > Arr[a]) {
//           let temp = Arr[i];	
//           Arr[i] = Arr[a];
//           Arr[a] = temp;

//         }
//         	console.log(Arr.toString());
// }

// exercise:

var star="*"
for (let i=1; i<11; i++)
console.log(star.repeat(i));

var temp = ''
for (var i = 1; i < 11; i++){
  temp = (temp + "*");
  console.log(temp)
}



