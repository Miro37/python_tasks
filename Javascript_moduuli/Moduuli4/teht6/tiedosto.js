'use strict';

const form = document.querySelector('form');
const resultsDiv = document.querySelector('#results');

form.addEventListener('submit', async function (evt) {
  evt.preventDefault();
  resultsDiv.innerHTML = '';
  const query = document.querySelector('#query').value;
  try {
    const response = await fetch(
      `https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(query)}`
    );
    const data = await response.json();
    for (const jokeItem of data.result) {
      const article = document.createElement('article');
      const p = document.createElement('p');
      p.textContent = jokeItem.value;
      article.append(p);
      resultsDiv.append(article);
    }
  } catch (error) {
    console.error('Virhe haettaessa vitsejä:', error);
  }
});