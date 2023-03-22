import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Avatar, Grid } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import { BASE_API } from '../services/base.service';
import OpenInNewIcon from '@mui/icons-material/OpenInNew';

export const PetCarousel = function (props) {
    var pet = {
      pet_id: props.petData[0].pet_id,
      full_photo: props.petData[0].full_photo,
      description: props.petData[0].pet_description,
      name: props.petData[0]['attrs']['name'],
      url: props.petData[0]['attrs']['url']
    }

    const { user } = useAuth0();
    const [counter, setCounter] = useState(1) 
    const [currentPet, setCurrentPet] = useState(pet)
    const [petData, setPetData] = useState(props.petData)

    
    function SetNextPet() {
        // check counter is less than or equal to length of petData
        // setCounter(counter + 1);
        console.log('counter is: ', counter)
        console.warn('setNextPet called')
        var pet = {
            pet_id: props.petData[counter].pet_id,
            full_photo: props.petData[counter].full_photo,
            description: props.petData[counter].pet_description,
            name: props.petData[counter]['attrs']['name'],
            url: props.petData[counter]['attrs']['url']
        }

        // setCurrentPet(pet)
        
        // React.useEffect(() => {
        //     console.log('useEffect called')
        //     if (counter === props.petData.length) {
        //         console.log('counter is equal to length')
        //         // setCounter(0)
        //     }
        // });s

        return pet
    }

    // async function getNewPetsCheck() {
    //   if (counter === 9){
    //     console.log('counter is 9')
    //     //var new_pets = await getNewPets()
    //     //setPetData(new_pets)
    //     setCounter(0)
    //   }
    //   const response = await axios.get(`${BASE_API}/get_new_recommendation/${user.email}/cat?option=collab&animal_id=58698691`)
    //   if (!response || !response.data) {
    //     console.error('Error fetching data: ', response)
    //     throw new Error('Error fetching data')
    //   }
      
    //   var pet_info = JSON.parse(response.data);
    //   return pet_info
    // }

    const saveLikeRanking = () => {
        // code to save like preference here
        console.log('saving like ranking')
        var Like = axios.post(`${BASE_API}/petmatch/put_ranking`, {
            
            "user_id": user.email,
            "pet_id": currentPet.pet_id,
            "animal_type": "cat",
            "response": true
            
        })
        if (Like) {
          console.log('like ranking saved')
          var new_pet = SetNextPet()
          return new_pet
        } else {
            console.log('like ranking not saved')
            var new_pet = SetNextPet()
            return new_pet
            }
    };
    
    const saveDislikeRanking = () => {
        // code to save dislike preference here
        console.log('saving dislike ranking')
        var Dislike = axios.post(`${BASE_API}/petmatch/put_ranking`, {
            "user_id": user.email,
            "pet_id": currentPet.pet_id,
            "animal_type": "cat",
            "response": false
        })
        if (Dislike) {
          console.log('dislike ranking saved')
          var new_pet = SetNextPet()
          return new_pet
        } else {
            console.log('dislike ranking not saved')
            var new_pet = SetNextPet()
            return new_pet
            }
    };



  return (
    <>
        <Card sx={{ minWidth: 400, maxWidth: 600, marginTop: 10, alignItems: 'center' }}>
        <Grid container justifyContent="center">
          <Grid container justifyContent="center">
            <Avatar alt={currentPet.pet_id} src={currentPet.full_photo} sx={{ marginTop: 10, width: 300, height: 300, alignContent: 'center' }} /> 
          </Grid>
          <CardContent>
          <Grid container justifyContent="center">
            <Typography variant="h1" component="div">
                {currentPet.name}
            </Typography>
            </Grid>
            <Grid container justifyContent="center">
            <a href={currentPet.url}>
              <Typography>
                <OpenInNewIcon /> Visit Profile on PetFinder
              </Typography>
            </a>
            </Grid>
            <Grid container justifyContent="center">
            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                {currentPet.description}
            </Typography>
            </Grid>

            </CardContent>
          <Grid container justifyContent="center">
          <CardActions>
            <Button variant="contained" onClick={() => {setCounter(counter + 1); setCurrentPet(saveLikeRanking())}} style={{ backgroundColor: 'green', color: 'white' }} >Like</Button>
            <Button variant="outlined" onClick={() => {setCounter(counter + 1); setCurrentPet(saveDislikeRanking()); setCounter(counter + 1)}} style={{ backgroundColor: 'red', color: 'white' }} >Not For Me</Button>
          </CardActions>
          </Grid>
          </Grid>
        </Card>
    </>
  );
}
