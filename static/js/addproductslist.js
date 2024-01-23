$("#warehouseChecket :checkbox").change(function (e) {
  if ($(this).is(":checked")) {
    let product = `<tr id="${$(this).val()}-product">
                          <th scope="row">${$(this).val()}</th>
                          <td>${$(this).data("product")}</td>
                          <td>
                              <input type="number" class="form-control" id="${$(
                                this
                              ).val()}-price" name="prices-${$(this).val()}">
                          </td>
                      </tr>`;
    $("#inputsProducts").append(product);
    $("#formProductPrice").validate();
    $("#" + $(this).val() + "-price").rules("add", {
      required: true,
      number: true,
      min: 0,
      messages: {
        required: "Precio requerido",
        number: "El precio debe ser una cantidad monetaria",
        min: "El precio no puede ser un numero negativo",
      },
    });
  } else {
    $("#" + $(this).val() + "-product").remove();
  }
});

$("#formProductPrice").validate({
  rules: {
    name: {
      required: true,
      minlength: 6,
      normalizer: function (value) {
        return $.trim(value);
      },
    },
  },
  messages: {
    name: {
      required: "Por favor, ingrese el nombre de la Lista de Precios",
      minlength:
        "El nombre de la Lista de Precios  debe de tener al menos 6 caracteres",
    },
  },
  submitHandler: function (form) {
    form.submit();
  },
});

$(document).ready(function () {
  $("#inputsProducts input[type=number]").each(function () {
    let id = $(this).attr("id").split("-")[0];
    $("#warehouseChecket #" + id + "-checkbox").prop("checked", true);
  });
});
