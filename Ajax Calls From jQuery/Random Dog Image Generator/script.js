$(document).ready(function () {

    $('#ajaxBtn').click(function () {
        $.ajax('https://random.dog/woof.json',   // request url
            {
                success: function (data, status, xhr) {    // success callback function
                    $('img').attr("src", data.url);
                }
            });
    });

});
