$(document).ready(function () {

    $('#submit').click(function () {
        var unit = $("#unit-search").val();
        var url = "https://cors-anywhere.herokuapp.com/https://age-of-empires-2-api.herokuapp.com/api/v1/unit" + "/" + unit;

        $.ajax(url,   // request url
            {
                success: function (data, status, xhr) {    // success callback function
                    console.log(data);
                    // Reset previous query: -------------------------------------------------------------------
                    $("#name").empty();
                    $("#description").empty();
                    $("#expansion").empty();
                    $("#age").empty();
                    $("#created_in").empty();
                    $("#cost").attr("hidden", true);
                    $("#1").empty();
                    $("#2").empty();
                    $("#build_time").empty();
                    $("#reload_time").empty();
                    $("#attack-delay").empty();
                    $("#movement_rate").empty();
                    $("#line_of_sight").empty();
                    $("#hit_points").empty();
                    $("#attack").empty();
                    $("#armor").empty();
                    $("#attack_bonus").attr("hidden", true);
                    $("ul").attr("hidden", true);
                    // New search -------------------------------------------------------------------
                    $("#name").append("Name: " + data.name);
                    $("#name").attr("hidden", false);
                    $("#description").append("(" + data.description + ")");
                    $("#description").attr("hidden", false);
                    $("#expansion").append("Expansion: " + data.expansion);
                    $("#expansion").attr("hidden", false);
                    $("#age").append("Age: " + data.age);
                    $("#age").attr("hidden", false);
                    $("#created_in").attr("hidden", false);
                    $.ajax("https://cors-anywhere.herokuapp.com/" + data.created_in,   // request url
                        {
                            success: function (data2, status, xhr) {
                                $("#created_in").append("Created in: " + data2[0].name);
                            }
                        });
                    $("#cost").attr("hidden", false);
                    // Conditionals depending on whether or not food, wood or gold coming in:
                    if (data.cost.Food && data.cost.Wood) {
                        $("#1").append(data.cost.Food + " food.");
                        $("#1").attr("hidden", false);
                        $("#2").append(data.cost.Wood + " wood.");
                        $("#2").attr("hidden", false);
                    } else if (data.cost.Food && data.cost.Gold) {
                        $("#1").append(data.cost.Food + " food.");
                        $("#1").attr("hidden", false);
                        $("#2").append(data.cost.Gold + " gold.");
                        $("#2").attr("hidden", false);
                    } else if (data.cost.Wood && data.cost.Gold) {
                        $("#1").append(data.cost.Wood + " wood.");
                        $("#1").attr("hidden", false);
                        $("#2").append(data.cost.Gold + " gold.");
                        $("#2").attr("hidden", false);
                    }
                    // ----------------------------------------------------------------------
                    $("#build_time").append("Build time: " + data.build_time + "s");
                    $("#build_time").attr("hidden", false);
                    $("#reload_time").append("Reload time: " + data.reload_time + "s");
                    $("#reload_time").attr("hidden", false);
                    if (data.attack_delay) {
                        $("#attack-delay").append("Attack delay: " + data.attack_delay + "s");
                        $("#attack-delay").attr("hidden", false);
                    }
                    if (data.name != "Trebuchet") {
                        $("#movement_rate").append("Movement rate: " + data.movement_rate + " tile(s)/second");
                        $("#movement_rate").attr("hidden", false);
                    } else {
                        $("#movement_rate").append("Movement rate: Can't move unless unpacked");
                        $("#movement_rate").attr("hidden", false);
                    }
                    $("#line_of_sight").append("Line of sight: " + data.line_of_sight + " tile(s)");
                    $("#line_of_sight").attr("hidden", false);
                    $("#hit_points").append("HP = " + data.hit_points);
                    $("#hit_points").attr("hidden", false);
                    $("#attack").append("Attack: " + data.attack);
                    $("#attack").attr("hidden", false);
                    $("#armor").append("Armor: " + data.armor + " (melee/pierce) ");
                    $("#armor").attr("hidden", false);
                    // Looping to add "attack_bonus" array elements:
                    for (i = 0; i < data.attack_bonus.length; i++) {
                        $("#attack_bonus").append(" " + data.attack_bonus[i]);
                    };
                    $("#attack_bonus").attr("hidden", false);
                    $("ul").attr("hidden", false);
                }
            });
    });
});
