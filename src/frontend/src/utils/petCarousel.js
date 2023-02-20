import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Avatar } from '@mui/material';
import { LineAxisOutlined } from '@mui/icons-material';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

function handleNextClick(){
    // save the preference that just happened
    

    // const [currentItemIndex, setCurrentItemIndex] = useState(0);
    // const currentItem = items[currentItemIndex];
    // iterate the state of the card to the next item

    // return the next current pet from state
}



export default function petCarousel(imageUrl,petDescription,petName) {
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
        <Button variant="contained" style={{ backgroundColor: 'green', color: 'white' }} >Like</Button>
        <Button variant="outlined" style={{ backgroundColor: 'red', color: 'white' }} >Not For Me</Button>
      </CardActions>
    </Card>
  );
}




// import Box from '@mui/material/Box';
// import React from 'react';
// import Card from '@mui/material/Card';
// import CardActionArea from '@mui/material/CardActionArea';
// import CardActions from '@mui/material/CardActions';
// import CardContent from '@mui/material/CardContent';
// import CardMedia from '@mui/material/CardMedia';
// import Button from '@mui/material/Button';
// import Avatar from '@mui/material/Avatar';


// export default function PetImage(image_url, width, height) {
//     return (
//         <Box
//           sx={{
//             width: width,
//             height: height,
//           }}>
//           <img src='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60'
//           style={{
//             objectFit: 'cover',
//             width: '100%',
//           }}
//           alt='Adoptable Pet'
//           />
//         </Box>
//     );
//   }