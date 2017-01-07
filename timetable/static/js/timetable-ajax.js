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
$("#talk").on("click","button", function() {
  console.log($(this).parent().text());
  var task = $(this).parent()
  $.ajax({
    url : "/delete_task/", // the endpoint
    type : "POST", // http method
    data : { the_post : task.text(),
              the_day : $(".panel-heading").text() }, // data sent with the post request

    // handle a successful response
    success : function(json) {
      console.log("succes");
      task.remove();
    },
    // handle a non-successful response
    error : function(xhr,errmsg,err) {
      $('#results').html("<div class='alert-box alert radius' data-alert>You need to be logged in</div>"); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
  console.log("removed");
  var badge = choosen.find("span");
  var value = parseInt(badge.text())-1;
  if(value){
    badge.text(value);
  }
  else{
    badge.remove();
  }
});

var choosen = $(".table")
$(".table").on("click", "td", function() {
  $("td").removeClass("mark");
  $( this ).addClass("mark");
  choosen = $(this)
  $(".panel-heading").text($(this).clone().children().remove().end().text().split(' ')[0]+" "+$(".month").text());
  $.ajax({
    type: "GET",
    url: "/get_day/",
    data: {task_day : $(".panel-heading").text() },
    success: function(json){
      $(".list-group").empty()
      $.each(json, function(k, v) {
          console.log("add");
        $(".list-group").append('<li class="list-group-item">'+v+
        '<button type="button" id="button-x" class="btn btn-default btn-xs pull-right glyphicon glyphicon-remove"></button></li>');
});
    }
  });
});

function create_post() {// sanity check
  if(choosen.text() != $(".table").text() && !choosen.hasClass("noday") && $('#post-text').val() != "" && choosen.text()!=""){
    var cos = choosen.find("span");
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
      $("#talk").prepend('<li class="list-group-item">'+json.text+ '<button type="button" id="button-x" class="btn btn-default btn-xs pull-right glyphicon glyphicon-remove"></button></li>');
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
