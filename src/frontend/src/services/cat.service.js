import axios from 'axios';
import { BASE_API } from './base.service';

export function getCats(user){
    console.log('starting get cats');
    const user_id = 'Denise';
    const response = axios.get(`${BASE_API}get_new_recommendation/${user_id}/cat`, {params: {
        option: "collab",
        animal_id: 1234
    }});

    console.warn(response);
    return response;
}

export function saveCatPreferences(pet_id, user_id, preference){
    const data = {
        // user_id: user_id,
        // pet_id: pet_id,
        animal_id: 58903660,
        pet_id: 58903660,
        user_id: 'Denise',
        animal_type: "cat",
        // preference: preference
        response: true
    }
    const response = axios.post(`${BASE_API}petmatch/put_ranking/`, data);
    return response;
}