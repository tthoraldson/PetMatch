import axios from 'axios';
import { json } from 'react-router-dom';
import { BASE_API } from './base.service';

export function getUserData(userId) {
    // TODO: Add functionality when get route is ready
    // const response = await axios.get(`${BASE_API}user`, {
    //     headers: {
    //     Authorization: `Bearer ${localStorage.getItem('token')}`,
    //     },
    // });
    
    // implement the get user service here 
    axios.get(`${BASE_API}petmatch/get_preferences/?user_id=${userId}`).then( response => {
        
        // load response.data from JSON to object
        const data = JSON.parse(response.data);
        
        data['user_preferences'] = JSON.parse(data.user_preferences.S)
        console.log(data)

        // get and assign the attribuets below from data.user_preferences to variables
        const full_name = data.user_preferences.full_name ? data.user_preferences.full_name : 'None';
        const email = data.user_preferences.email ? data.user_preferences.email : 'None';
        const user_id = data.user_preferences.user_id ? data.user_preferences.user_id : 'None';
        const zip_code = data.user_preferences.zip_code ? data.user_preferences.zip_code : 'None';
        const readiness = data.user_preferences.readiness ? data.user_preferences.readiness : 'None';
        const age = data.user_preferences.age ? data.user_preferences.age : 'None';
        const g_expression = data.user_preferences.g_expression ? data.user_preferences.g_expression : 'None';
        const has_current_pets = data.user_preferences.has_current_pets ? data.user_preferences.has_current_pets : 'None';
        const current_pets = data.user_preferences.current_pets ? data.user_preferences.current_pets : 'None';
        const dog_size = data.user_preferences.dog_size ? data.user_preferences.dog_size : 'None';
        const dog_energy = data.user_preferences.dog_energy ? data.user_preferences.dog_energy : 'None';
        const cat_size = data.user_preferences.cat_size ? data.user_preferences.cat_size : 'None';
        const cat_energy = data.user_preferences.cat_energy ? data.user_preferences.cat_energy : 'None';
        const user_prefs = data.user_preferences.user_prefs ? data.user_preferences.user_prefs : 'None';
        
        // return the variables in a form that can be displayed in the component
        return {
            full_name: full_name,
            email: email,
            user_id: user_id,
            zip_code: zip_code,
            readiness: readiness,
            age: age,
            g_expression: g_expression,
            has_current_pets: has_current_pets,
            current_pets: current_pets,
            dog_size: dog_size,
            dog_energy: dog_energy,
            cat_size: cat_size,
            cat_energy: cat_energy,
            user_prefs : data.user_preferences.user_prefs
        }

    }).catch(error => {
        console.error(error);
    })
}

export async function saveUserData(data) {
    const response = await axios.post(`${BASE_API}petmatch/put_preferences/`, data);
    return response.data;  
}