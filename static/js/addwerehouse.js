$("#formaddwerehouse").validate({
    rules: {
        title: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        store: {
            required: true
        }
    },
    messages: {
        title: {
            required: "Por favor, ingrese el nombre del almacen",
            minlength: "El nombre del almacen debe de tener al menos 6 caracteres"
        },
        store: {
            required: "Por favor, seleccione una sucursal"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formeditwerehouse").validate({
    rules: {
        title: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        store: {
            required: true
        }
    },
    messages: {
        title: {
            required: "Por favor, ingrese el nombre del almacen",
            minlength: "El nombre del almacen debe de tener al menos 6 caracteres"
        },
        store: {
            required: "Por favor, seleccione una sucursal"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});