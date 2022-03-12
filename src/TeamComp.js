const { Button } = primereact.button;
const {Carousel} = primereact.carousel
const {Card} = primereact.card


const truncate_text = (str, strt,end) => {
    return str.length > end ? str.substring(strt, end) + "..." : str;
  };



const MyTeam = ({team}) =>{
    //const {data, error} = useSWR('https://jsonplaceholder.typicode.com/photos?_limit=10',fetcher)
    const responsiveOptions = [
        {
            breakpoint: '1024px',
            numVisible: 3,
            numScroll: 3
        },
        {
            breakpoint: '768px',
            numVisible: 2,
            numScroll: 2
        },
        {
            breakpoint: '560px',
            numVisible: 1,
            numScroll: 1
        }
    ];
    const myTemplate =(obj)=>{
        const header = <img src={obj.imgurl}  
        alt="Card" width={500}  
        height={260} 
        //sizes="100vw" 
        
        //priority={true}  
        className='p-2' />
       // console.log('obj',obj)
        
        const footer = (
            <span>
                <Button label="View" icon="pi pi-check" />
            </span>
        );
        
        
        return(<div>
            <Card header={header} className="mx-1" title={truncate_text(obj.name,0,30)}
             subTitle={obj.rank} footer={footer}
            
            >
            <p className="m-0" style={{lineHeight: '1.5'}}>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
                    quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!</p>
            </Card>
            </div>)
        
    }
    
    //console.log('images',data)
    if(!team)return(<div></div>)
    return(
        <div className='my-1'>
        <h3 className='h3 fst-italic text-center text-muted'> Meet Our Wonderful Team</h3>
    <Carousel value={team} itemTemplate={myTemplate} numVisible={3} numScroll={1} 
            circular
            autoplayInterval={3000}
             responsiveOptions={responsiveOptions}
             />
    </div>
    )
}

