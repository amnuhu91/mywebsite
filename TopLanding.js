var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

var _React = React,
    useState = _React.useState,
    useEffect = _React.useEffect;


var LandingComp = function LandingComp() {
  var _useState = useState({
    job_desc: "Providing IT Solution to Your Business.",
    slogan: "...be  ready for the future"
  }),
      _useState2 = _slicedToArray(_useState, 2),
      company_info = _useState2[0],
      setCompany_info = _useState2[1];

  return React.createElement(
    "div",
    { className: "row" },
    React.createElement(
      "div",
      {

        className: "col-sm-12 col-md-12 p-5 contlanding ",
        style: {
          backgroundColor: "white",
          border: "1px solid black",
          borderRadius: "5px",
          opacity: 0.8,
          boxShadow: "5px 10px 10px #390d04",
          transition: "0.5s"
        }
      },
      React.createElement(
        "p",
        { className: "h1", style: { color: "black" } },
        company_info.job_desc
      ),
      React.createElement(
        "div",
        { className: "d-flex justify-content-end " },
        React.createElement(
          "p",
          { className: "small" },
          company_info.slogan
        )
      ),
      React.createElement(
        "div",
        { className: "d-flex justify-content-around" },
        React.createElement(
          "div",
          null,
          React.createElement(
            "p",
            { className: "strong h6" },
            "connect with us on"
          ),
          React.createElement(
            "a",
            {
              style: { color: "#3b5998", marginRight: "20px" },
              href: "#!",
              role: "button"
            },
            React.createElement("i", { className: "fab fa-facebook-f fa-lg" })
          ),
          React.createElement(
            "a",
            {
              style: { color: "#55acee", marginRight: "20px" },
              href: "#!",
              role: "button"
            },
            React.createElement("i", { className: "fab fa-twitter fa-lg" })
          ),
          React.createElement(
            "a",
            {
              style: { color: "#dd4b39", marginRight: "20px" },
              href: "#!",
              role: "button"
            },
            React.createElement("i", { className: "fab fa-google fa-lg" })
          )
        ),
        React.createElement(
          "button",
          {
            id: "btns",
            className: "btn btn-outline-secondary",
            "data-mdb-ripple-color": "dark"
          },
          "Explore..."
        )
      )
    )
  );
};

ReactDOM.render(React.createElement(LandingComp, null), document.getElementById('toplanding'));