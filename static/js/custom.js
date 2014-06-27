$(document).ready(function() {
    $("#add-post").hide();
    $("#contact-details").hide();

    $("#show_add_item").click(function() {
        $("#add-post").toggle();
    });

    $("#login-form").hide();
    $("#login-button").click(function() {
        $("#login-form").toggle();
        console.log('a');
    });

    $('#contact').click(function() {
       $("#posts").hide();
       console.log("a");
       $("#contact-details").show();
    });
});
