'use strict';
const names = ['John', 'Paul', 'Jones'];
let vastaus="";
for (let i in names) {
    vastaus+="<li>" + names[i]+ "</li>"
}
document.getElementById("target").innerHTML=vastaus
