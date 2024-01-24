$("#formAddTypeMovement").validate({
    rules: {
        name: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre del movimiento",
            minlength: "El nombre del movimiento debe de tener al menos 6 caracteres"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formedittypemovement").validate({
    rules: {
        name: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        name: {
            required: "Por favor, ingrese el nombre del movimiento",
            minlength: "El nombre del movimiento debe de tener al menos 6 caracteres"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});