import React from "react";
import {Image} from "react-bootstrap"
import { connect } from "react-redux";
import  yes from "../assets/owl4.jpeg"
class ProcessedImage extends React.Component{
    render(){
        return(
            <div>
                <h3>Our AI Calculated</h3>
               <Image src={this.props.fetchAIReduce.Image}/>
               <h4>{this.props.fetchAIReduce.Label}</h4>
           <audio controls>
  <source src="this.props.fetchAIReduce.Voice" type="audio/mpeg"/>
  Your browser does not support the audio tag.
</audio> 
              <div>
                  <p>
                 {this.props.fetchAIReduce.Body}
                 <a href="https://www.youtube.com/watch?v=oHg5SJYRHA0">Read More</a> </p>
              </div>
            </div>
        )
    }
}


const mapStateToProps = (state) => {
    console.log(state);
    return {
      fetchAIReduce: state.fetchAI,
    };
  };
  
  export default connect(mapStateToProps)(ProcessedImage);