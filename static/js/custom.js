$(document).ready(function() {
    $("#add-post").hide();
    $("#contact-details").hide();

    $("#login-form").hide();
    $("#login-button").click(function() {
        $("#login-form").toggle();
        console.log('a');
    });

    $("#add-post-form").hide();
    $("#add-post-button").click(function() {
        $("#add-post-form").toggle();
    });

    $('#contact').click(function() {
       $("#posts").hide();
       console.log("a");
       $("#contact-details").show();
    });

    $('#markdown').markItUp(myMarkdownSettings);
});
