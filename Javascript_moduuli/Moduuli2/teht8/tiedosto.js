const jutut = ["piipuu", "papapapapap", "diidoopaa", "piipiipoopaa", "pepaeoapo"];
function concat(taulukko){
    let tulos=""
    for (let i=0; i< taulukko.length; i++) {
        tulos+=taulukko[i];
    }
    return tulos;
}
const vastaus=concat(jutut);
document.getElementById("vastaus").innerHTML=vastaus;
