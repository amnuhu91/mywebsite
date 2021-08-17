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
  

});

const sr = document.getElementById('search-id')
sr.addEventListener('keyup', function(){
  alert('keyup')
});





