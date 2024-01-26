$("#formTransferWarehouse").validate({
    rules: {
        werehouseTypeMovementSend: {
            required: true
        },
        werehouseConceptSend: {
            required: true
        },
        werehouseSend: {
            required: true,
        },
        werehouseTypeMovementReception: {
            required: true
        },
        werehouseConceptReception: {
            required: true
        },
        werehouseReception: {
            required: true,
        }
    },
    messages: {
        werehouseTypeMovementSend: {
            required: "Por favor, Seleccione un tipo de movimeinto"
        },
        werehouseConceptSend: {
            required: "Por favor, Seleccione un concepto de almacen"
        },
        werehouseSend: {
            required: "Por favor, Seleccione un almacen"
        },
        werehouseTypeMovementReception: {
            required: "Por favor, Seleccione un tipo de movimeinto"
        },
        werehouseConceptReception: {
            required: "Por favor, Seleccione un concepto de almacen"
        },
        werehouseReception: {
            required: "Por favor, Seleccione un almacen"
        }
    },
    submitHandler: function (form) {
        if (validateQuantity()) {
            form.submit();
        } else {
            Swal.fire({
                title: 'Productos en Cero',
                text: 'Para realizar un movimiento de almacen, se debe de tener al menos un producto con existencia',
                icon: 'warning',
                confirmButtonText: 'Ok',
                confirmButtonColor: '#0d6efd'
            });
        }
    }
});

let additionsend = true;
let additionreception = true;
const csrftoken = Cookies.get('csrftoken');
$("#werehouseTypeMovementSend").change(function () {
    $.ajax({
        url: "/addtypemovement/gettypemovement/" + $(this).val(),
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': csrftoken
        },
        success: function (res) {
            $('#werehouseConceptSend').empty();
            let option = '<option selected disabled value="">Seleccionar ...</option>';
            Object.entries(res).forEach(([key, value]) => {
                if (key != 'typemovement') {
                    option += `<option value="${key}">${value}</option>`;

                }

            })
            additionsend = res['typemovement'];
            $('#werehouseConceptSend').append(option);
        }
    });
});

$("#werehouseTypeMovementReception").change(function () {
    $.ajax({
        url: "/addtypemovement/gettypemovement/" + $(this).val(),
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': csrftoken
        },
        success: function (res) {
            $('#werehouseConceptReception').empty();
            let option = '<option selected disabled value="">Seleccionar ...</option>';
            Object.entries(res).forEach(([key, value]) => {
                if (key != 'typemovement') {
                    option += `<option value="${key}">${value}</option>`;

                }

            })
            additionreception = res['typemovement'];
            $('#werehouseConceptReception').append(option);
        }
    });
});

$("#tabletransferWerehouse input[type=number]").keyup(function () {
    let val = $(this).val();
    let input = $(this);
    let total = 0

    if(!additionsend){
        let id = $(this).attr("id").split("-")[0];
        console.log(id)
        $.ajax({
            url: "/addwerehouse/getstockwerehouse/"+ id,
        method: 'POST',
        data : {
            'csrfmiddlewaretoken':csrftoken
            
        },
            success: function (res) {
                console.log(res)
                let max = parseInt(res['stock']);
                if (val > max) {
                    Swal.fire({
                        title: 'Maximo Superado',
                        text: 'La cantidad maxima del producto es: ' + max,
                        icon: 'warning',
                        confirmButtonText: 'Ok',
                        confirmButtonColor: '#0d6efd'
                    });
                   
                    input.val(max);
                }
                $("#tabletransferWerehouse input[type=number]").each(function () {

                    if (!$(this).val() == '' && !$(this).val() == 0) {
                        total += parseInt($(this).val());
                    }
                });
                $("#valuetypeMovement").val("resta");
                $("#totaltransferWarehouse").val(total);
            }
        });
    }

});

$(document).ready(function () {
    $("#tabletransferWerehouse input[type=number]").each(function () {
        $(this).rules("add", {
            required: true,
            digits: true,
            min: 0,
            messages: {
                required: "Cantidad requerida",
                digits: "La cantidad debe ser un numero entero",
                min: "La cantidad debe ser un numero positivo"
            }
        });
    });
});

function validateQuantity() {
    $("#tabletransferWerehouse input[type=number]").each(function () {
        if ($(this).val() > 0) {
            return true;
        }
    });
    return false;
}
