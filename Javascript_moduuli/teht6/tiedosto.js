kysymys=prompt("Lasketaanko juuri?: Kirjoita Kyllä tai Ei:")
if (kysymys ==="kyllä") {
 juuri=prompt("Anna luku: ")
 const vastaus = Math.sqrt(juuri)
 document.getElementById("printti").innerHTML= vastaus
}
else if (kysymys === "ei"){
    document.getElementById("printti").innerHTML= "Juurta ei lasketa"
}