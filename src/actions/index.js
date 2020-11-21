import jsonPlaceholder from "../Axios/ApiServer"

export const fetchAI=(image)=>async dispatch=>{
    const response=await jsonPlaceholder.post('/user', {
        image: image
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    dispatch({type:"FETCH_AI", payload:response.data})
 };