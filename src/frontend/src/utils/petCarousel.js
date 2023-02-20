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

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

// function handleNextClick(){
//     // save the preference that just happened
    

//     const [currentItemIndex, setCurrentItemIndex] = useState(0);
//     const currentItem = items[currentItemIndex];
//     // iterate the state of the card to the next item

//     // return the next current pet from state
// }



export default function petCarousel(imageUrl,petDescription,petName) {

    const saveLikeRanking = () => {
        console.log("User liked this content");
        // code to save like preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
        // MOCKED TODO: replace with actual user_id and info
            "user_id": "000",
            "pet_id": "string",
            "animal_type": "cat",
            "preference": true
            
        })
    };
    
    const saveDislikeRanking = () => {
        console.log("User disliked this content");
        // code to save dislike preference here
        axios.post('http://petmatch-alb-1418813607.us-east-1.elb.amazonaws.com:8086/petmatch/put_ranking', {
            
        // MOCKED TODO: replace with actual user_id and info
            "user_id": "000",
            "pet_id": "test",
            "animal_type": "cat",
            "preference": false
            
        })
    };

  return (
    <Card sx={{ minWidth: 275 }}>
      <Avatar alt='' src={imageUrl} sx={{w:500}} /> 
      <CardContent>
        <Typography variant="h1" component="div">
            {petName}
        </Typography>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            {petDescription}
        </Typography>
        </CardContent>
      <CardActions>
        <Button variant="contained" onClick={saveLikeRanking} style={{ backgroundColor: 'green', color: 'white' }} >Like</Button>
        <Button variant="outlined" onClick={saveDislikeRanking} style={{ backgroundColor: 'red', color: 'white' }} >Not For Me</Button>
      </CardActions>
    </Card>
  );
}
