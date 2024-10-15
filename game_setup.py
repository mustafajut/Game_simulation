import random
from scipy import stats

def setup_game(num_players):
    return [f"Player_{i+1}" for i in range(num_players)]

def simulate_game(players, num_rounds, win_probability):
    results = {player: 0 for player in players}
    
    for _ in range(num_rounds):
        for player in players:
            if random.random() < win_probability:
                results[player] += 1
    
    return list(results.values())

def player_move(strategy):
    strategies = {
        'conservative': lambda: random.random() < 0.3,
        'balanced': lambda: random.random() < 0.5,
        'aggressive': lambda: random.random() < 0.7
    }
    return strategies[strategy]()

def simulate_round(players, strategies):
    return list(map(lambda p, s: player_move(s), players, strategies))

def filter_winners(round_results):
    return list(filter(lambda x: x, round_results))