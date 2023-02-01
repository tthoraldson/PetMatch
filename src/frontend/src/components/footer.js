import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

export default function Footer() {
    return (
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
        }}>
        <CssBaseline />
        <Box
          component="footer"
          sx={{
            position: "fixed", 
            width: "100%",
            minHeight: "5vh",
            mt: "1vh",
            bottom: 0,
            backgroundColor: (theme) =>
              theme.palette.mode === 'light'
                ? theme.palette.grey[200]
                : theme.palette.grey[800],
          }}
        >
          <Container maxWidth="sm">
            <center>
            <Typography variant="body1">
              Made with ❤️ by the Petmatch Team @ FourthBrain
            </Typography>
            </center>
          </Container>
        </Box>
      </Box>
    );
}