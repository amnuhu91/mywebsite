const url = window.location.href
const searchForm  = document.getElementById('search-form')
const searchInput  = document.getElementById('search-id')

const result  = document.getElementById('search-topic')
const csrf  = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(url);
console.log(csrf);
console.log(searchForm);
console.log(searchInput);
const search_function = (search_val) =>{
    let search_data  = new FormData();
    search_data.append('csrfmiddlewaretoken',csrf)
    search_data.append('saerch_val', searchInput.value);
    console.log(search_data)
    axios.post(url, search_data)
    .then((res)=>{
        console.log('tested')
        console.log(res.data)
        console.log(typeof res.data)
        topics = res.data
        if searchInput.value ===null || searchInput.value ==='' searchInput.value ===undefined{
            console.log('empty search')
        }
        else{
            console.log(searchInput.value)
        }

    })
    .catch((err)=>{
        console.log('err')
    })
};
searchInput.addEventListener('keyup', (e)=>{
   
   search_function(e.target.value)
});


//           for (let obj in topics){
//           //console.log(`${data[obj].phone}`);
//          let lst=''

//          if (topics[obj].topic_name != '' ){
//           lst+=`
//           <li class="list-group-item" style="font-size:10"><small><i class="fa fa-mobile me-3" ></i>${topics[obj].topic_name}</small></li>

//         `
//          }

//          result.innerHTML = lst
//         }
