$("#formaddbrands").validate({
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
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre de la marca",
            minlength: "El nombre de la marca debe de tener al menos 6 caracteres"
        },
        categories: {
            required: "Por favor, seleccione la categoria a la que pertenece"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formeditbrands").validate({
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
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre de la marca",
            minlength: "El nombre de la marca debe de tener al menos 6 caracteres"
        },
        categories: {
            required: "Por favor, seleccione la categoria a la que pertenece"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});