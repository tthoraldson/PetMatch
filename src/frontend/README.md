# PetMatch Web App~
- `npm install`
- create `src/auth_config.json`
```JSON
{
"domain": "{domain}",
"clientId": "{client}"
}
```
- Poke Theresa for secrets
- `npm start`
- Docker??


### Routes to be done
- Save user profile stuff
  - Already exists, but might have errors
  - Theresa: Just match frontend to that endpoint
- Get new recommendation
  - Payload
    - UserId
    - Animal Preference
      - Cat/Dog
    - Option
      - collaborative filtering
      - content based
      - we need to know whether we're calling for a new collaborative or content based pet for dogs especially and future for cats as well
  - Response
    - New pet
      - pet id
      - image url (prefer just one)
      - pet description
      - pet attributes
        - All of the TRUE features
- Save preference/get new recommndation (all one route!!)
  - Payload
    - Preferences
        - Petid
        - pet type
        - userid
      - Request
        - Cat/dog request
  - Response
    - New pet
      - pet id
      - image url (prefer just one)
      - pet description
      - pet attributes
        - All of the TRUE features



### References/Resources
- [Base React App Reference](https://stackblitz.com/edit/react-fq1gel?file=public%2Findex.html)
