import jsonPlaceholder from "../Axios/ApiServer"

export const fetchAI=(image)=>async dispatch=>{
   return await jsonPlaceholder.post('/upload', {
    image: image
  })
      .then(function (response) {
        console.log(response);
        dispatch({type:"FETCH_AI", payload:response.data})
      })
      .catch(function (error) {
        console.log(error);
      });

 };