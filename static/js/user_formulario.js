$(document).ready(function () {
  //your code here
  $('button').click(function() {
        var user = $('#txtUsername').val();
        var pass = $('#txtPassword').val();
        if (user == '' || pass == '' ) {
            return alert('uno de los campos esta vacio');
        }
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                alert("Hello! I am an alert box!");
                alert(response);
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});


// $(document).ready(function () {
//   //your code here
//   $('button .process_customer').click(function() {
//         event.preventDefault();
//         var user = $('#first_name').val();
//         var last = $('#last_name').val();
//         var gender = $('#gender').val();
//         var type_id = $('#identification_type').val();
//         var id = $('#identification').val();
//         var phone = $('#phone').val();
//         var movil = $('#movil').val();
//         var email = $('#email').val();
//         var identificacion = $('#identification').val();
//         var birth = $('#date_birth').val();
//         var address = $('#address').val();
//         console.log(user,last,gender,type_id,id_phone,movil,email,identificacion,birth,address);
//         // $.ajax({
//         //     url: '/signUpUser',
//         //     data: $('form').serialize(),
//         //     type: 'POST',
//         //     success: function(response) {
//         //         console.log(response);
//         //     },
//         //     error: function(error) {
//         //         console.log(error);
//         //     }
//         // });
//     });
// });

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