import { useAuth0, withAuthenticationRequired } from '@auth0/auth0-react';
import { Box, Button, FormControl, FormControlLabel, FormLabel, Grid, Radio, RadioGroup, TextField } from '@mui/material';
import Loading from 'components/loading';
import React from 'react';
import { useNavigate } from 'react-router-dom';
import Page from '../components/page';
import { getUserData, saveUserData } from '../services/user.service';
  
export const Preferences = () => {
    const navigate = useNavigate();
    const { user } = useAuth0();
    const [catOrDog, updateCatOrDog] = React.useState(false); // true = cat, false = dog
    const data = getUserData(user.email);
    const [userPreferences, setUserPreferences] = React.useState(data);

    const goHome = (e) => {
        console.warn(userPreferences);
        navigate('/home');
    }

    const savePreferences = (e) => {
        console.warn(userPreferences);
        console.warn(saveUserData(userPreferences));
        navigate('/home');
    }

    function handleZipCodeChange(e){
        setUserPreferences({
            ...userPreferences,
            zip_code: e.target.value
        })
    }

    function handleAdoptChange(e){
        setUserPreferences({
            ...userPreferences,
            readiness: e.target.value
        })
    }

    function handleAgeChange(e){
        setUserPreferences({
            ...userPreferences,
            age: e.target.value
        })
    }

    function handleFullNameChange(e){
        setUserPreferences({
            ...userPreferences,
            full_name: e.target.value
        })
    }

    function handleGenderExpressionChange(e){
        setUserPreferences({
            ...userPreferences,
            g_expression: e.target.value
        })
    }

    function handleHasCurrentPetsChange(e){
        setUserPreferences({
            ...userPreferences,
            has_current_pets: e.target.value
        })
    }

    function handleCurrentPetsChange(e){
        setUserPreferences({
            ...userPreferences,
            current_pets: e.target.value
        })
    }

    function handleCatOrDogChange(e){
        updateCatOrDog(e.target.value);

    }

    function handleSizeChange(e){
        if (catOrDog){
            setUserPreferences({
                ...userPreferences,
                cat_size: e.target.value
            })
        } else {
            setUserPreferences({
                ...userPreferences,
                dog_size: e.target.value
            })
        }
    }

    function handleEnergyChange(e){
        if (catOrDog){
            setUserPreferences({
                ...userPreferences,
                cat_energy: e.target.value
            })
        } else {
            setUserPreferences({
                ...userPreferences,
                dog_energy: e.target.value
            })
        }
    }

    function handleUserPrefsChange(e){
        setUserPreferences({
            ...userPreferences,
            user_prefs: [e.target.value]
        })
    }
    
    return (
        <Page title='Preferences | Petmatch'>
            <Grid
            container
            spacing={0}
            direction="column"
            alignItems="center"
            justifyContent="center">
            <h1>Preferences</h1>
            <div
                style={{
                    display: 'block',
                    alignItems: "center",
                    width: 400
                }}>
                <FormControl sx={{ display: 'block', p:2, width: '100%' }}>
                <TextField disabled label="email" defaultValue={user.email} InputLabelProps={{ shrink: true}} sx={{ display: 'block', m:2, width:1}}/>
                <TextField label="Full Name" InputLabelProps={{ shrink: true}} sx={{ display: 'block', m:2 }} defaultValue={userPreferences.full_name} onChange={handleFullNameChange}/>
                <TextField label="Zip Code" InputLabelProps={{ shrink: true}} sx={{ display: 'block', m:2 }} defaultValue={userPreferences.zip} onChange={handleZipCodeChange}/>
                <Box sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">How ready are you to adopt?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        value={userPreferences.readiness ? userPreferences.readiness : "not"}
                        onChange={handleAdoptChange}
                        name="radio-buttons-group"
                    >
                        <FormControlLabel value="not" control={<Radio />} label="Not Ready" />
                        <FormControlLabel value="somewhat" control={<Radio />} label="Somewhat Ready" />
                        <FormControlLabel value="very" control={<Radio />} label="Very Ready" />
                        <FormControlLabel value="curious" control={<Radio />} label="Just Curious" />
                    </RadioGroup>
                </Box>

                <Box>
                <TextField sx={{ display: 'block', p:2 }}
                label="Age"
                type="number"
                defaultValue={userPreferences.age ? userPreferences.age : 25}
                onChange={handleAgeChange}
                InputLabelProps={{
                    shrink: true,
                }}
                />
                </Box>

                <Box sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">How do you Identify?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        value={userPreferences.g_expression ? userPreferences.g_expression : "m"}
                        onChange={handleGenderExpressionChange}
                        name="gender"
                    >
                        <FormControlLabel value="m" control={<Radio />} label="Male" />
                        <FormControlLabel value="f" control={<Radio />} label="Female" />
                        <FormControlLabel value="o" control={<Radio />} label="Other" />
                        <FormControlLabel value="n" control={<Radio />} label="N/A" />
                    </RadioGroup>
                </Box>

                <Box sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">Do you currently have any pets?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        value={userPreferences.has_current_pets ? userPreferences.has_current_pets : "n"}
                        onChange={handleHasCurrentPetsChange}
                        name="current-pets"
                    >
                        <FormControlLabel value="y" control={<Radio />} label="Yes" />
                        <FormControlLabel value="n" control={<Radio />} label="No" />
                    </RadioGroup>
                </Box>

                {userPreferences.has_current_pets === "y" &&
                    <Box sx={{ display: 'block', p:2 }}>
                        <FormLabel id="demo-radio-buttons-group-label">Do you have Cat(s) or Dog(s)?</FormLabel>
                        <RadioGroup
                            aria-labelledby="demo-radio-buttons-group-label"
                            value={userPreferences.current_pets ? userPreferences.current_pets : "n"}
                            onChange={handleCurrentPetsChange}
                            name="current-pets"
                        >
                            <FormControlLabel value="c" control={<Radio />} label="Cat(s)" />
                            <FormControlLabel value="d" control={<Radio />} label="Dog(s)" />
                            <FormControlLabel value="b" control={<Radio />} label="Both" />
                            <FormControlLabel value="n" control={<Radio />} label="None" />
                        </RadioGroup>
                    </Box>
                }
                
                <Box sx={{ display: 'block', p:2 }}>
                    <FormLabel id="demo-radio-buttons-group-label">What type of pet are you looking for?</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        value={catOrDog ? catOrDog : false}
                        onChange={handleCatOrDogChange}
                        name="seeking"
                    >
                        <FormControlLabel value={true} control={<Radio />} label="Cat" />
                        <FormControlLabel value={false} control={<Radio />} label="Dog" />
                    </RadioGroup>
                </Box>
                {catOrDog != null &&
                        <div>
                            <Box sx={{ display: 'block', p:2 }}>
                                <FormLabel id="demo-radio-buttons-group-label">What size pet are you looking for?</FormLabel>
                                <RadioGroup
                                    aria-labelledby="demo-radio-buttons-group-label"
                                    defaultValue="m"
                                    name="size"
                                    onChange={handleSizeChange}
                                >
                                    <FormControlLabel value="s" control={<Radio />} label="Small" />
                                    <FormControlLabel value="m" control={<Radio />} label="Medium" />
                                    <FormControlLabel value="l" control={<Radio />} label="Large" />
                                </RadioGroup>
                            </Box>

                            <Box sx={{ display: 'block', p:2 }}>
                                <FormLabel id="demo-radio-buttons-group-label">What level of energy are you looking for?</FormLabel>
                                <RadioGroup
                                    aria-labelledby="demo-radio-buttons-group-label"
                                    defaultValue="l"
                                    name="energy"
                                    onChange={handleEnergyChange}
                                >
                                    <FormControlLabel value="l" control={<Radio />} label="Low" />
                                    <FormControlLabel value="m" control={<Radio />} label="Medium" />
                                    <FormControlLabel value="h" control={<Radio />} label="High" />
                                </RadioGroup>
                            </Box>

                            <Box sx={{ display: 'block', p:2 }}>
                                <FormLabel id="demo-radio-buttons-group-label">Which of these would be ideal for your pet?</FormLabel>
                                <RadioGroup
                                    aria-labelledby="demo-radio-buttons-group-label"
                                    onChange={handleUserPrefsChange}
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
                            </Box>
                    </div>
                }
                </FormControl>
                <Button variant="contained" sx={{ m:1 }} onClick={savePreferences}>Save</Button>
                <Button variant="outlined" onClick={goHome}>Cancel</Button>
            </div>
            </Grid>
        </Page>
    )
}


export default withAuthenticationRequired(Preferences, {
    onRedirecting: () => <Loading />,
  });