$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
      let lang = $('INPUT#language_code').val();
      getHelloData(lang);
    });
  $('INPUT#language_code').on('focus', function() {
      $(this).on('keydown', function(event) {
        if (event.which === 13) {
          var lang = $(this).val();
          getHelloData(lang);
        }
      });
    });
});

function getHelloData(lang) {
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
    $('DIV#hello').text(data.hello);
  });
}
