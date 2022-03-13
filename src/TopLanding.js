const  { useState, useEffect } = React

const LandingComp = () => {
  const [company_info, setCompany_info] = useState({
    job_desc: "Providing IT Solution to Your Business.",
    slogan: "...be  ready for the future",
  });
  return (
    <div className="row">
      <div
        
        className="col-sm-12 col-md-12 p-5 contlanding "
        style={{
          backgroundColor: "white",
          border: "1px solid black",
          borderRadius: "5px",
          opacity: 0.8,
          boxShadow: "5px 10px 10px #390d04",
          transition: "0.5s",
        }}
      >
        <p className="h1" style={{ color: "black" }}>
          {company_info.job_desc}
        </p>
        <div className="d-flex justify-content-end ">
          <p className="small">{company_info.slogan}</p>
        </div>
        <div className="d-flex justify-content-around">
          <div>
           
            <p className="strong h6">connect with us on</p>
            <a
              style={{ color: "#3b5998", marginRight: "20px" }}
              href="#!"
              role="button"
            >
              <i className="fab fa-facebook-f fa-lg"></i>
            </a>

            <a
              style={{ color: "#55acee", marginRight: "20px" }}
              href="#!"
              role="button"
            >
              <i className="fab fa-twitter fa-lg"></i>
            </a>

            <a
              style={{ color: "#dd4b39", marginRight: "20px" }}
              href="#!"
              role="button"
            >
              <i className="fab fa-google fa-lg"></i>
            </a>
          </div>

          <button
            id="btns"
            className="btn btn-outline-secondary"
            data-mdb-ripple-color="dark"
          >
            Explore...
          </button>
        </div>
      </div>
    </div>
  );
};

ReactDOM.render(<LandingComp />,document.getElementById('toplanding'))


