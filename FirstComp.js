var Button = primereact.button.Button;

var team = [
  {
    userID: 1,
    name: "Abubakar Muhammad Nuhu",
    rank: "Programmer",
    imgurl: "/static/media/first.jpg",
  },
  {
    userID: 2,
    name: "Yusuf Suleiman",
    rank: "Programm Designer",
    imgurl: "/static/media/second.jpg",
  },
  {
    userID: 3,
    name: "Suraj Umar",
    rank: "Prgramme Analyst",
    imgurl: "/static/media/third.jpg",
  },
  {
    userID: 4,
    name: "Ismail Balarabe",
    rank: "Digital Marketer",
    imgurl: "/static/media/first.jpg",
  },
];

function FirstComp(props) {
  return React.createElement(MyTeam, { team: team });
}

ReactDOM.render(
  React.createElement(FirstComp, null),
  document.getElementById("root")
);
