$(document).ready(function () {
    $('#messages').click(function (event) {
        $('.admin-message').show()
        $('.admin-newsletter').hide()
        $('.admin-send-newsletter').hide()
    });

    $('#newsletter').click(function (event) {
        $('.admin-message').hide()
        $('.admin-newsletter').show()
        $('.admin-send-newsletter').hide()
    });

    $('#send-newsletter').click(function (event) {
        $('.admin-message').hide()
        $('.admin-newsletter').hide()
        $('.admin-send-newsletter').show()
    });
  });
  