function showtext() {
    var dialog2 = document.getElementById('dialog2');
    document.getElementById('show2').onclick = function() {
        dialog2.show();
    };
    document.getElementById('hide2').onclick = function() {
        dialog2.close();
    };
}
showtext();


document.getElementById("violin").addEventListener("click", function(){
    document.getElementById("audio1").play();
});


document.getElementById("piano").addEventListener("click", function(){
    document.getElementById("audio2").play();
});

document.getElementById("guitar").addEventListener("click", function(){
    document.getElementById("audio3").play();
});

document.getElementById("saxaphone").addEventListener("click", function(){
    document.getElementById("audio4").play();
});

document.getElementById("cello").addEventListener("click", function(){
    document.getElementById("audio5").play();
});

document.getElementById("trumpet").addEventListener("click", function(){
    document.getElementById("audio6").play();
});

document.getElementById("drums").addEventListener("click", function(){
    document.getElementById("audio7").play();
});

document.getElementById("clarinet").addEventListener("click", function(){
    document.getElementById("audio8").play();
});






// function pageScroll() {
//     window.scrollBy(0,1);
//     scrolldelay = setTimeout(pageScroll,10);
// }