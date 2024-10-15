# import random
# import matplotlib.pyplot as plt 
# from scipy import stats 
# import numpy as np 

# from game_setup import setup_game, simulate_game
# from probability_calculations import calculate_conditional_probability
# from distributions import generate_poisson_events, plot_distribution

# def main():
#     # Game Setup
#     num_players = 4
#     num_rounds = 100
#     win_probability = 0.6

#     players = setup_game(num_players)
#     results = simulate_game(players, num_rounds, win_probability)

#     # Visualize game results
#     plt.bar(range(len(players)), results)
#     plt.xlabel('Player')
#     plt.ylabel('Wins')
#     plt.title('Game Simulation Results')
#     plt.show()

#     # Conditional Probability Calculation
#     condition_move = 'high_risk'
#     prob_win_given_move = calculate_conditional_probability(results, condition_move)
#     print(f"Probability of winning given {condition_move} move: {prob_win_given_move:.2f}")

#     # Probability Distributions
#     lambda_param = 2
#     num_events = 1000
#     poisson_events = generate_poisson_events(lambda_param, num_events)
#     plot_distribution(poisson_events, 'Poisson Distribution of Events')

# if __name__ == "__main__":
#     main()

import random
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

from game_setup import setup_game, simulate_game
from probability_calculations import calculate_conditional_probability
from distributions import generate_poisson_events, plot_distribution

def play_game():
    # Game Setup
    num_players = int(input("Enter the number of players: "))
    num_rounds = int(input("Enter the number of rounds: "))
    win_probability = float(input("Enter the win probability (0-1): "))

    players = setup_game(num_players)
    results = simulate_game(players, num_rounds, win_probability)

    # Visualize game results
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(players)), results)
    plt.xlabel('Player')
    plt.ylabel('Wins')
    plt.title('Game Simulation Results')
    plt.xticks(range(len(players)), players)
    plt.show()

    # Conditional Probability Calculation
    condition_move = input("Enter the condition move (e.g., 'high_risk'): ")
    prob_win_given_move = calculate_conditional_probability(results, condition_move)
    print(f"Probability of winning given {condition_move} move: {prob_win_given_move:.2f}")

    # Probability Distributions
    lambda_param = float(input("Enter lambda parameter for Poisson distribution: "))
    num_events = int(input("Enter number of events to generate: "))
    poisson_events = generate_poisson_events(lambda_param, num_events)
    plot_distribution(poisson_events, 'Poisson Distribution of Events')

def main():
    while True:
        play_game()
        play_again = input("Do you want to play another game? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()