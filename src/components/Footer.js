import React from "react";
import logo from "../assets/Coloseu.png"
import "../assets/footer.css"
const Footer=()=>{
    return(
<div>
<div class="container-fluid pb-0 mb-0  justify-content-center text-light ">
<footer>
<div class="row my-1 justify-content-center py-1">
<div class="col-11">
    <div class="row ">
        <div class="col-xl-8 col-md-4 col-sm-4 col-12 my-auto mx-auto a">
            <h3 class="text-muted mb-md-0 mb-5 bold-text">Apollonia Assistant</h3>
        </div> 
        <div class="col-xl-2 col-md-4 col-sm-4 col-12">
        <img src={logo} width="150"
        height="150"
        alt="Responsive image"/>
                     </div>           
        <div class="col-xl-2 col-md-4 col-sm-4 col-12">
            <h6 class="mb-3 mb-lg-4 text-muted bold-text mt-sm-0 mt-5"><b>ADDRESS</b></h6>
            <p class="mb-1" style={{color:"black"}} >Tirane,Albania</p>
            <p style={{color:"black"}} >Yet to be decided</p>
        </div>
    </div>
    <div class="row ">
        <div class="col-xl-8 col-md-4 col-sm-4 col-auto my-md-0 mt-5 order-sm-1 order-3 align-self-end">
            <p class="social text-muted mb-0 pb-0 bold-text"> <span class="mx-2"><i class="fa fa-facebook" aria-hidden="true"></i></span> <span class="mx-2"><i class="fa fa-linkedin-square" aria-hidden="true"></i></span> <span class="mx-2"><i class="fa fa-twitter" aria-hidden="true"></i></span> <span class="mx-2"><i class="fa fa-instagram" aria-hidden="true"></i></span> </p><small class="rights"><span>&#174;</span> Apollonia AI Team All Rights Reserved.</small>
        </div>
        <div class="col-xl-2 col-md-4 col-sm-4 col-auto order-1 align-self-end ">

        </div>
        <div class="col-xl-2 col-md-4 col-sm-4 col-auto order-2 align-self-end mt-3 ">
        <h6 class="mt-55 mt-2 text-muted bold-text"><b>Apollonia Team</b></h6><small> <span><i class="fa fa-envelope" aria-hidden="true"></i></span> <div style={{color:"black"}} >gjonajarber@outlook.com</div></small>
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
