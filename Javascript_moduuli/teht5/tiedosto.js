vuosi=parseInt(prompt("Anna vuosi: "))
if (vuosi /4) {
    document.getElementById(vastaus).innerHTML="Vuosi " + vuosi +"" + "on karkausvuosi"
}
else if (vuosi / 400) {
    document.getElementById(vastaus).innerHTML="Vuosi " + vuosi + "" + "on karkausvuosi"
}
else {
    document.getElementById(vastaus)=innerHTML="Vuosi " + vuosi + "" + "ei ole karkausvuosi"
}
