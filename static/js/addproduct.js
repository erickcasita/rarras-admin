
$("#selectAll").click(function () {
    if ($(this).is(":checked")) {
        $("#warehouseChecket :checkbox").each(function () {
            if (!$(this).is(":checked")) {
                $(this).trigger('click')
            }
        });
    } else {
        $("#warehouseChecket :checkbox").each(function () {
            if ($(this).is(":checked")) {
                $(this).trigger('click')
            }
        });
    }
});

$("#warehouseChecket :checkbox").change(function (e) {
    if (!$(this).is(":checked")) {
        $("#selectAll").prop('checked', false)
    }
});