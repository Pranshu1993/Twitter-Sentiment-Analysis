// script.js
$(document).ready(function() {
    $("#clear-btn").click(function() {
        $("#input-text").val("");
        $("#sentiment").text("");
    });

    $("#predict-btn").click(function() {
        var input_text = $("#input-text").val();
        $.ajax({
            type: "POST",
            url: "/predict",
            data: { text: input_text },
            success: function(response) {
                $("#sentiment").text(response);
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    });
});
