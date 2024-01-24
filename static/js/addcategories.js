$("#formaddcategories").validate({
    rules: {
        name: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        sat: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        umedida: {
            required: true,
            minlength: 2,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre de la categoria",
            minlength: "El nombre de la categoria debe de tener al menos 6 caracteres"
        },
        sat: {
            required: "Por favor, ingrese el codigo SAT de la categoria",
            minlength: "El codigo de la categoria debe de tener al menos 6 caracteres"
        },
        umedida: {
            required: "Por favor, ingrese la unidad de medida de la categoria",
            minlength: "La unidad de medida de la categoria debe de tener al menos 2 caracteres"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formeditcategories").validate({
    rules: {
        name: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        sat: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        umedida: {
            required: true,
            minlength: 2,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre de la categoria",
            minlength: "El nombre de la categoria debe de tener al menos 6 caracteres"
        },
        sat: {
            required: "Por favor, ingrese el codigo SAT de la categoria",
            minlength: "El codigo de la categoria debe de tener al menos 6 caracteres"
        },
        umedida: {
            required: "Por favor, ingrese la unidad de medida de la categoria",
            minlength: "La unidad de medida de la categoria debe de tener al menos 2 caracteres"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});