$("#formaddproducts").validate({
    rules: {
        name: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        categories: {
            required: true,
        },
        brands: {
            required: true,
        },
        cvesap: {
            required: true,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre del producto",
            minlength: "El nombre del producto debe de tener al menos 6 caracteres"
        },
        categories: {
            required: "Por favor, seleccione la categoria a la que pertenece"
        },
        brands: {
            required: "Por favor, seleccione la marca a la que pertenece"
        },
        cvesap: {
            required: "Por favor, ingrese el sku del producto"
        },
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formeditproducts").validate({
    rules: {
        name: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        categories: {
            required: true,
        },
        brands: {
            required: true,
        },
        cvesap: {
            required: true,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre del producto",
            minlength: "El nombre del producto debe de tener al menos 6 caracteres"
        },
        categories: {
            required: "Por favor, seleccione la categoria a la que pertenece"
        },
        brands: {
            required: "Por favor, seleccione la marca a la que pertenece"
        },
        cvesap: {
            required: "Por favor, ingrese el sku del producto"
        },
    },
    submitHandler: function (form) {
        form.submit();
    }
});

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
        let check = $(this);
        $.ajax({
            url: "/consultar/cantidad en almacen/" + $(this).val() + '/' + $('#idProductEdit').val(),
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrftoken
            },
            success: function (res) {
                if (res['quantity'] > 0) {
                    check.prop('checked', true);
                } else {
                    $("#selectAll").prop('checked', false)
                }
            },
            error: function (res) {
                $("#selectAll").prop('checked', false)
            }
        });
    }
});