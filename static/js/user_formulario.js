$('.process_customer').click(function(){
  event.preventDefault();
  $('form input[name=user_input]').each(function(){
    var mydata = $(this).val();
    window.alert(mydata);
    alert(mydata)
  });
  $.ajax({
    type: 'POST',
    url: '/add_user',
    data: mydata,
    cache: false,
    success: function(result) {
      if(result == "true"){
        
        alert("el paciente se grego");
      }else{
        alert("paciente no agrego");
      }
    }
  });
});