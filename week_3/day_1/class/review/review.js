let things = document.getElementsByTagName("section")[0];
		let basket = ["apple", "orange", "banana"];
		// Loop for a set number of times
		for(i=0; i<basket.length; i++){
			console.log(basket[i])
		}
		// Loop through all the items
		for (fruit of basket){
			console.log(fruit);
		}
		let element = document.getElementById("div1") // Gets 1 div
		let array_of_elements = document.getElementsByClassName("mydiv") // Gets some divs
		let array_of_elements = document.getElementsByTagName("div") // Gets all divs
		for (item of array_of_elements){
			console.log(item)
		}
		// Functions
		function greet(name){
			name = name.charAt(0).toUpperCase() + name.slice(1);
			console.log("hello " + name + "!");
		}
		let students = ["adam", "bobby", "charlie"];
		for (student of students) {
			greet(student);
		}
		
		create element , then appendchild
		then get the elements, and then loop through them.

		getElementById; one element
		getElementsByTagName: array of some elements
		getElementsByClassName; array of all elements

		querySelector (#id) or (.class): gets you one
		querySelectorAll(css stuff): gets you all

		let paragraphs = document.getElementsByTagName('p');
		for(paragraph of paragraphs){
			paragraph.classList.add("redback");
		}
		paragraphs[paragraphs.lenth-1].remove(); //to get to the last p

		myarr[myarr.length-1] will get u to the last item on the arry.
		for first:  myarr[0]

			for (i in paragraphs){ //in checks index.  
				if (index % 2 == 0){
				paragraphs[index].classList.add("greenback");
				}
			else {//odd
				paragraphs[index].classList.add("redback");
				}

			}
			
			for(i=0;i<=things.length;i++)
			for (thing of things)
				for (i in things)