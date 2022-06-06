
function payWithPaystack(salary,nuban,bank) {
    Swal.fire({
        title: '<strong>Transaction Successful</strong>',
        type: 'success',
        html:
          'The sum of #' +salary +
          ' has been deposited into the Account Number '+nuban +
          ' at '+bank,
        showCloseButton: true,
        showCancelButton: false,
        focusConfirm: false,
        confirmButtonText:
          'Redirecting....',
        confirmButtonAriaLabel: 'Thumbs up, great!',

        
      })
      // setTimeout(()=>{
      //     window.location.href='/dashboard'
      // }, 3000)
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function AdvancePayment(username,userid) {
  var csrftoken = getCookie('csrftoken');
  // console.log(user);
  Swal.fire({
    title: 'Advance Payment',
    text: username,
    input: 'text',
    inputPlaceholder: 'amount',
      
    }).then(({value}) => {
      if (value) {
        console.log(value);
        $.ajax(
          {
              type:"POST",
              url: "/employee_advance/",
              data:{
                amount: value,
                user_id:userid,
                'csrfmiddlewaretoken': csrftoken
              },
              success: function( data ) 
              {
                // document.getElementById('price_sum').innerHTML =data['price__sum']
                //  console.log(data);
              }
           })

           
        Swal.fire('', 'success')
      } else {
        Swal.fire('', 'exit', 'exit')
      }
    });
    // setTimeout(()=>{
    //     window.location.href='/dashboard'
    // }, 3000)
}


function checkin(userid) {
  var csrftoken = getCookie('csrftoken');
  $.ajax(
    {
        type:"POST",
        url: "/employee_checkin/",
        data:{
          user_id:userid,
          'csrfmiddlewaretoken': csrftoken
        },
        success: function( data ) 
        {
          console.log(data);
        Swal.fire('', 'successful check in')
        window.location.reload();
          // document.getElementById('price_sum').innerHTML =data['price__sum']
          //  console.log(data);
        }
     })
}


  $(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/send',
      data:{
          employee:$('#employee').val(),
          message:$('#message').val(),
          sender:'employee',
        csrfmiddlewaretoken:getCookie('csrftoken'),
      },
      success: function(data){
         //alert(data)
      }
    });
    document.getElementById('message').value = ''
  });
  $(document).on('submit','#post-form-individual',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/send/employer',
      data:{
          employee:$('#employee').val(),
          message:$('#message').val(),
          sender:'employee',
        csrfmiddlewaretoken:getCookie('csrftoken'),
      },
      success: function(data){
         //alert(data)
      }
    });
    document.getElementById('message').value = ''
  });

  $(document).on('submit','#update_paid',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/update_paid',
      data:{
          employee:$('#employeeiddd').val(),
          sender:'employee',
        csrfmiddlewaretoken:getCookie('csrftoken'),
      },
      success: function(data){
         //alert(data)x
         console.log(data);
        //  var da = JSON.parse(data)
        //  console.log(da);
         if (data['message'] == "success"){
           
        Swal.fire('', 'successfully updated to paid')
           setTimeout(() => {
             
           location.reload()
           }, 2000);
         }
      }
    });
  });