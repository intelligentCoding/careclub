setTimeout(function () {
    $('#message').fadeOut('slow');
}, 10000);
$(":input").inputmask();
$("#phone").inputmask({"mask": "(999) 999-9999"});
