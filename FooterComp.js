var FooterComp = function FooterComp() {
  return React.createElement(
    "div",
    null,
    React.createElement(
      "footer",
      { className: "text-center text-lg-start bg-dark text-white pt-1 mt-3" },
      React.createElement(
        "section",
        { className: "" },
        React.createElement(
          "div",
          { className: "container text-center text-md-start mt-5" },
          React.createElement(
            "div",
            { className: "row mt-3" },
            React.createElement(
              "div",
              { className: "col-md-3 col-lg-4 col-xl-3 mx-auto mb-4" },
              React.createElement(
                "h6",
                { className: "text-uppercase fw-bold mb-4" },
                React.createElement("i", { className: "fas fa-gem me-3" }),
                "AmnSolution"
              ),
              React.createElement(
                "p",
                null,
                "Here you can use rows and columns to organize your footer content. Lorem ipsum dolor sit amet, consectetur adipisicing elit."
              )
            ),
            React.createElement(
              "div",
              { className: "col-md-2 col-lg-2 col-xl-2 mx-auto mb-4" },
              React.createElement(
                "h6",
                { className: "text-uppercase fw-bold mb-4" },
                "Products"
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Angular"
                )
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "React"
                )
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Vue"
                )
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Laravel"
                )
              )
            ),
            React.createElement(
              "div",
              { className: "col-md-3 col-lg-2 col-xl-2 mx-auto mb-4" },
              React.createElement(
                "h6",
                { className: "text-uppercase fw-bold mb-4" },
                "Useful links"
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Pricing"
                )
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Settings"
                )
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Orders"
                )
              ),
              React.createElement(
                "p",
                null,
                React.createElement(
                  "a",
                  { href: "#!", className: "text-reset" },
                  "Help"
                )
              )
            ),
            React.createElement(
              "div",
              { className: "col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4" },
              React.createElement(
                "h6",
                { className: "text-uppercase fw-bold mb-4" },
                "Contact"
              ),
              React.createElement(
                "p",
                null,
                React.createElement("i", { className: "fas fa-home me-3" }),
                " New York, NY 10012, US"
              ),
              React.createElement(
                "p",
                null,
                React.createElement("i", { className: "fas fa-envelope me-3" }),
                "info@example.com"
              ),
              React.createElement(
                "p",
                null,
                React.createElement("i", { className: "fas fa-phone me-3" }),
                " + 01 234 567 88"
              ),
              React.createElement(
                "p",
                null,
                React.createElement("i", { className: "fas fa-print me-3" }),
                " + 01 234 567 89"
              )
            )
          )
        )
      ),
      React.createElement(
        "div",
        {
          className: "text-center p-4",
          style: { backgroundColor: "rgba(0, 0, 0, 0.05)" }
        },
        "\xA9 2021 Copyright:",
        React.createElement(
          "a",
          { className: "text-reset fw-bold", href: "https://mdbootstrap.com/" },
          "amnsolution.com"
        )
      )
    )
  );
};

ReactDOM.render(React.createElement(FooterComp, null), document.getElementById('footer'));