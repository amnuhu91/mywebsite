const {useState,useEffect} = React
const { OrganizationChart }= primereact.organizationchart

const { ProgressSpinner } = primereact.progressspinner
 




function CompChart(){
    const [selection, setSelection] = useState([]);
    const data = [{
        label:"Amn IT Business Solution Nig. LTD",
        expanded:true,
        children:[
            {
                label:"CEO",
                type:"person",
                className:"p-person",
                expanded:true,
                data:{name:"Abubakar Muhammad Nuhu", avatar:"first.jpg"},
                children:[
                    {
                        label:"COO",
                        type:"person",
                        expanded:true,
                        data:{name:"Ahmad Abubakar", avatar:'third.jpg'},
                        children:[
                            {
                                label:"Front end design",
                                className:"department-cfo"
                            },
                            {
                                label:"Data base design",
                                className:"department-cfo"
                            }
                        ]
                    },
                    {
                        label:"CCo",
                        type:"person",
                        expanded:true,
                        data:{name:"Ibrahim Auwal Musa", avatar:"second.jpg"},
                        children:[
                            {
                                label:"Marketing",
                                className:"department-coo"
                            },
                            {
                                label:"Sale",
                                className:"department-coo"
                            }
                        ]
                    }
                ]
    
            }
        ]
    }]
    

    const nodeTemplate = (node) => {
        if (node.type === "person") {
            return (
                <div>
                    <div className="node-header">{node.label}</div>
                    <div className="node-content">
                        <img alt={node.data.avatar} src={`/static/media/${node.data.avatar}`} onError={(e) => e.target.src='https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png'} style={{ width: '32px' }} />
                        <div>{node.data.name}</div>
                    </div>
                </div>
            );
        }

        if (node.type === "department") {
            return node.label;
        }
    }

    return (
        <div className="organizationchart-demo">
            <div className="card">
                <h5 className="text text-center">Advanced</h5>
                <OrganizationChart value={data} nodeTemplate={nodeTemplate} selection={selection} selectionMode="multiple"
                    onSelectionChange={event => setSelection(event.data)} className="company"></OrganizationChart>

                {/* <h5>Basic</h5>
                <OrganizationChart value={data2}></OrganizationChart> */}
            </div>
        </div>
    )

}


function WithLoading(Component) {
    return function WihLoadingComponent({ isLoading, ...props }) {
      if (!isLoading) return <Component {...props} />;
      return <div style={{width:"400px",margin:"auto"}} className="justify-content-center">Hold on, fetching data might take some time.
             <ProgressSpinner style={{width: '50px', height: '50px'}} strokeWidth="8" fill="var(--surface-ground)" animationDuration=".5s"/>
      </div>;
    };
  }
const OrgWithLoading = WithLoading(CompChart)
function MyCompOrgChart(){
    const [isLoading, setIsloading] = useState(true)
    // setTimeout(()=>{
    //     setIsloading(false)
    // },5000)
    useEffect(()=>{
        setIsloading(false)
    },[])
   
   
    return(
        <OrgWithLoading isLoading={isLoading}/>
    )
}

 

ReactDOM.render(<MyCompOrgChart  />, document.getElementById('org-chart'))
