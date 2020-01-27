let game = alert ("Welcome to hangman!");
const word = "abstract";
const chances = 10;
let wordArr = word.split('');
let userArr = [];

 for (var i = 0; i < wordArr.length; i++) {
   if(i == 0 || i == wordArr.length-1){
    userArr.push(wordArr[i]);
  }
  else {
    userArr.push('*');
   }
  }
  alert(userArr.join(''));
 
 for (let i = 0; i < 10; i++){
  let guess = prompt("Guess a letter to figure out the word");
   if (guess.length<=1){
    for (let j = 0; j < wordArr.length; j++) {
      if (wordArr[j].toLowerCase() == guess.toLowerCase()) {
        userArr[j] = wordArr[j];
      }
    }
    alert(userArr.join(''));
    if(word == userArr.join('')){
    alert("Good job! The answer " + word + " was correct!");
    break;
    }
  }
}