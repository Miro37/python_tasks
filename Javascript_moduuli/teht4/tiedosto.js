numero=Math.floor(Math.random() * 4) + 1;
let nimi=prompt("Anna nimesi: ")
if (numero === 1) {
    document.getElementById("vastaus").innerHTML="Terve " + nimi + "luokkasi on Rohkelikko."
}
else if (numero === 2) {
    document.getElementById("vastaus").innerHTML="Terve " + nimi + "luokkasi on Luihuinen."
}
else if (numero === 3) {
    document.getElementById("vastaus").innerHTML="Terve " + nimi + "luokkasi on Puuskupuh"
}
else if (numero ===4) {
    document.getElementById("vastaus").innerHTML="Terve " + nimi + "" + "luokkasi on Korpikynsi"
}