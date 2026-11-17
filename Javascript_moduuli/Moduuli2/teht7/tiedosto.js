let tahkot=parseInt(prompt("Montako tahkoa nopassa on"))
function noppa() {
    return Math.floor(Math.random()* tahkot) + 1;
}
const heitot=[]
let tulos;
 do {
    tulos=noppa()
    heitot.push(tulos)

    }
 
 while(tulos!=tahkot)
let lista= "";
for(let i=0; i<heitot.length; i++){
    lista += "<li>" + heitot[i] + "</li>";
}
document.getElementById("vastaus").innerHTML= "<ul>" + lista + "</ul>";