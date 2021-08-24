const url = window.location.href
const searchForm  = document.getElementById('search-form')
const searchInput  = document.getElementById('search-id')

const result  = document.getElementById('search-topic')
const csrf  = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(url);
console.log(csrf);
console.log(searchForm);
console.log(searchInput);
let search_function = (search_val) =>{
    search_data  = new FormData();
    search_data.append('csrf',csrf)
    search_data.append('saerch_val', searchInput);
    
    $.ajax({
        methed: 'POST',
        url: url,
        data:search_data,
        success:(res)=>{
            console.log(res);
        },
        error: (res)=>{
            console.log(res.error);
        }

    });
};
searchInput.addEventListener('keyup', (e)=>{
    //console.log(e.target.value);
    search_function(e.currentTarget.value)
});