import axios from 'axios';
import { BASE_API } from './base.service';

export function getCats(user){
    const user_id = user.email; 
    axios.get(`${BASE_API}get_new_recommendation/${user_id}/cat`, {params: {
        option: "collab", // FIXME: check local storage for option 
        animal_id: 0
    }}).then((response) => {
        return JSON.parse(response.data);
    }).catch((err) => {
        console.warn('An error happend when grabbing cat recommendations', err.message);
    });
}

export function saveCatPreferences(user, pet_id, preference){
    const data = {
        animal_id: pet_id,
        user_id: user.email,
        animal_type: "cat",
        response: preference
    }
    const response = axios.post(`${BASE_API}petmatch/put_ranking/`, data);
    return response;
}