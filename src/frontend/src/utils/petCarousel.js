import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Avatar } from '@mui/material';
import axios from 'axios';
import PetImage from './petImage.js'
import { useEffect, useState } from 'react';



const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function PetCarousel(props) {

    const [currentImage, setCurrentImage] = useState(props.firstImage)
    const [currentPetId, setCurrentPetId] = useState('')
    const [currentDescription, setCurrentDescription] = useState('')
    const [currentPetName, setCurrentPetName] = useState('')
    const [counter, setCounter] = useState(0)
    

    // const [petInfo, setPetInfo] = useState({name: '', image: '', description: ''});
    // useEffect(() => {
    //   getFirstPet().then( pet => { setPetInfo(pet.data) })
    // });


    function setNextPet (response) {
        var pet_info = JSON.parse(JSON.parse(response.data));

            setCounter(counter + 1)
            console.log("PET INFO", pet_info[counter]);
            
            setCurrentPetId(pet_info[counter].pet_id)
            setCurrentImage(`${pet_info[counter].full_photo}.jpg`)
            setCurrentDescription(pet_info[counter].description)
            setCurrentPetName(pet_info[counter].name)

    }

    const saveLikeRanking = () => {
        // console.log("User liked this content");
        // code to save like preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
        // MOCKED TODO: replace with actual user_id and info
            "user_id": "000",
            "pet_id": currentPetId,
            "animal_type": "cat",
            "preference": true
            
        }).then( setNextPet )
    };
    
    const saveDislikeRanking = () => {
        // console.log("User disliked this content");
        // code to save dislike preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
        // MOCKED TODO: replace with actual user_id and info
            "user_id": "000",
            "pet_id": currentPetId,
            "animal_type": "cat",
            "preference": false
        }).then(setNextPet)
    };

  return (
    <Card sx={{ minWidth: 275 }}>
      {/* <Avatar alt='' src={currentImage} sx={{w:500}} />  */}
      < PetImage image_url={currentImage} />
      {/* <CardMedia
        component="img"
        height="194"
        image={`${currentImage}.jpg`}
        alt="Paella dish"
      /> */}
      <CardContent>
        <Typography variant="h1" component="div">
            {currentPetName}
        </Typography>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            {currentDescription}
        </Typography>
        </CardContent>
      <CardActions>
        <Button variant="contained" onClick={saveLikeRanking} style={{ backgroundColor: 'green', color: 'white' }} >Like</Button>
        <Button variant="outlined" onClick={saveDislikeRanking} style={{ backgroundColor: 'red', color: 'white' }} >Not For Me</Button>
      </CardActions>
    </Card>
  );
}
