// let arr = ["banana", 'apples', 'oranges', 'pears', 'kiwi']

// for(let i = 0; i<arr.length; i++) {
// 	console.log(arr[i])
// }
// for(let i = arr.length-1; i >= 0; i--) {
// 	console.log(arr[i])
// }


// //Write a JavaScript for loop that will iterate from 0 to 15. For each iteration,
// //it will check if the current number is odd or even,
// //and display a message to the screen.
// //Sample Output:
// //"0 is even"
// //"1 is odd"
// //"2 is even"

// for(let i=0; i<=15; i++){
// 	if (i%2==0){
// 		console.log (i + " even")
// 	}
//      else {
//      	console.log (i + " odd")
//      }
// }
	
// ​
// //Write a JavaScript program which iterates the integers from 1 to 100.
// //But for multiples of three print "Fizz" instead of the number and
// //for the multiples of five print "Buzz".
// //For numbers which are multiples of both three and five print "FizzBuzz".

for (let i = 1; i <= 100; i++) {
	if (i%3==0 && i%5==0){
		console.log("fizzbuzz");
	}
     else if (i%3==0) {
	console.log("fizz");
	}
	else if (i%5==0){
		console.log("buzz");
	}
	else{
		console.log(i);
	}
}
// ​
// //Write a JavaScript program which compute, the average marks of the following students
// // Then, this average is used to determine the corresponding grade.
// /*
// var students = [
//   ['David', 80],
//   ['Vinoth', 77],
//   ['Divya', 88],
//   ['Ishitha', 95],
//   ['Thomas', 68]
// ];
// Range	Grade
// F <60
// D <70
// C <80
// B <90
// A <100
// */
 var students = [
  ['David', 80],
  ['Vinoth', 77],
  ['Divya', 88],
  ['Ishitha', 95],
  ['Thomas', 68]
];
	let sum=0;
	for (let i = 0; i <students.length; i++){
		sum = sum + students[i][1];
	}
	let avg = sum/students.length;
	{
		console.log(avg)
	}

	 if (avg<60) {
	 	console.log('f')
	 }
	 else if(avg<70) {
	 	console.log ('d')
	 }
	 else if(avg<80) {
	 	console.log ('c' )
	 }
	 else if(avg<90) {
	 	console.log('b');
	 }




// //Write a JavaScript program which iterates the integers from 1 to 100.
// //But for multiples of three print "Fizz" instead of the number and
// //for the multiples of five print "Buzz".
// //For numbers which are multiples of both three and five print "FizzBuzz".
// ​
// //Write a JavaScript program to construct the following pattern,
// //using a nested for loop.
// *
// * *
// * * *
// * * * *
// * * * * *

// var star="*"
// for (let i=1; i<6; i++)
// console.log(star.repeat(i));

// var temp = ''
// for (var i = 1; i < 6; i++){
//   temp = temp + *
//   console.log(temp)
// }
// ​

// Sort the array const arr = [5,0,9,1,7,4,2,6,3,8];using a for loop after sorting the result will be [9,8,7,6,5,4,3,2,1,0]
// Use the method toString() to render the array as a string

// a. hint - use a temporary VARIABLE : let temp;
// b. hint # 2 - use 2 loops
// for (let i = 0; i < arr.length; i ++) { statement }


// const arr = [5,0,9,1,7,4,2,6,3,8]
// arr.toString()
// console.log(arr)




// //DAILY CHALLENGE//

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


