$("#formWerehousePurchasing").validate({
    rules: {
        dateRemission: {
            required: true
        },
        priceList: {
            required: true
        }
    },
    messages: {
        dateRemission: {
            required: "Por favor, ingrese la fecha de remision"
        },
        priceList: {
            required: "Por favor, seleccione una lista de precios"
        }
    },
    submitHandler: function (form) {
        if ($('#listProduct').find('div').length > 0) {
            form.submit();
        } else {
            Swal.fire({
                title: 'Canasta Vacia',
                text: 'No se han agregado productos a la compra',
                icon: 'error',
                confirmButtonText: 'Ok',
                confirmButtonColor: '#0d6efd'
            });
        }
    }
});

let match = false;
const csrftoken = Cookies.get('csrftoken');
$("#codeProduct").keyup(function () {

    $.ajax({
        url: "/addproductlist/getpriceproduct/" + $("#codeProduct").val(),
        method: 'POST',
        data: {
            'csrfmiddlewaretoken': csrftoken,
            'productlist': $("#priceList").val()
        },
        success: function (res) {
            $("#codeSAP").val(res['cvesap']);
            $("#lastCost").val(res['predlp']);
            $("#product").val($("#codeProduct").val()).prop('selected', true).change();
            match = true;
        },
        error: function (res) {
            match = false;
            $("#codeSAP").val('');
            $("#lastCost").val('');
            $("#product option:first").prop('selected', true).change();
        }

    });
});

$("#add").on("click", function () {
    if (parseInt($("#quantity").val()) > 0 && match) {
        //nuevo
        if ($(`#${$("#codeProduct").val() + '-product'}`).length) {
            Swal.fire({
                title: 'Producto Existente',
                text: 'Este producto ya fue agregado a la compra',
                icon: 'warning',
                confirmButtonText: 'Ok',
                confirmButtonColor: '#0d6efd'
            });
            return false;
            match = false; //nuevo
        }
        //fin nuevo
        let quantity = parseInt($("#quantity").val());
        let amount = parseFloat($("#quantity").val() * $("#lastCost").val());
        let tr = `<tr id="${$("#codeProduct").val() + '-table'}">
                <td>${quantity}</td>
                <td>${$("#codeProduct").val()}</td>
                <td>${$("#codeSAP").val()}</td>
                <td>${$("#product").find('option:selected').text()}</td>
                <td>${$("#lastCost").val()}</td>
                <td>${amount}</td>
                <td>${amount}</td>
            </tr>`;
        $("#tableProduct").append(tr);
        $("#totalQuantity").val(parseInt($("#totalQuantity").val()) + quantity);
        $("#totalAmount").val(parseFloat($("#totalAmount").val()) + amount);
        $("#total").val(parseFloat($("#total").val()) + amount);
        add();
        clean();
    } else {
        //nuevo
        Swal.fire({
            title: 'No hay cantidad o producto',
            text: 'No se ha establecido una cantidad o producto establecido para la compra',
            icon: 'warning',
            confirmButtonText: 'Ok',
            confirmButtonColor: '#0d6efd'
        });
        //fin nuevo
    }
});

function add() {
    let product = `
    <div id="${$("#codeProduct").val() + '-product'}">
    <input type="hidden" name="quantity" value="${parseInt($("#quantity").val())}">
    <input type="hidden" name="product" value="${$("#codeProduct").val()}">
    <input type="hidden" name="sap" value="${$("#codeSAP").val()}">
    <input type="hidden" name="total" value="${parseInt($("#quantity").val()) * $("#lastCost").val()}">
    <input type="hidden" name="predlp" value="${$("#lastCost").val()}">

    </div>
    `;
    $('#listProduct').append(product);
}
$("#remove").on("click", function () {
    if ($(`#${$("#codeProduct").val() + '-product'}`).length) {
        let indexInput = 1;
        let lastQuantity = 0;
        $(`#${$("#codeProduct").val() + '-product'} input[type=hidden]`).each(function () {

            if (indexInput == 1) {
                lastQuantity = $(this).val();
                $("#totalQuantity").val(parseInt($("#totalQuantity").val()) - lastQuantity);
            }

            if (indexInput == 2) {
                $("#totalAmount").val(parseFloat($("#totalAmount").val()) - (lastQuantity * $("#lastCost").val()));
            }

            if (indexInput == 3) {
                $("#total").val(parseFloat($("#total").val()) - (lastQuantity * $("#lastCost").val()));
            }

            indexInput++;

        });

        $(`#${$("#codeProduct").val() + '-product'}`).remove();
        $(`#${$("#codeProduct").val() + '-table'}`).remove();
        clean();
    } else {
        //nuevo
        Swal.fire({
            title: 'Sin existencia en compra',
            text: 'El producto que intenta borrar no esta en la bolsa de compra',
            icon: 'warning',
            confirmButtonText: 'Ok',
            confirmButtonColor: '#0d6efd'
        });
        clean();
        //fin nuevo
    }
});

function clean() {
    $("#codeProduct").val('');
    $("#quantity").val('');
    $("#codeSAP").val('');
    $("#lastCost").val('');
    $("#product option:first").prop('selected', true).change();
}