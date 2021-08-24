$(document).ready(function(){
  $('#topic').accordion();
  
  console.log('loaded');

  //get email contact
  axios.get("https://programminghero.herokuapp.com/email/")
  .then((res)=>{
    data = res.data;
    console.log(data);
    for (let obj in data){
     // console.log(`${data[obj].email}`);
     let lst=''
     
     if (data[obj].status !=false){
      lst+=`
      <li class="list-group-item" style="font-size:10"><small><i class="fa fa-envelope me-3" ></i>${data[obj].email}</small></li>
      
    `
     }
     

      $('#emailcontact').append(lst)
    }
    

  })
  .catch((err)=>{
    console.log(err);
  });
//get phone for prod
  axios.get("https://programminghero.herokuapp.com/phone/")
  .then((res)=>{
    data = res.data;
    //console.log(data);
    for (let obj in data){
      //console.log(`${data[obj].phone}`);
     let lst=''
     
     if (data[obj].status != false ){
      lst+=`
      <li class="list-group-item" style="font-size:10"><small><i class="fa fa-mobile me-3" ></i>${data[obj].phone}</small></li>
      
    `
     }

      $('#emailcontact').append(lst)
    }
    

  })
  .catch((err)=>{
    console.log(err);
  });

//console.log('all request');
  //all
  const email_re = axios.get("https://programminghero.herokuapp.com/email/")
  const phone_re = axios.get("https://programminghero.herokuapp.com/phone/")
  axios.all([email_re,phone_re]).then(axios.spread((res1,res2)=>{
    // console.log(res1.data);
    // console.log(res2.data);
  }));
<<<<<<< HEAD
  
=======
  //addde
    let url = window.location.href;
    let searchform = $('#search-form')
   let search_input = $('#search-id')
    let csrf = document.getElementsByName('csrfmiddlewaretoken')
    console.log(search_input)
    console.log(searchform)
  $('#search-id').keyup((e)=>{
    //alert('keyup')
    console.log(e.taget.value)
  });
>>>>>>> b12e62693a2e5de745a64839e0a41f9cd526608e

});







