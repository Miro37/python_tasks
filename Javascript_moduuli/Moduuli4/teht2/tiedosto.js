'use strict'
const haesarja = document.querySelector("form")
haesarja.addEventListener('submit', async function (evt) {
  evt.preventDefault();
const query = document.querySelector("#query").value;
try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`)
    const Jsondata = await response.json();
    console.log(Jsondata);
} catch(error) {
    console.error("virhe haettaessa dataa:", error);
}
})