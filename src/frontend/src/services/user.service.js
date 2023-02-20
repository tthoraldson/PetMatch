import axios from 'axios';
import { BASE_API } from './base.service';

export function getUserData(user) {
    // TODO: Add functionality when get route is ready
    // const response = await axios.get(`${BASE_API}user`, {
    //     headers: {
    //     Authorization: `Bearer ${localStorage.getItem('token')}`,
    //     },
    // });
    return {
        full_name: '',
        email: user.email,
        user_id: user.email,
        zip_code: 0,
        readiness: "not",
        age: 0,
        g_expression: 'f',
        has_current_pets: 'n',
        current_pets: '',
        dog_size: '',
        dog_energy: '',
        cat_size: '',
        cat_energy: '',
        user_prefs: []
    };   
}

export async function saveUserData(data) {
    const response = await axios.post(`${BASE_API}petmatch/put_preferences/`, data);
    return response.data;  
}