$(document).ready(function () {

    $('#ajaxBtn').click(function () {
        $.ajax('https://dog.ceo/api/breeds/image/random',   // request url
            {
                success: function (data, status, xhr) {    // success callback function
                    $("img").attr("src", data.message);
                }
            });
    });

});
