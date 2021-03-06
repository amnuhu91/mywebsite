var OrganizationChart = primereact.organizationchart.OrganizationChart;

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

var data = [{
    label: "Amn IT Business Solution Nig. LTD",
    expanded: true,
    children: [{
        label: "CEO",
        type: "person",
        className: "p-person",
        expanded: true,
        data: { name: "Abubakar Muhammad Nuhu", avatar: "ff.jpg" },
        children: [{
            label: "COO",
            type: "person",
            expanded: true,
            data: { name: "Ahmad Abubakar", avatar: '' },
            children: [{
                label: "Front end design",
                className: "department-cfo"
            }, {
                label: "Data base design",
                className: "department-cfo"
            }]
        }, {
            label: "CCo",
            type: "person",
            expanded: true,
            data: { name: "Ibrahim Auwal Musa" },
            children: [{
                label: "Marketing",
                className: "department-coo"
            }, {
                label: "Sale",
                className: "department-coo"
            }]
        }]

    }]
}];

var nodeTemplate = function nodeTemplate(node) {
    if (node.type === "person") {
        return React.createElement(
            "div",
            null,
            React.createElement(
                "div",
                { className: "node-header" },
                node.label
            ),
            React.createElement(
                "div",
                { className: "node-content" },
                React.createElement("img", { alt: node.data.avatar, src: "images/organization/" + node.data.avatar, onError: function onError(e) {
                        return e.target.src = 'https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png';
                    }, style: { width: '32px' } }),
                React.createElement(
                    "div",
                    null,
                    node.data.name
                )
            )
        );
    }

    if (node.type === "department") {
        return node.label;
    }
};

ReactDOM.render(React.createElement(OrganizationChart, { value: data, nodeTemplate: nodeTemplate }), document.getElementById('chart'));