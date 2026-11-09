let numero1=prompt("Anna ensimmäinen luku: ")
let numero2=prompt("Anna toinen luku: ")
let numero3=prompt("Anna kolmas luku: ")
let summa, tulo, keskiarvo;
summa = numero1 + numero2 + numero3;
tulo=numero1 * numero2 * numero3
keskiarvo= (numero1 + numero2 + numero3) / 3 
document.getElementById("sum").innerHTML="Summa: " + summa;
document.getElementById("product").innerHTML="Tulo: " + tulo;
document.getElementById("average").innerHTML="Keskiarvo: " + keskiarvo;
