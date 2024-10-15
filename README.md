# Game_simulation
probability_based_game_simulation


Now that we have created all the necessary modules, you can run the simulation by executing the game_simulation.py script. This project covers the following concepts:

## Probability Distributions: 
We use Bernoulli distribution for individual game outcomes and Binomial distribution for the overall game results. We also implement Poisson distribution for modeling rare events.
## Conditional Probability: 
The calculate_conditional_probability function in probability_calculations.py calculates the probability of winning given a certain move.
## PDF/CDF: 
The calculate_pdf and calculate_cdf functions in probability_calculations.py can be used to calculate probability density function and cumulative distribution function for given distributions.
## Lambda Functions: 
We use lambda functions in the player_move function in game_setup.py to define different strategies.
## Map/Filter: 
The simulate_round function in game_setup.py uses map to apply moves to all players, and filter_winners uses filter to select winning moves.

To run the simulation:

Save each module in a separate .py file with the names mentioned in the artifacts.
Make sure you have the required libraries installed (matplotlib, scipy, numpy).
Run the game_simulation.py script.

![Screenshot 2024-10-15 230554](https://github.com/user-attachments/assets/c3a29169-196b-49aa-9e0a-5309c422b00c)
![Screenshot 2024-10-15 230524](https://github.com/user-attachments/assets/1fd15656-5123-4375-af79-a3c8154cbb48)
