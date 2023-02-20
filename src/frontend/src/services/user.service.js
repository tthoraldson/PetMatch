import axios from 'axios';
import { json } from 'react-router-dom';
import { BASE_API } from './base.service';

export function getUserData(userId) {
    // axios.get(`${BASE_API}petmatch/get_preferences/?user_id=${userId}`).then( response => {
    //     // load response.data from JSON to object
    //     const data = JSON.parse(response.data);
        
    //     data['user_preferences'] = JSON.parse(data.user_preferences.S)
    //     console.log(data)

    //     // get and assign the attribuets below from data.user_preferences to variables
    //     // const full_name = data.user_preferences.full_name ? data.user_preferences.full_name : 'None';
    //     // const email = data.user_preferences.email ? data.user_preferences.email : 'None';
    //     // const user_id = data.user_preferences.user_id ? data.user_preferences.user_id : 'None';
    //     // const zip_code = data.user_preferences.zip_code ? data.user_preferences.zip_code : 'None';
    //     // const readiness = data.user_preferences.readiness ? data.user_preferences.readiness : 'None';
    //     // const age = data.user_preferences.age ? data.user_preferences.age : 'None';
    //     // const g_expression = data.user_preferences.g_expression ? data.user_preferences.g_expression : 'None';
    //     // const has_current_pets = data.user_preferences.has_current_pets ? data.user_preferences.has_current_pets : 'None';
    //     // const current_pets = data.user_preferences.current_pets ? data.user_preferences.current_pets : 'None';
    //     // const dog_size = data.user_preferences.dog_size ? data.user_preferences.dog_size : 'None';
    //     // const dog_energy = data.user_preferences.dog_energy ? data.user_preferences.dog_energy : 'None';
    //     // const cat_size = data.user_preferences.cat_size ? data.user_preferences.cat_size : 'None';
    //     // const cat_energy = data.user_preferences.cat_energy ? data.user_preferences.cat_energy : 'None';
    //     // const user_prefs = data.user_preferences.user_prefs ? data.user_preferences.user_prefs : 'None';
        
    //     // // return the variables in a form that can be displayed in the component
    //     return {
    //         full_name: '',
    //         email: userId,
    //         user_id: userId,
    //         zip_code: 0,
    //         readiness: "not",
    //         age: 0,
    //         g_expression: 'f',
    //         has_current_pets: 'n',
    //         current_pets: '',
    //         dog_size: '',
    //         dog_energy: '',
    //         cat_size: '',
    //         cat_energy: '',
    //         user_prefs: []
    //     };  

    // }).catch(error => {
    //     console.error(error);
    // })
    return {
        full_name: '',
        email: userId,
        user_id: userId,
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

    console.log(data,'we are saving this \n')
    // const response = await axios.post(`${BASE_API}petmatch/put_preferences/`, data);
    // return response.data;  
}