const { OrganizationChart }= primereact.organizationchart

// const data = [{
//     label: 'Amn IT Business Solution Nig. LTD',
//     expanded: true,
//     children: [
//         {
//             label: 'F.C Barcelona',
//             expanded: true,
//             children: [
//                 {
//                     label: 'Chelsea FC'
//                 },
//                 {
//                     label: 'F.C. Barcelona'
//                 }
//             ]
//         },
//         {
//             label: 'Real Madrid',
//             expanded: true,
//             children: [
//                 {
//                     label: 'Bayern Munich'
//                 },
//                 {
//                     label: 'Real Madrid'
//                 }
//             ]
//         }
//     ]
// }];

const data = [{
    label:"Amn IT Business Solution Nig. LTD",
    expanded:true,
    children:[
        {
            label:"CEO",
            type:"person",
            className:"p-person",
            expanded:true,
            data:{name:"Abubakar Muhammad Nuhu", avatar:"ff.jpg"},
            children:[
                {
                    label:"COO",
                    type:"person",
                    expanded:true,
                    data:{name:"Ahmad Abubakar", avatar:''},
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
                    data:{name:"Ibrahim Auwal Musa"},
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
                    <img alt={node.data.avatar} src={`images/organization/${node.data.avatar}`} onError={(e) => e.target.src='https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png'} style={{ width: '32px' }} />
                    <div>{node.data.name}</div>
                </div>
            </div>
        );
    }

    if (node.type === "department") {
        return node.label;
    }
}



 

ReactDOM.render(<OrganizationChart value={data} nodeTemplate={nodeTemplate} />, document.getElementById('org-chart'))
