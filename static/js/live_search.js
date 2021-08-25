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
    search_data  = new FormData();
    search_data.append('csrfmiddlewaretoken',csrf)
    search_data.append('saerch_val', searchInput.value);
    
    axios.post('/course-detail/', search_data)
    .then((res)=>{
        console.log('tested')
    })
    .catch((err)=>{
        console.log('err')
    })
};
searchInput.addEventListener('keyup', (e)=>{
   
   search_function(e.target.value)
});
