 
function noppa() {
    return Math.floor(Math.random()* 6) + 1;
}
const heitot=[]
let tulos;
 do {
    tulos=noppa()
    heitot.push(tulos)

    }
 
 while(tulos!=6)
let lista= "";
for(let i=0; i<heitot.length; i++){
    lista += "<li>" + heitot[i] + "</li>";
}
document.getElementById("vastaus").innerHTML= "<ul>" + lista + "</ul>";