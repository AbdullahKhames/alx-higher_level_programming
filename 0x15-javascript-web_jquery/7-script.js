$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, statusStr) => {
  $('DIV#character').text(data.name);
})
