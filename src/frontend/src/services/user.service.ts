import axios from 'axios';
import { BASE_API } from './base.service';

const getUserData = async () => {
    const response = await axios.get(`${BASE_API}user`, {
        headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
    });
    return response.data;   
}

export default getUserData;