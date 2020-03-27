$.getJSON("http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=631416b69d0636bd13ceaff2562628e2", function (data) {
    console.log(data);
    var icon = "https://openweathermap.org/img/w/" + data.weather[0].icon + ".png";
    var temp = Math.round(data.main.temp);
    var description = data.weather[0].main;

    $("#icon").attr("src", icon);
    $("#description").append(description);
    $("#temp").append(temp);
});
