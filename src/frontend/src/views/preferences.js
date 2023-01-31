import { useAuth0, withAuthenticationRequired } from '@auth0/auth0-react';
import { Box, Button, FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, TextField } from '@mui/material';
import Loading from 'components/loading';
import React from 'react';
import Page from '../components/page';

export async function loader() {
    // TODO: Add api call here~
    return 'Hello World';
  }
  
export const Preferences = () => {
    const { user } = useAuth0();

    const goHome = () => {
        console.warn('hit');
    }
    
    return (
        <Page title='Preferences | Petmatch'>
            <h1>Preferences</h1>
            <Box
                component="form"
                sx={{
                    // '& .MuiTextField-root': { m: 1, width: '200ch' },
                    display: 'block',
                    alignItems: "center",
                    justify: "center",
                }}
                noValidate
                autoComplete="off"
                >
                <TextField disabled label="Username" defaultValue={user.name} InputLabelProps={{
                shrink: true,
            }} sx={{ display: 'block', m:2}}/>
                <TextField label="Zip Code" InputLabelProps={{
                shrink: true,
            }} sx={{ display: 'block', m:2 }}/>
                <FormControl sx={{ display: 'block', p:2 }}>
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

                <TextField sx={{ display: 'block', p:2 }}
                label="Age"
                type="number"
                InputLabelProps={{
                    shrink: true,
                }}
                />

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">How do you Identify?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="f"
                        name="gender"
                    >
                        <FormControlLabel value="m" control={<Radio />} label="Male" />
                        <FormControlLabel value="f" control={<Radio />} label="Female" />
                        <FormControlLabel value="o" control={<Radio />} label="Other" />
                        <FormControlLabel value="n" control={<Radio />} label="N/A" />
                    </RadioGroup>
                </FormControl>

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">Do you currently have any pets?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="y"
                        name="current-pets"
                    >
                        <FormControlLabel value="y" control={<Radio />} label="Yes" />
                        <FormControlLabel value="n" control={<Radio />} label="No" />
                    </RadioGroup>
                </FormControl>

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">Do you have Cat(s) or Dog(s)?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="n"
                        name="current-pets"
                    >
                        <FormControlLabel value="c" control={<Radio />} label="Cat(s)" />
                        <FormControlLabel value="d" control={<Radio />} label="Dog(s)" />
                        <FormControlLabel value="b" control={<Radio />} label="Both" />
                        <FormControlLabel value="n" control={<Radio />} label="None" />
                    </RadioGroup>
                </FormControl>

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">What type of pet are you looking for?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="c"
                        name="seeking"
                    >
                        <FormControlLabel value="c" control={<Radio />} label="Cat" />
                        <FormControlLabel value="d" control={<Radio />} label="Dog" />
                    </RadioGroup>
                </FormControl>

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">What size pet are you looking for?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="m"
                        name="size"
                    >
                        <FormControlLabel value="s" control={<Radio />} label="Small" />
                        <FormControlLabel value="m" control={<Radio />} label="Medium" />
                        <FormControlLabel value="l" control={<Radio />} label="Large" />
                    </RadioGroup>
                </FormControl>

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">What level of energy are you looking for?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue="l"
                        name="energy"
                    >
                        <FormControlLabel value="l" control={<Radio />} label="Low" />
                        <FormControlLabel value="m" control={<Radio />} label="Medium" />
                        <FormControlLabel value="h" control={<Radio />} label="High" />
                    </RadioGroup>
                </FormControl>

                <FormControl sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">Which of these would be ideal for your pet?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="energy"
                    >
                        <FormControlLabel value="0" control={<Radio />} label="Spayed or Neutered" />
                        <FormControlLabel value="1" control={<Radio />} label="House Trained" />
                        <FormControlLabel value="2" control={<Radio />} label="Has claws (Cats)" />
                        <FormControlLabel value="3" control={<Radio />} label="Declawed (Cats)" />
                        <FormControlLabel value="4" control={<Radio />} label="I would care for an animal with special needs" />
                        <FormControlLabel value="5" control={<Radio />} label="Has its shots" />
                        <FormControlLabel value="6" control={<Radio />} label="Good with kids" />
                        <FormControlLabel value="7" control={<Radio />} label="Good with other animals" />
                        <FormControlLabel value="8" control={<Radio />} label="Bonded Pairs" />
                        <FormControlLabel value="9" control={<Radio />} label="Senior" />
                        <FormControlLabel value="10" control={<Radio />} label="Youth" />
                        <FormControlLabel value="11" control={<Radio />} label="Adolescent" />
                        <FormControlLabel value="12" control={<Radio />} label="OK with an animal in recovery" />
                        <FormControlLabel value="13" control={<Radio />} label="Quiet" />
                        <FormControlLabel value="14" control={<Radio />} label="Talkative" />
                    </RadioGroup>
                </FormControl>
                <Button variant="contained" sx={{ m:1 }} onClick={goHome}>Save</Button>
                <Button variant="outlined" onClick={goHome}>Cancel</Button>
            </Box>
        </Page>
    )
}


export default withAuthenticationRequired(Preferences, {
    onRedirecting: () => <Loading />,
  });