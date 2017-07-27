$(document).ready(function () {
  //your code here
  $('button').click(function() {
        var user = $('#txtUsername').val();
        var pass = $('#txtPassword').val();
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

// $('.process_customer').bind('click', function() {
//   event.preventDefault();
//   $('form input[name=user_input]').each(function (){
//       var myinfo = $(this).val();
//     })
//   $.getJSON('/add_user', {
//     a: myinfo,
//     b: 'test'
//   }, function(data) {
//     console.log(data);
//   });
//   return false;
// });