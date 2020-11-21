import React from "react"
import {Form,Image,Button} from "react-bootstrap"
class ImageInput extends React.Component{
    
    constructor(props) {
        super(props);
        this.state = {file: '',imagePreviewUrl: ''};
      }

    _handleImageChange(e) {
        e.preventDefault();
    
        let reader = new FileReader();
        let file = e.target.files[0];
    
        reader.onloadend = () => {
          this.setState({
            file: file,
            imagePreviewUrl: reader.result
          });
        }
    
        reader.readAsDataURL(file)
      }
    render(){
        let {imagePreviewUrl} = this.state;
        let $imagePreview = null;
        if (imagePreviewUrl) {
          $imagePreview = (<Image style={{maxWidth:"600px",
       maxHeight:"600px"}}  
           fluid src={imagePreviewUrl} />);
        } else {
          $imagePreview = (<div className="previewText">Please select an Image for our AI to calculate</div>);
        }
        return(
            <div>
                <h2>Please Input Image</h2>
                <div class="custom-file" >
    <Form.File className="w-90 h-90 custom-file-input"   type="image" id="exampleFormControlFile1" label="Example file input"  onChange={(e)=>this._handleImageChange(e)}/>
    <label class="custom-file-label" for="inputGroupFile01">Choose image</label>
    </div>

<div className="imgPreview">
          {$imagePreview}
        </div>
        <Button style={{margin:"20px"}} ariant="outline-primary">Calculate</Button>
            </div>
            
        )
    }
    
}
export default ImageInput;