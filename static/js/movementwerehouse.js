$("#formFilterMovementWarehouses").validate({
    rules: {
        dateFilter: {
            required: true
        }
    },
    messages: {
        dateFilter: {
            required: "Por favor, Seleccione una fecha"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$("#formWarehouseMovement").validate({
    rules: {
        werehouseTypeMovement: {
            required: true
        },
        concept: {
            required: true
        },
        werehouse: {
            required: true,
        }
    },
    messages: {
        werehouseTypeMovement: {
            required: "Por favor, Seleccione un tipo de movimeinto"
        },
        concept: {
            required: "Por favor, Seleccione un concepto de almacen"
        },
        werehouse: {
            required: "Por favor, Seleccione un almacen"
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});
let addition = true;
const csrftoken = Cookies.get('csrftoken');

$("#branchValidation").change(function () {
    

    $.ajax({
        url: "/addtypemovement/gettypemovement/"+ $(this).val(),
        method: 'POST',
        data : {
            'csrfmiddlewaretoken':csrftoken
            
        },
       
        success: function (res) {

            console.log(res)
            $('#werehouseConcept').empty();
            let option = '<option selected disabled value="">Seleccionar ...</option>';
            Object.entries(res).forEach(([key,value])=>{
                if(key != 'typemovement'){
                    option += `<option value="${key}">${value}</option>`;

                }

            })
            addition = res['typemovement'];
            console.log(addition)
            $('#werehouseConcept').append(option);
        }
    });
});

$("#tableWerehouseMovement input[type=number]").keyup(function () {

    let val = $(this).val();
    let input = $(this);
    let total = 0

    if (addition) {
        $("#tableWerehouseMovement input[type=number]").each(function () {

            if (!$(this).val() == '' && !$(this).val() == 0) {
                total += parseInt($(this).val());
            }
        });
   
        
        $("#totalMovementWarehouse").val(total);
    } else {
        let id = $(this).attr("id").split("-")[0];
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

                $("#tableWerehouseMovement input[type=number]").each(function () {

                    if (!$(this).val() == '' && !$(this).val() == 0) {
                        total += parseInt($(this).val());
                    }
                });
                $("#valuetypeMovement").val("resta");
                $("#totalMovementWarehouse").val(total);
            }
        });
    }


});

$(document).ready(function () {
   
    $("#tableWerehouseMovement input[type=number]").each(function () {
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