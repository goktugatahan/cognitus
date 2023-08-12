$(document).ready(function () {
  get_datas();
});

function get_datas() {
  $.ajax({
    type: "GET",
    url: "{% url 'get_datas' %}",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    success: function (datas) {
      $("#data_list").html("");

      for (let i = 0; i < datas.length; i++) {
        $("#data_list").append(`
                          <tr>
                              <td>${datas[i].text}</td>
                              <td>${datas[i].label}</td>
                            <td><button value="${datas[i].id}" class="delete_button"> Delete data </button></td>
                          </tr>`);
      }
    },
    error: function (error) {},
  });
}
$(document).on("click", ".delete_button", function () {
  let data_id = $(this).attr("value");

  let req_data = {
    data_id: data_id,
  };

  $.ajax({
    type: "DELETE",
    url: "{% url 'delete_data' %}",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(req_data),
    success: function (response) {
      get_datas();
    },
    error: function (error) {
      get_datas();
    },
  });
  return false;
});
function train_data() {
  $.ajax({
    type: "GET",
    url: "{% url 'train_data' %}",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    success: function (datas) {
      $("#data_list").html("");
    },
    error: function (error) {},
  });
}
