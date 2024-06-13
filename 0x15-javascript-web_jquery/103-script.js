$(document).ready(function () {
  function fetchHello () {
    const lang = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchHello);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchHello();
    }
  });
});
