var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var _React = React,
    useState = _React.useState;
var InputText = primereact.inputtext.InputText;
var InputTextarea = primereact.inputtextarea.InputTextarea;

//Email Component

var EmailUsComp = function EmailUsComp() {
  var _useState = useState({}),
      _useState2 = _slicedToArray(_useState, 2),
      message = _useState2[0],
      setMessage = _useState2[1];

  var handleInputChange = function handleInputChange(e) {
    var target = e.target;
    var value = target.value;
    var name = target.name;

    setMessage(Object.assign({}, message, _defineProperty({}, name, value)));
  };
  var handlesubmit = function handlesubmit(e) {
    e.preventDefault();
    // console.log("message", message);
  };

  //console.log(message);
  return React.createElement(
    "div",
    {
      className: "card p-5",
      style: { width: "100%", boxShadow: "5px 10px 10px 	#808080 " }
    },
    React.createElement(
      "p",
      { className: "h6 text-muted text-center" },
      "Email us"
    ),
    React.createElement(
      "form",
      { className: "mt-5", onSubmit: handlesubmit },
      React.createElement(
        "span",
        { className: "p-float-label" },
        React.createElement(InputText, {
          name: "email",
          onChange: handleInputChange,
          style: { width: "100%" }
        }),
        React.createElement(
          "label",
          { htmlFor: "in" },
          "Email"
        )
      ),
      React.createElement(
        "p",
        { className: "h6 text-muted", style: { marginTop: "10px" } },
        " ",
        "Your Message"
      ),
      React.createElement(InputTextarea, {
        name: "msg",
        rows: 5,
        cols: 30,
        onChange: handleInputChange,
        autoResize: true,
        style: { width: "100%" }
      }),
      React.createElement(
        "button",
        {
          type: "submit",
          className: "btn btn-outline-primary btn-rounded form-control",
          "data-mdb-ripple-color": "dark"
          //   style={{ backgroundColor: "#55acee" }}
          , href: "#!",
          role: "button"
        },
        "Send"
      )
    )
  );
};

//call us Component
var CallUs = function CallUs() {
  var contact = {
    phones: ["08064790955", "08162472682"],
    emails: ["amnuhu91@gmail.com", "amnuhu91@yahoo.com"],
    chats: ["+2348064790955"]
  };
  return React.createElement(
    "div",
    { className: "pt-5" },
    React.createElement(
      "p",
      { className: "h6 text-muted text-center" },
      "Call/chat/email us on "
    ),
    React.createElement(
      "div",
      {
        className: "card p-4",
        style: { width: "100%", boxShadow: "5px 10px 10px 	#808080 " }
      },
      React.createElement(
        "ul",
        {
          className: "list-group list-group-flush",
          style: { fontSize: "1.2rem" }
        },
        contact.phones.map(function (phone, index) {
          return React.createElement(
            "li",
            { className: "list-group-item", key: index },
            React.createElement(
              "span",
              null,
              React.createElement("i", { className: "fa fa-phone" }),
              " ",
              "  ",
              phone
            )
          );
        })
      ),
      React.createElement(
        "ul",
        { className: "list-group list-group-flush" },
        contact.emails.map(function (email, index) {
          return React.createElement(
            "li",
            { className: "list-group-item", key: index },
            React.createElement(
              "span",
              null,
              React.createElement("i", { className: "fas fa-envelope" }),
              " ",
              email
            )
          );
        })
      ),
      React.createElement(
        "ul",
        { className: "list-group list-group-flush" },
        contact.chats.map(function (chat, index) {
          return React.createElement(
            "li",
            { className: "list-group-item", key: index },
            React.createElement("i", {
              className: "fa fa-whatsapp",
              style: { fontSize: "36px", color: " #25d366" }
            }),
            " ",
            React.createElement(
              "span",
              { style: { fontSize: "1.2rem" } },
              chat
            )
          );
        })
      )
    )
  );
};

var ContactComp = function ContactComp() {
  return React.createElement(
    "div",
    { className: "row mt-1" },
    React.createElement(
      "div",
      { className: "col-sm-12 col-md-8" },
      React.createElement(EmailUsComp, null)
    ),
    React.createElement(
      "div",
      { className: "col-sm-12 col-md-4 mt-1" },
      React.createElement(CallUs, null)
    )
  );
};

ReactDOM.render(React.createElement(ContactComp, null), document.getElementById('ct'));