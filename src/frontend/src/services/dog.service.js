import axios from 'axios';
import { BASE_API } from "./base.service";

// use content model till there are 5 likes
export function getDogs(user){
    console.log('starting get dogs');
    const user_id = user.email;
    axios.get(`${BASE_API}get_new_recommendation/${user_id}/dog`, {params: {
        option: "collab", // FIXME: check local storage for option
        animal_id: 0
    }}).then((response) => {
        return JSON.parse(response.data);
    }).catch((err) => {
        console.error('an error happened when getting dog recommendations', err.message);
    });
}

export function saveDogPreferences(user, pet_id, preference){
    const data = {
        user_id: user.email,
        pet_id: pet_id,
        animal_type: "dog",
        preference: preference
    }
    const response = axios.post(`${BASE_API}petmatch/put_ranking/`, data);
    return response;
}