import React from "react";
import {Image} from "react-bootstrap"
import { connect } from "react-redux";
import  yes from "../assets/owl4.jpeg"
class ProcessedImage extends React.Component{
    render(){
        return(
            <div>
                <h3>Our AI Calculated</h3>
               <Image  src={this.props.fetchAIReduce.original_image} width="500px"/>
               <Image  src={this.props.fetchAIReduce.predicted_image} width="500px"/>
               <h4>{this.props.fetchAIReduce.label}</h4>
               <p>{this.props.fetchAIReduce.description}</p>
           <audio controls>
  <source src={this.props.fetchAIReduce.english} type="audio/mpeg"/>
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