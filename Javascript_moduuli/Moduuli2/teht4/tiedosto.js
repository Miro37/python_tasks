const numerot=[]
do{
    kysely=parseInt(prompt("Anna luku: "))
    if (kysely !== 0) {
        numerot.push(kysely);
    } 
}
while (kysely != 0);

numerot.sort((a, b) => b - a);
console.log(numerot)
