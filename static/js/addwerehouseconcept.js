$("#formaddwerehouseconcept").validate({
    rules: {
        title: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        typemovement: {
            required: true
        },
        description: {
            required: true,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        title: {
            required: "Por favor, ingrese el titulo del concepto",
            minlength: "El titulo del concepto debe de tener al menos 6 caracteres"
        },
        typemovement: {
            required: "Por favor, seleccione un tipo de movimiento"
        },
        description: {
            required: "Por favor, ingrese la descripción del concepto de almacen"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formeditwerehouseconcept").validate({
    rules: {
        title: {
            required: true,
            minlength: 6,
            normalizer: function (value) {
                return $.trim(value);
            }
        },
        typemovement: {
            required: true
        },
        description: {
            required: true,
            normalizer: function (value) {
                return $.trim(value);
            }
        }
    },
    messages: {
        title: {
            required: "Por favor, ingrese el titulo del concepto",
            minlength: "El titulo del concepto debe de tener al menos 6 caracteres"
        },
        typemovement: {
            required: "Por favor, seleccione un tipo de movimiento"
        },
        description: {
            required: "Por favor, ingrese la descripción del concepto de almacen"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});