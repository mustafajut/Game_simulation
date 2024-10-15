def calculate_conditional_probability(results, condition):
    total_games = sum(results)
    condition_games = sum(r for r, c in zip(results, [condition] * len(results)) if c == condition)
    wins_given_condition = sum(r for r, c in zip(results, [condition] * len(results)) if c == condition and r > 0)
    
    if condition_games == 0:
        return 0
    
    return wins_given_condition / condition_games

def calculate_pdf(x, distribution):
    return distribution.pdf(x)

def calculate_cdf(x, distribution):
    return distribution.cdf(x)