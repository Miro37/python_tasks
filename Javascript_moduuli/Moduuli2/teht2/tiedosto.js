const kilpailijat=[];
kysely=prompt("Montako Kilpailijaa: ")
for (let i=0; i < kysely; i++ ) {
    let nimet=prompt("Anna kilpailijoiden nimet: ");
    kilpailijat.push(nimet)
    
}
kilpailijat.sort();
let lista="";
for(let i=0; i < kilpailijat.length; i++){
    lista += "<li>" + kilpailijat[i] + "</li>";
}
  
 document.getElementById("vastaus").innerHTML="<ol>" + lista + "</ol>";

 
    
