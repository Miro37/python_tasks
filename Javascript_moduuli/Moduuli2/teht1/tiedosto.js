numbers=[];

for(let i=0; i < 5; i++ ) {
kysely=prompt("Anna numero: ")
numbers.push(kysely);
}
console.log(numbers)

for (let i=numbers.length -1; i >= 0; i--) {
    document.getElementById("vastaus").innerHTML += numbers[i] + "<br>";
}

