
const osoite = "https://api.chucknorris.io/jokes/random"

fetch(osoite)
    .then(function(vastaus) {
      return vastaus.json();
    })
    .then(function(data) {
      console.log(data.value);
    });
