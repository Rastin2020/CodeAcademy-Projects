$(document).ready(function () {

    $('#ajaxBtn').click(function () {
        $.ajax('https://random.dog/woof.json',   // request url
            {
                success: function (data, status, xhr) {    // success callback function
                    if (data.url.endsWith(".png") || data.url.endsWith(".jpg") || data.url.endsWith(".jpeg") || data.url.endsWith(".JPG")) {
                        $("img").attr("src", data.url);
                    }
                }
            });
    });

});
