$('.enter-post').keypress(function (event) {
  if (event.which == 13) {
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
  }
});

$('#post-form').on('submit', function(event){
  event.preventDefault();
  console.log("form submitted!")  // sanity check
  create_post();
});

$(".table").on("click", "td", function() {
  $("td").removeClass("mark");
  $( this ).addClass("mark");
  $(".panel-heading").text($( this ).text()+" "+$(".month").text());
  console.log("get day is working!") // sanity check
  $.ajax({
    type: "GET",
    url: "/get_day/",
    data: {task_day : $(".panel-heading").text() },
    success: function(json){
      $(".list-group").empty()
      $.each(json, function(k, v) {
        console.log(v);
        $(".list-group").append('<li class="list-group-item">'+v+'</li>');
});
    }
  });
});

function create_post() {
  console.log($(".panel-heading").text()) // sanity check
  $.ajax({
    url : "/create_task/", // the endpoint
    type : "POST", // http method
    data : { the_post : $('#post-text').val(),
              the_day : $(".panel-heading").text() }, // data sent with the post request

    // handle a successful response
    success : function(json) {
      $('#post-text').val(''); // remove the value from the input
      console.log(json); // log the returned json to the console
      $("#talk").prepend('<li class="list-group-item">'+json.text+"</li>");
      console.log("success"); // another sanity check
    },
    // handle a non-successful response
    error : function(xhr,errmsg,err) {
      $('#results').html("<div class='alert-box alert radius' data-alert>You need to be logged in</div>"); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
};
