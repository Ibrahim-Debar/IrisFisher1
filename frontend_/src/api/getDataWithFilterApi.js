
import axios from "axios";
import ApiBaseUrl from "../config/config";


const getDataWithFilterApi = async (classe) =>{

    const result = await axios({
      method: 'get',
      url: `${ApiBaseUrl}iris/classe/${classe}/`,
      headers: {
        'Access-Control-Allow-Origin' : '*',
      }
    });
  
    return result;
}


export default getDataWithFilterApi