import axios from 'axios';
import { BASE_API } from "./base.service";

export function getDogs(user){
    const user_id = user.email;
    const response = axios.get(`${BASE_API}get_new_reccomendation/${user_id}/dog`, {params: {
        option: "collab",
        animal_id: 1234
    }});
    return response;
}

export function saveDogPreferences(pet_id, user_id, preference){
    const data = {
        user_id: user_id,
        pet_id: pet_id,
        animal_type: "dog",
        preference: preference
    }
    const response = axios.post(`${BASE_API}petmatch/put_ranking/`, data);
    return response;
}