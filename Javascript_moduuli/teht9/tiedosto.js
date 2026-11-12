luku=parseInt(prompt("Anna luku: "))
let onAlkuluku = true;
if (luku <= 1) {
    onAlkuluku = false;
}
else {
    for (let i=2; i < luku; i++) {
        if (luku % i === 0){
            onAlkuluku=false;
            break;
        }
    }
}
if (onAlkuluku) {
    document.getElementById("vastaus").innerHTML = "Luku " + luku +" on alkuluku";

}
else {
    document.getElementById("vastaus").innerHTML = "Luku " + luku + " ei ole alkulukua";

}