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
            minlength: 6,
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
            required: "Por favor, ingrese el sku del producto",
            minlength: "El sku del producto debe de tener al menos 6 caracteres"
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
            minlength: 6,
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
            required: "Por favor, ingrese el sku del producto",
            minlength: "El sku del producto debe de tener al menos 6 caracteres"
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
        $("#selectAll").prop('checked', false)
    }
});