const koirat=[];
for (let i=0; i < 6; i++ ) {
    let nimet=prompt("Anna koirien nimet: ");
    koirat.push(nimet)
    
}
koirat.sort()    
koirat.reverse()

let lista= "";
for(let i=0; i<koirat.length; i++){
    lista += "<li>" + koirat[i] + "<li>";
}
document.getElementById("vastaus").innerHTML=lista + "</ul>";