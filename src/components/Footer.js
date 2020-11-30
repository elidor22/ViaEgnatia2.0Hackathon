import React from "react";
import logo from "../assets/Coloseu.png"
import "../assets/footer.css"
const Footer=()=>{
    return(
<div>
<div className="container-fluid pb-0 mb-0  justify-content-center text-light ">
<footer>
<div className="row my-1 justify-content-center py-1">
<div className="col-11">
    <div className="row ">
        <div className="col-xl-8 col-md-4 col-sm-4 col-12 my-auto mx-auto a">
            <h3 className="text-muted mb-md-0 mb-5 bold-text">Apollonia Assistant</h3>
        </div> 
        <div className="col-xl-2 col-md-4 col-sm-4 col-12">
        <img src={logo} width="150"
        height="150"
        alt="Responsive image"/>
                     </div>           
        <div className="col-xl-2 col-md-4 col-sm-4 col-12">
            <h6 className="mb-3 mb-lg-4 text-muted bold-text mt-sm-0 mt-5"><b>ADDRESS</b></h6>
            <p className="mb-1" style={{color:"black"}} >Tirane,Albania</p>
            <p style={{color:"black"}} >Yet to be decided</p>
        </div>
    </div>
    <div className="row ">
        <div className="col-xl-8 col-md-4 col-sm-4 col-auto my-md-0 mt-5 order-sm-1 order-3 align-self-end">
            <p className="social text-muted mb-0 pb-0 bold-text">  Apollonia AI Team All Rights Reserved.</p>
        </div>
        <div className="col-xl-2 col-md-4 col-sm-4 col-auto order-1 align-self-end ">

        </div>
        <div className="col-xl-2 col-md-4 col-sm-4 col-auto order-2 align-self-end mt-3 ">
        <h6 className="mt-55 mt-2 text-muted bold-text"><b>Apollonia Team</b></h6><small> <span><i className="fa fa-envelope" aria-hidden="true"></i></span> <div style={{color:"black"}} >gjonajarber@outlook.com</div></small>
        </div>
    </div>
</div>
</div>
</footer>
</div>
</div>
    )
}

export default Footer;
