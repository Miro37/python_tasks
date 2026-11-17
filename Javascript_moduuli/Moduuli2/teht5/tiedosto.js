const numbers=[];
let numerot
do{
    numerot = parseInt(prompt("Anna numero"));
    if (numbers.includes(numerot)){
        alert("Annoit tämän luvun jo.")
        break;
    }
    numbers.push(numerot)
} 
while (true);
numbers.sort((a, b) => a-b);
console.log(numbers);

