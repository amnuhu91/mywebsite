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
    // get data function
    axios.get(url)
    .then((res) =>{
        console.log(res.data);
    })
    .catch((res) =>{
        console.log(res.error);
    })
    //on keyup handle function
    axios.post(url, search_data)
    .then((res)=>{
        console.log('tested')
        console.log(res.data)
        console.log(typeof res.data)
        topics = res.data
            console.log('empty search')
            for (let obj in topics){
                let lst=''
                 lst+=`
                 <li class="list-group-item" >${topics[obj].topic_name}</li>
               `
                result.innerHTML=lst
               }
    })
    .catch((err)=>{
        console.log('err')
    })
};
searchInput.addEventListener('keyup', (e)=>{
   
   search_function(e.target.value)
});


        
