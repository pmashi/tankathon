import random
from collections import Counter

def nba_lottery_simulation():
    teams = {
        'Team1': 140,  
        'Team2': 140,
        'Team3': 140,
        'Team4': 125,
        'Team5': 105,
        'Team6': 90,
        'Team7': 75,
        'Team8': 60,
        'Team9': 45,
        'Team10': 30,
        'Team11': 20,
        'Team12': 15,
        'Team13': 10,
        'Team14': 5   
    }
    
    lottery_balls = []
    for team, odds in teams.items():
        lottery_balls.extend([team] * odds)
    
    random.shuffle(lottery_balls)
    
    top_4_picks = []
    while len(top_4_picks) < 4:
        pick = random.choice(lottery_balls)
        if pick not in top_4_picks:
            top_4_picks.append(pick)
    
    return top_4_picks[0]  

def run_simulations(n):
    first_picks = []
    for _ in range(n):
        first_pick = nba_lottery_simulation()
        first_picks.append(first_pick)
    
    return first_picks

num_simulations = 1000
first_picks = run_simulations(num_simulations)

# Count the frequency of each team getting the first pick
pick_counter = Counter(first_picks)

print("First Pick Frequency after 1000 Simulations:")
with open('nba_lottery_first_picks.txt', 'w') as file:
    for team, count in pick_counter.items():
        result = f"{team}: {count} times"
        print(result)
        file.write(result + '\n')