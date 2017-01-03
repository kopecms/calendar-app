$('.input').keypress(function (event) {
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
$("tr td").click(function(e){     //function_td
  $(this).css("font-weight","bold");
  e.stopPropagation();
});

function create_post() {
  console.log("create post is working!") // sanity check
  $.ajax({
    url : "create_post/", // the endpoint
    type : "POST", // http method
    data : { the_post : $('#post-text').val() }, // data sent with the post request

    // handle a successful response
    success : function(json) {
      $('#post-text').val(''); // remove the value from the input
      console.log(json); // log the returned json to the console
      $("#talk").prepend('<li class="list-group-item">'+json.text+"</li>");
      console.log("success"); // another sanity check
    },


    // handle a non-successful response
    error : function(xhr,errmsg,err) {
      $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
      " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
};
