$(document).ready(() => {
  const elementToAdd = '<li>Item</li>';
  const holder = 'UL.my_list';
  $('DIV#add_item').on('click', () => {
    $(holder).append(elementToAdd);
  });
  $('DIV#remove_item').on('click', () => {
    $(holder + ' li:last').remove();
  });
  $('DIV#clear_list').on('click', () => {
    $(holder).empty();
  })
});
