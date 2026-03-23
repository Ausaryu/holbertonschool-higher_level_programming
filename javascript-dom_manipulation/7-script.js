const list_movies = document.querySelector("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())
  .then(data => {
    for (const film of data.results) {
      const new_list = document.createElement("li");
      new_list.textContent = film.title;

      list_movies.appendChild(new_list);
    }
  });