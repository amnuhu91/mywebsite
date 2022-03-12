var Button = primereact.button.Button;
var Carousel = primereact.carousel.Carousel;
var Card = primereact.card.Card;


var truncate_text = function truncate_text(str, strt, end) {
    return str.length > end ? str.substring(strt, end) + "..." : str;
};

var MyTeam = function MyTeam(_ref) {
    var team = _ref.team;

    //const {data, error} = useSWR('https://jsonplaceholder.typicode.com/photos?_limit=10',fetcher)
    var responsiveOptions = [{
        breakpoint: '1024px',
        numVisible: 3,
        numScroll: 3
    }, {
        breakpoint: '768px',
        numVisible: 2,
        numScroll: 2
    }, {
        breakpoint: '560px',
        numVisible: 1,
        numScroll: 1
    }];
    var myTemplate = function myTemplate(obj) {
        var header = React.createElement('img', { src: obj.imgurl,
            alt: 'Card', width: 500,
            height: 260
            //sizes="100vw" 

            //priority={true}  
            , className: 'p-2' });
        // console.log('obj',obj)

        var footer = React.createElement(
            'span',
            null,
            React.createElement(Button, { label: 'View', icon: 'pi pi-check' })
        );

        return React.createElement(
            'div',
            null,
            React.createElement(
                Card,
                { header: header, className: 'mx-1', title: truncate_text(obj.name, 0, 30),
                    subTitle: obj.rank, footer: footer

                },
                React.createElement(
                    'p',
                    { className: 'm-0', style: { lineHeight: '1.5' } },
                    'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!'
                )
            )
        );
    };

    //console.log('images',data)
    if (!team) return React.createElement('div', null);
    return React.createElement(
        'div',
        { className: 'my-1' },
        React.createElement(
            'h3',
            { className: 'h3 fst-italic text-center text-muted' },
            ' Meet Our Wonderful Team'
        ),
        React.createElement(Carousel, { value: team, itemTemplate: myTemplate, numVisible: 3, numScroll: 1,
            circular: true,
            autoplayInterval: 3000,
            responsiveOptions: responsiveOptions
        })
    );
};