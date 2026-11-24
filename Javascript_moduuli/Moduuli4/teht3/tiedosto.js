'use strict'
const haesarja = document.querySelector("form")
const resultsDiv = document.querySelector('#results');

haesarja.addEventListener('submit', async function (evt) {
  evt.preventDefault();
  resultsDiv.innerHTML = '';
const query = document.querySelector("#query").value;
try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`)
    const Jsondata = await response.json();
    console.log(Jsondata);

    for (const tvshow of Jsondata) {
    const show = tvshow.show;
    const article = document.createElement("article");
    const h2 = document.createElement("h2");
    h2.textContent=show.name;

    const link = document.createElement("a")
    link.href = show.url;
    link.textContent = show.url;
    link.target = '_blank';
    const summaryDiv = document.createElement('div');
  summaryDiv.innerHTML = show.summary ?? '';

  article.append(h2, link);

  if (show.image?.medium) {
    const img = document.createElement('img');
    img.src = show.image.medium;
    img.alt = show.name;
    article.append(img);
  }
    article.append(summaryDiv);
    resultsDiv.append(article);
}
} catch(error) {
    console.error("virhe haettaessa dataa:", error);
}
})
