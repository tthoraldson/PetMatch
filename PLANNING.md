# Design + Discussion for PetML

Source: https://huyenchip.com/machine-learning-systems-design/design-a-machine-learning-system.html#design-a-machine-learning-system-dwGQI5R

## Project Setup

### Goal

- Allow aspiring pet ownners to enter their info
- Allow pet info to be obtained/requested from various shelter listing sources
- Give users maximally appropriate pet recommendations based on their information and our modeling prediction/recommendation
- Maximize pets adopted from kill shelters
- Understand the nuance behind pet searching
- Show users pets they may not know are perfect for them
- provide a means to contact pet's owner/shelter

### User Experience
- A "Tinder-like" user experience
- Pets in a balanced number considering a limit of matches per day (?)
- Rate the quality of matches to supply retraining features/variables for user specific training

### Performance Constraints
- Compute limitations of on device training
- Limited # of total pets
- No need to be perfect predictions in this case
- Ask more behavioral questions

### Evaluation
- Metric showing accepted matches
- Metrics from users rating their opinion of the matches

### Personalization
- Ideally one lite model layer can be used for specific user(s) recommendations but is this technically feasible, given performance constraints?
- Could be imeplemented as uers specific feature store that supplies some inputs to a base recommendation model
- Adaptation to specific users situations is a good metric imho

### Project Constraints
- Limited time to implement
- No budget for spending
- 3 person 5 animal team
- Full stack deliverable

### Data Pipeline
#### Inputs
user profile
environmental profile
pet profile
organization/shelter profile

#### Outputs
pet recommendation (binary classification)

### Bias Considerations
- How do we avoid reinforcement of societal biases, such as who can adopt a pet, which pets are worth adoption
- Some have a bias against rescues, mixed breed pets, and certain breeds
- We can actually highlight genetic disease resistance, life span, temperment metrics to try and "train out" biases when they arise

### Model Selection
supervised or unsupervised?
Generation or prediction - prediction
Regression or classication?

### Baseline
Simple heuristic baseline 60% of adopted pets are within 20mi radius (example only)