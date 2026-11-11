noppa=Math.floor((Math.random() * 6)+1);
heitot=prompt("Montako kertaa noppaa heitetään")
let summa = 0;

for (let i=0; i < heitot; i++) {
    let luvut = Math.floor(Math.random() * 6) + 1;
    summa = summa + luvut
}
document.getElementById("vastaus").innerHTML=summa

