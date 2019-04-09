window.onload = function () {
//    console.log("загрузили DOM");
    $(".basket-list").on("change", "input[type='number']", function (event) {
//        console.log(event.target);

        var targetHref = event.target;

        $.ajax({
            url: "/basket/update/" + targetHref.name + "/" + targetHref.value + "/",
            success: function (data) {
                console.log(data);

                $('.basket-list').html(data.result);
            }
        });
    });
}

