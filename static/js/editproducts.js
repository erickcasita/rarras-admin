const csrftoken = Cookies.get('csrftoken');
$(document).ready(function () {
  
    let id =  $("#idProductEdit").val();
    $.ajax({
        url: "/addproducts/getwerehousesproduct/" + id,
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': csrftoken
        },
        success: function (res) {
            res['idwerehouse'].forEach(element => {
                $("#check-" + element).prop("checked", true);
            });
        }
    });
    
  });

  $("#warehouseChecket :checkbox").change(function (e) { 
    if (!$(this).is(":checked")) {
        let check = $(this);
        $.ajax({
            url: "/addproducts/getstockproduct/"+$('#idProductEdit').val(),
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'werehouse':  $(this).val()
            },
            success: function (res) {
                console.log(res)
                if (res['stock'] > 0) {
                    check.prop('checked', true);
                } else {
                    $("#selectAll").prop('checked', false)
                }
            },
            error: function (res) {
                $("#selectAll").prop('checked', false)
            }
        });
    }
});