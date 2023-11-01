$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    let lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
