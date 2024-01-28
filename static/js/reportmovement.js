$("#formreportmovements").validate({
    rules: {
        typemovement: {
            required: true,
        },
        werehouse: {
            required: true,
        },
        concept: {
            required: true,
        },
        date_init: {
            required: true,
        },
        date_finish: {
            required: true,
        }
    },
    messages: {
        typemovement: {
            required: "Por favor, seleccione el movimiento del reporte"
        },
        werehouse: {
            required: "Por favor, seleccione el almacen del reporte"
        },
        concept: {
            required: "Por favor, seleccione el concepto del reporte"
        },
        date_init: {
            required: "Por favor, seleccione la fecha inicial del reporte"
        },
        date_finish: {
            required: "Por favor, seleccione la fecha final del reporte",
        }
    },
    submitHandler: function (form) {
        let now = new Date();
        let today = new Date(`${now.getFullYear()}-${now.getMonth() + 1}-${now.getDate()}`);
        let dateinitform = new Date($('#date_init').val());
        let datefinishform = new Date($('#date_finish').val());
        if (today < dateinitform || today < datefinishform) {
            Swal.fire({
                title: 'Fecha no validas',
                text: 'Alguna fecha proporcionada es posterior al dia actual',
                icon: 'error',
                confirmButtonText: 'Ok',
                confirmButtonColor: '#0d6efd'
            });
        } else {
            if (dateinitform > datefinishform) {
                Swal.fire({
                    title: 'Fecha inicial no valida',
                    text: 'La fecha inicial del reporte es posterior a la fecha final',
                    icon: 'error',
                    confirmButtonText: 'Ok',
                    confirmButtonColor: '#0d6efd'
                });
            } else {
                form.submit();
            }
        }
    }
});

const csrftoken = Cookies.get('csrftoken');

$("#branchValidation").change(function () {
    $.ajax({
        url: "/addtypemovement/gettypemovement/" + $(this).val(),
        method: 'POST',
        data: {
            'csrfmiddlewaretoken': csrftoken
        },

        success: function (res) {
            $('#reportmovementconcept').empty();
            let option = '<option selected disabled value="">Seleccionar ...</option>';
            Object.entries(res).forEach(([key, value]) => {
                if (key != 'typemovement') {
                    option += `<option value="${key}">${value}</option>`;

                }
            })
            $('#reportmovementconcept').append(option);
        }
    });
});