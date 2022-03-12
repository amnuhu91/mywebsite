const { useState } = React
const { InputText } =primereact.inputtext
const { InputTextarea } = primereact.inputtextarea



//Email Component
const EmailUsComp = () => {
  const [message, setMessage] = useState({});
  const handleInputChange = (e) => {
    const target = e.target;
    const value = target.value;
    const name = target.name;

    setMessage({ ...message, [name]: value });
  };
  const handlesubmit = (e) => {
    e.preventDefault();
    // console.log("message", message);
  };

  //console.log(message);
  return (
    <div
      className="card p-5"
      style={{ width: "100%", boxShadow: "5px 10px 10px 	#808080 " }}
    >
      <p className="h6 text-muted text-center">Email us</p>
      <form className="mt-5" onSubmit={handlesubmit}>
        <span className="p-float-label">
          <InputText
            name="email"
            onChange={handleInputChange}
            style={{ width: "100%" }}
          />
          <label htmlFor="in">Email</label>
        </span>
        <p className="h6 text-muted" style={{ marginTop: "10px" }}>
          {" "}
          Your Message
        </p>
        <InputTextarea
          name="msg"
          rows={5}
          cols={30}
          onChange={handleInputChange}
          autoResize
          style={{ width: "100%" }}
        />
        <button
          type="submit"
          className="btn btn-outline-primary btn-rounded form-control"
          data-mdb-ripple-color="dark"
          //   style={{ backgroundColor: "#55acee" }}
          href="#!"
          role="button"
        >
          Send
        </button>
      </form>
    </div>
  );
};

//call us Component
const CallUs = () => {
  const contact = {
    phones: ["08064790955", "08162472682"],
    emails: ["amnuhu91@gmail.com", "amnuhu91@yahoo.com"],
    chats: ["+2348064790955"],
  }
  return (
    <div className="pt-5">
      <p className="h6 text-muted text-center">Call/chat/email us on </p>
      <div
        className="card p-4"
        style={{ width: "100%", boxShadow: "5px 10px 10px 	#808080 " }}
      >
        <ul
          className="list-group list-group-flush"
          style={{ fontSize: "1.2rem" }}
        >
          {contact.phones.map((phone, index) => (
            <li className="list-group-item" key={index}>
              <span>
                <i className="fa fa-phone"></i> {"  "}
                {phone}
              </span>
            </li>
          ))}
        </ul>
        <ul className="list-group list-group-flush">
          {contact.emails.map((email, index) => (
            <li className="list-group-item" key={index}>
              <span>
                <i className="fas fa-envelope"></i> {email}
              </span>
            </li>
          ))}
        </ul>
        <ul className="list-group list-group-flush">
          {contact.chats.map((chat, index) => (
            <li className="list-group-item" key={index}>
              <i
                className="fa fa-whatsapp"
                style={{ fontSize: "36px", color: " #25d366" }}
              ></i>{" "}
              <span style={{ fontSize: "1.2rem" }}>{chat}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}


const ContactComp = () => {
    return (
      <div className="row mt-1">
        <div className="col-sm-12 col-md-8">
          <EmailUsComp />
        </div>
  
        <div className="col-sm-12 col-md-4 mt-1">
          <CallUs />
        </div>
      </div>
    );
  }
  

  ReactDOM.render(<ContactComp />,document.getElementById('ct'))