let alkuvuosi=parseInt(prompt("Anna alkuvuosi: "))
let loppuvuosi=parseInt(prompt("Anna loppuvuosi: "))
vuodet=alkuvuosi
tulos=""
while (vuodet !== loppuvuosi) {
    if (vuodet % 4 ==0) {
         tulos += vuodet + "<br>";
}
    else if (vuodet % 400==0) {
         tulos += vuodet + "<br>";
    }
    vuodet = vuodet + 1 
}
document.getElementById("vastaus").innerHTML=tulos;
