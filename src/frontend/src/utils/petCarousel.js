import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Avatar } from '@mui/material';
import { LineAxisOutlined } from '@mui/icons-material';
import axios from 'axios';
import PetImage, {petImage} from './petImage.js'
import CardMedia from '@mui/material/CardMedia';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

const pets = [1,2,3,4,5]

// function savePreferenceGetNewPet(){
//     // save the preference that just happened
    

//     const [currentItemIndex, setCurrentItemIndex] = useState(0);
//     const currentItem = items[currentItemIndex];
//     // iterate the state of the card to the next item

//     // return the next current pet from state
// }

export default function petCarousel(props) {
    
    var currentImage
    var currentDescription
    var currentPetName
    var currentPetId

    const getFirstPet = () => {
        
        // get the first ten pets from the API
        axios.get('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/get_new_recommendation/000/cat?option=collab&animal_id=58698691').then( response => {
            
            // parse the ten returned pets from the response
            var pet_info = JSON.parse(response.data);
            console.log(pet_info,'\n the pets info on load' );
            
            currentPetId = pet_info[0].pet_id
            currentImage = `${pet_info[0].full_photo}.jpg`
            // console.log(currentImage,'\n the current image on load')
            currentDescription = pet_info[0].description
            currentPetName = pet_info[0].name

        })
    }

    getFirstPet()

    const saveLikeRanking = () => {
        // console.log("User liked this content");
        // code to save like preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
        // MOCKED TODO: replace with actual user_id and info
            "user_id": "000",
            "pet_id": "string",
            "animal_type": "cat",
            "preference": true
            
        }).then( response => {
            
            // parse the ten returned pets from the response
            var pet_info = JSON.parse(response.data);
            console.log(pet_info,'\n the pets info after like' );
            
            currentPetId = pet_info[0].pet_id
            currentImage = `${pet_info[0].full_photo}.jpg`
            currentDescription = pet_info[0].description
            currentPetName = pet_info[0].name
        })
    };
    
    const saveDislikeRanking = () => {
        // console.log("User disliked this content");
        // code to save dislike preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
        // MOCKED TODO: replace with actual user_id and info
            "user_id": "000",
            "pet_id": "test",
            "animal_type": "cat",
            "preference": false
        }).then( response => {
            
            // parse the ten returned pets from the response
            var pet_info = JSON.parse(response.data);
            // console.log(pet_info,'\n the pets info after dislike' );

            currentPetId = pet_info[0].pet_id
            currentImage = `${pet_info[0].full_photo}.jpg`
            currentDescription = pet_info[0].description
            currentPetName = pet_info[0].name
        })
    };

  return (
    <Card sx={{ minWidth: 275 }}>
      {/* <Avatar alt='' src={currentImage} sx={{w:500}} />  */}
      < PetImage image_url={currentImage} width={500} height={500} />
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
