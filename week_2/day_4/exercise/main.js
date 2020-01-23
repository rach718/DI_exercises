let usernum;
let computerNumber;
let lose;

function playTheGame (){
	let play = confirm ("Do you want to play the game?");

	do{
		if (play==true){
			choosenum();
			play = test();
			lose = test();
		} 
		else{
			play = false;
			alert ("No problem, Goodbye");
		}
	} while (play);
	if (lose == false){
		alert ("Sorry, game over:(")
	}
}


function choosenum(){
	let wrongnum = true;
	do{
		usernum = prompt ("Choose a number between 0 and 10");
		console.log(usernum);

		if (isNaN(usernum)){
			alert ("Sorry Not a number, Goodbye");
		}
		else if (usernum<0 || usernum>10){
			alert ("Sorry it's not a good number, Goodbye");
		}		
		else {
			wrongnum = false;
			if (isNaN(computerNumber)){
				computerNumber = Math.floor(Math.random() * 11);
				console.log(computerNumber);
			}
		}
	} while (wrongnum)
}

let tries = 0;
function test (){
	while(tries<2){
		if (usernum==computerNumber){
			console.log("User num " + usernum + " computerNumber " + computerNumber);
			alert ("You won!");
			return true;
		}
		else if (usernum>computerNumber){
			alert ("Please choose a lower number.");
			console.log("User num " + usernum + " computerNumber " + computerNumber);
			choosenum();
			tries = tries + 1;
		}
		else if (usernum<computerNumber){
			alert ("please choose a higher number.");
			console.log("User num " + usernum + " computerNumber " + computerNumber);
			choosenum()
			tries = tries + 1
		}
	}	return false;
} 




