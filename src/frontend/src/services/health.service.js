const HealthService = () => {
        // TODO: Need to get prod API base URL
        const baseApi = process.env.NODE_ENV === 'development' ? 'http://localhost:8086/' : '';
        return fetch(baseApi)
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