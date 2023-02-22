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

export const PetCarousel = function (props) {

    console.log(props,'these are the props')

    const { user } = useAuth0();
    const [currentImage, setCurrentImage] = useState(props.firstImage)
    const [currentPetId, setCurrentPetId] = useState(props.petId)
    const [currentDescription, setCurrentDescription] = useState(props.petDescription)
    const [currentPetName, setCurrentPetName] = useState(props.petName)
    const [counter, setCounter] = useState(0)         

    function SetNextPet () {

        setCounter(counter + 1);
        setCurrentImage(props.petData[counter].full_photo)
        setCurrentPetId(props.petData[counter].pet_id)
        setCurrentDescription(props.petData[counter].pet_description)
        setCurrentPetName(props.petData[counter].name)
        
        React.useEffect(() => {
            console.log('useEffect called')
            if (counter === props.petData.length) {
                console.log('counter is equal to length')
                setCounter(0)
            }
        }, [counter, currentImage, currentPetId, currentDescription, currentPetName])
    }

    const saveLikeRanking = () => {
        // code to save like preference here
        console.log('saving like ranking')
        var Like = axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
            "user_id": user.email,
            "pet_id": currentPetId,
            "animal_type": "cat",
            "preference": true
            
        })
        if (Like) {
          console.log('like ranking saved')
          SetNextPet()
        } else {
            console.log('like ranking not saved')
            }
    };
    
    const saveDislikeRanking = () => {
        // code to save dislike preference here
        console.log('saving dislike ranking')
        var Dislike = axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            "user_id": user.email,
            "pet_id": currentPetId,
            "animal_type": "cat",
            "preference": false
        })
        if (Dislike) {
          console.log('dislike ranking saved')
          SetNextPet()
        } else {
            console.log('dislike ranking not saved')
            }
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
