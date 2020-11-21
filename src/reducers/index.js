
import { combineReducers } from "redux";
const fetchAIReducer = (image = null, action) => {
    if (action.type === "FETCH_AI") {
      return action.payload;
    }
  
    return image;
  };
  export default combineReducers({
    fetchAI: fetchAIReducer,
  });