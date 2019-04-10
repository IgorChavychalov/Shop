window.onload = function () {
    $(".basket-list").on("change", "input[type='number']", function (event) {
        var targetHref = event.target;
        $.ajax({
            url: "/basket/update/" + targetHref.name + "/" + targetHref.value + "/",
            success: function (data) {
                console.log(data);

                $('.basket-list').html(data.result);
            }
        });
    });
};
