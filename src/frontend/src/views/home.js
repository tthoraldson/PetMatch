import { useAuth0, withAuthenticationRequired } from '@auth0/auth0-react';
import { LineAxisOutlined } from '@mui/icons-material';
import Box from '@mui/material/Box';
import Loading from 'components/loading';
import React from 'react';
import { getCats } from 'services/cat.service';
import { getDogs } from 'services/dog.service';
import PetImage from 'utils/petImage';
// import { useLoaderData } from 'react-router-dom';
import Page from '../components/page';
import axios from 'axios';
import { json } from 'react-router-dom';
import { BASE_API } from '../services/base.service';
import petCarousel from '../utils/petCarousel.js';


export async function loader() {
  // TODO: Add api call here~
  return 'Hello World';


    // get user preferences
    // set user preferences

      // get new pet
}

export async function getNewPet(user){
  var cats = getCats(user)
  console.log(cats);
  getDogs(user)

  var userId = '000'
  var animal_type = 'cat'
  var option = 'collab'
  var pet_id = '58698691'

  // saveCatPreferences(null, null, null)
  // axios get request with url and query parameters
  axios.get(`${BASE_API}get_new_recommendation/${userId}/${animal_type}?option=${option}&animal_id=${pet_id}`).then (response => {
     const data = JSON.parse(response.data);

      console.log(data)

      // loop through the object, one by one, wait for a callback before moving on

  })

    // it should also have like and dislike buttons
    
  
  // , start with one. And then we will eventually have ten
  // then create another stepper function that will go through and display them in a component or something
}

export async function savePreference(){
  
}

export const Home = () => {

  const { user } = useAuth0();
  // var data = getNewPet(user);
  // console.log(data);
  // make an API request that gets pet recommendation(s) from this user with the query parameters as variables
  http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/get_new_recommendation/${userId}/{animal_type}?option={option}&animal_id={pet_id}

    return (
      <Page title='Home | PetMatch'>
        <Box sx={{width: 400}}>
          <PetImage image_url='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1336&q=80' width='300'/>

          {petCarousel()}

        </Box>
      </Page>
    );
}

export default withAuthenticationRequired(Home, {
  onRedirecting: () => <Loading />,
});


// import React, { useState } from 'react';

// const MyComponent = ({ items }) => {
//   const [currentItemIndex, setCurrentItemIndex] = useState(0);
//   const handleNextClick = () => {
//     setCurrentItemIndex((currentItemIndex + 1) % items.length);
//   };
//   const currentItem = items[currentItemIndex];

//   return (
//     <div>
//       <button onClick={handleNextClick}>Next</button>
//       <div>
//         <h2>{currentItem.name}</h2>
//         <img src={currentItem.full_photo} alt={currentItem.name} />
//         <p>{currentItem.pet_description}</p>
//         {/* display other properties as needed */}
//       </div>
//     </div>
//   );
// };

// export default MyComponent;
