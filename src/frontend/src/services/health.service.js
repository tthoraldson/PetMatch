import { BASE_API } from './base.service';

const HealthService = () => { 
        return fetch(BASE_API)
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then((response) => response)
            .catch((error) => {
                console.error(
                    'There has been a problem with your fetch operation:',
                    error
                );
    });
}

export default HealthService;