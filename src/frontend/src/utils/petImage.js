import * as React from 'react';

export default function PetImage(image_url) {
    return (
        <img src='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60'
        style={{
          maxHeight: 500,
        }}
        alt='Adoptable Pet'
        />
    );
  }