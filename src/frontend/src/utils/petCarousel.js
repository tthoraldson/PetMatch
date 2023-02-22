import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Avatar, Container, Grid } from '@mui/material';
import axios from 'axios';
import PetImage from './petImage.js'
import { useEffect, useState } from 'react';
import { useAuth0 } from '@auth0/auth0-react';



const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function PetCarousel(props) {
    const { user } = useAuth0();
    const [currentImage, setCurrentImage] = useState(props.firstImage)
    const [currentPetId, setCurrentPetId] = useState(props.petId)
    const [currentDescription, setCurrentDescription] = useState(props.petDescription)
    const [currentPetName, setCurrentPetName] = useState(props.petName)
    const [counter, setCounter] = useState(0)

    function SetNextPet () {
        // get the first ten pets from the API
        // axios.get(`http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/get_new_recommendation/000/cat?option=collab&animal_id=${currentPetId}`).then(
        //   response => {
        //     console.warn(response.data)
        //   }
        // ).catch((error) => {
        //   console.warn('there was an error getting the next pet', error);
        // });
        setCounter(counter + 1);
        React.useEffect(() => {
          console.log(counter)
        }, [counter])
    }

    const saveLikeRanking = () => {
        // console.log("User liked this content");
        // code to save like preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
            "user_id": user.email,
            "pet_id": currentPetId,
            "animal_type": "cat",
            "preference": true
            
        }).then( SetNextPet )
        .catch((error) => {
          console.warn('there was an error saving the like ranking', error);
          SetNextPet();
        });
    };
    
    const saveDislikeRanking = () => {
        // console.log("User disliked this content");
        // code to save dislike preference here
        console.log(currentPetId);
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            "user_id": user.email,
            "pet_id": currentPetId,
            "animal_type": "cat",
            "preference": false
        }).then(SetNextPet)
        .catch((error) => {
          console.warn('there was an error saving the dislike ranking', error);
          SetNextPet();
        });
    };

  return (
    <Grid container justifyContent="center">
      <Card sx={{ minWidth: 400, maxWidth: 600, marginTop: 10, alignItems: 'center' }}>
      <Grid container justifyContent="center">
        <Avatar alt={currentPetId} src={currentImage} sx={{ marginTop: 10, width: 300, height: 300, alignContent: 'center' }} /> 
        <CardContent>
        <Grid container justifyContent="center">
          <Typography variant="h1" component="div">
              {currentPetName}
          </Typography>
          </Grid>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
              {currentDescription}
          </Typography>
          </CardContent>
        <CardActions>
          <Button variant="contained" onClick={saveLikeRanking} style={{ backgroundColor: 'green', color: 'white' }} >Like</Button>
          <Button variant="outlined" onClick={saveDislikeRanking} style={{ backgroundColor: 'red', color: 'white' }} >Not For Me</Button>
        </CardActions>
        </Grid>
      </Card>
    </Grid>
  );
}
