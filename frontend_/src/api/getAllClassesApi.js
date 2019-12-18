import axios from "axios";
import ApiBaseUrl from "../config/config";

const getAllClassesApi = async () =>{

    const result = await axios({
      method: 'get',
      url: `${ApiBaseUrl}iris/all_classe/`,
      headers: {
        'Access-Control-Allow-Origin' : '*',
      }
    });
  console.log(result);
    return result;
}


export default getAllClassesApi