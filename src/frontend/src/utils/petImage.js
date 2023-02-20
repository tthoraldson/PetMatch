import Box from '@mui/material/Box';
import React from 'react';

export default function PetImage(props) {
    return (
        <Box
          sx={{
            width: props['width'],
            height: props['height'],
          }}>
          <img src={props['image_url']}
          style={{
            objectFit: 'cover',
            width: '100%',
          }}
          alt='Adoptable Pet'
          />
        </Box>
    );
  }