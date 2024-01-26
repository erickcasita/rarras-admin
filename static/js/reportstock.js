$("#formgeneratereportstock").validate({
    rules: {
        categories: {
            required: true,
        },
        werehouse: {
            required: true,
        }
    },
    messages: {
        categories: {
            required: "Por favor, seleccione la categoria del reporte"
        },
        werehouse: {
            required: "Por favor, seleccione el almacen del reporte"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});