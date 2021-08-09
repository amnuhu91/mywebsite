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





// const myform = document.getElementById('reg')
// myform.addEventListener('submit',(event)=>{
//   event.preventDefault();
//   //console.log(myform);
//   const csrfmiddlewaretoken =  document.querySelector('[name=csrfmiddlewaretoken]').value;
//   const last_name = document.getElementById('post-l_name');
//   const midle_name = document.getElementById('post-midle');
//   const first_name = document.getElementById('post-f_name');
//   //console.log(csrfmiddlewaretoken);
//   const fd = new FormData();
  
//   fd.append('f_name',first_name.value)
//   fd.append('midle',midle_name.value)
//   fd.append('l_name',last_name.value)
//   fd.append("csrfmiddlewaretoken",csrfmiddlewaretoken)
 
//   // for(let val of fd){
//   //   console.log(val);
//   // }
//   axios.post("",fd)
//   .then((response)=>{
//     let data = response.data;
//     console.log(data);
//     // for(let i=0; i<data.length; i++){
//     //   let per = data[i];
//     //   console.log(per.id, per.f_name,);
      
//     // }
//     for(let obj in data){
//       console.log(`${obj}:  :${data[obj].f_name},${data[obj].midle}${data[obj].l_name}
      
//       `);
//     }
//     if(response.status==200){
//       first_name.value=''
//       midle_name.value=''
//       last_name.value=''
//       //myform.reset()
//       first_name.focus()
//       $('#view-per').click().hide(0);


//     }
//     else{
//       console.log('something went wrong');
//     }
    

//   })
//   .catch((err)=>{
//     console.log(err);
//   });
    
  
// });

// const viewPer = document.getElementById('view-per');
// viewPer.addEventListener('click', function(){
//   const percontainer= document.getElementById('pers')
  
//   axios.get('/person')
//       .then((response)=>{
//           //console.log(response.data);
//         percontainer.innerHTML=response.data;

//       })
//       .catch((err)=>{
//         console.log(err);
//       });
// });