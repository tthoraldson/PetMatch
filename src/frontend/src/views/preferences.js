import { useAuth0, withAuthenticationRequired } from '@auth0/auth0-react';
import { Box, FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, TextField } from '@mui/material';
import Loading from 'components/loading';
import React from 'react';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
export const Preferences = () => {
    const { user } = useAuth0();
    console.warn(user);
    
    return (
        <Page title='Preferences | Petmatch'>
            <Box
                component="form"
                sx={{
                    '& .MuiTextField-root': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
                >
                <TextField disabled label="Name" InputLabelProps={{
                shrink: true,
            }}/>
                <TextField disabled label="Email" InputLabelProps={{
                shrink: true,
            }}/>
                <TextField label="ZipCode" InputLabelProps={{
                shrink: true,
            }}/>
                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">How ready are you to adopt?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="not"
                        name="radio-buttons-group"
                    >
                        <FormControlLabel value="not" control={<Radio />} label="Not Ready" />
                        <FormControlLabel value="somewhat" control={<Radio />} label="Somewhat Ready" />
                        <FormControlLabel value="very" control={<Radio />} label="Very Ready" />
                        <FormControlLabel value="curious" control={<Radio />} label="Just Curious" />
                    </RadioGroup>
                </FormControl>

                    <TextField
            label="Age"
            type="number"
            InputLabelProps={{
                shrink: true,
            }}
            />
                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">How do you Identify?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="f"
                        name="radio-buttons-group"
                    >
                        <FormControlLabel value="m" control={<Radio />} label="Male" />
                        <FormControlLabel value="f" control={<Radio />} label="Female" />
                        <FormControlLabel value="o" control={<Radio />} label="Other" />
                        <FormControlLabel value="n" control={<Radio />} label="N/A" />
                    </RadioGroup>
                </FormControl>

                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">How do you Identify?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="f"
                        name="radio-buttons-group"
                    >
                        <FormControlLabel value="m" control={<Radio />} label="Male" />
                        <FormControlLabel value="f" control={<Radio />} label="Female" />
                        <FormControlLabel value="o" control={<Radio />} label="Other" />
                        <FormControlLabel value="n" control={<Radio />} label="N/A" />
                    </RadioGroup>
                </FormControl>
            </Box>
        </Page>
    )
}


export default withAuthenticationRequired(Preferences, {
    onRedirecting: () => <Loading />,
  });