$('.enter-post').keypress(function (event) {
  if (event.which == 13) {
    event.preventDefault();
    create_post();
  }
});

$('#post-form').on('submit', function(event){
  event.preventDefault();
  create_post();
});

var choosen = $(".table")
$(".table").on("click", "td", function() {
  $("td").removeClass("mark");
  $( this ).addClass("mark");
  choosen = $(this)
  $(".panel-heading").text($( this ).text().split(" ")[0]+" "+$(".month").text());
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

function create_post() {// sanity check
  if(choosen.text() != $(".table").text()){
    var cos = choosen.find("span");
    console.log(cos.length)
    if(cos.length){
      cos.text(parseInt(cos.text())+1)
    }
    else{
      choosen.append('<span class="badge pull-right">1</span>');
    }
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
}
};
