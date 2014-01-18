$(document).ready(function() {
    $("#add-post").hide();
    $("#contact-details").hide();

    $("#show_add_item").click(function() {
        $("#add-post").toggle();
        console.log("a");
    });

    $('#contact').click(function() {
       $("#posts").hide();
       console.log("a");
       $("#contact-details").show();
    });
});
