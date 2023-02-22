import { useAuth0, withAuthenticationRequired } from '@auth0/auth0-react';
import { LineAxisOutlined } from '@mui/icons-material';
import Box from '@mui/material/Box';
import Loading from 'components/loading';
import React from 'react';
import { getCats } from 'services/cat.service';
import { getDogs } from 'services/dog.service';
import { useEffect, useState } from 'react';
import PetImage from 'utils/petImage';
// import { useLoaderData } from 'react-router-dom';
import Page from '../components/page';
import axios from 'axios';
import { json } from 'react-router-dom';
import { BASE_API } from '../services/base.service';
import PetCarousel from '../utils/petCarousel.js';
import { Grid } from '@mui/material';


export async function loader() {
  // TODO: Add api call here~
  return 'Hello World';


    // get user preferences
    // set user preferences

      // get new pet
}

async function getFirstPet() {
        
  // get the first ten pets from the API
  const response = await axios.get('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/get_new_recommendation/000/cat?option=collab&animal_id=58698691')
  if (!response || !response.data) {
    console.error('Error fetching data: ', response)
    throw new Error('Error fetching data')
  }
  // parse the ten returned pets from the response
  var pet_info = JSON.parse(response.data);
  // console.log(pet_info,'\n the pets info on load' );
  console.warn(pet_info)
  console.log(pet_info[0])
  var pet = {
    pet_id: pet_info[4].pet_id,
    full_photo: pet_info[4].full_photo,
    description: pet_info[4].pet_description,
    name: pet_info[4]['attrs']['name'],
    pet_info: pet_info
  }
  console.warn(pet)
  return pet  
}

async function getNewPet(user){

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

export const Home = function () {

  const [pet, setPet] = useState(null);
  const { user } = useAuth0();

  useEffect(() => {
    const fetchData = async () => {
      const petFromDB = await getFirstPet();
      console.log("petFromDB", petFromDB)

      if (petFromDB && petFromDB.full_photo) {
        setPet(petFromDB)
      }
    }

    fetchData()
  }, [])

  // var data = getNewPet(user);
  // console.log(data);
  // make an API request that gets pet recommendation(s) from this user with the query parameters as variables
  http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/get_new_recommendation/${userId}/{animal_type}?option={option}&animal_id={pet_id}

  return (
    <Page title='Home | PetMatch'>
      <Grid container justifyContent="center">
    {
      pet && pet.full_photo && (

        <PetCarousel petData={pet.pet_info} firstImage={pet.full_photo} petName={pet.name} petDescription={pet.description} petId={pet.pet_id} />
      )
    } 

      </Grid>
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
