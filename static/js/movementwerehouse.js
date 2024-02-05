$("#formFilterMovementWarehouses").validate({
    rules: {
        dateInitFilter: {
            required: true
        },
        dateFinishFilter: {
            required: true
        }
    },
    messages: {
        dateInitFilter: {
            required: "Por favor, Seleccione la fecha inicial para filtrar"
        },
        dateFinishFilter: {
            required: "Por favor, Seleccione la fecha final para filtrar"
        }
    },
    submitHandler: function (form) {
        let now = new Date();
        let today = new Date(`${now.getFullYear()}-${now.getMonth() + 1}-${now.getDate()}`);
        let dateinitform = new Date($('#dateInitFilter').val());
        let datefinishform = new Date($('#dateFinishFilter').val());
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