import React from "react"
import ImageInput from "./ImageInput"
import ProcessedImage from "./ProcessedImage"
import Header from "../components/Header"
class Main extends React.Component{
    
    render(){
        return(
            <div class="container text-center">
                <Header/>
<ImageInput/>
<ProcessedImage/>
            </div>
        )
    }
    
}
export default Main;