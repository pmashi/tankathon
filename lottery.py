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
    
    return top_4_picks 

def run_simulations(n):
    first_picks = []
    second_picks = []
    third_picks = []
    fourth_picks = []
    for _ in range(n):
        picks = nba_lottery_simulation()
        first_picks.append(picks[0])
        second_picks.append(picks[1])
        third_picks.append(picks[2])
        fourth_picks.append(picks[3])
    
    return first_picks, second_picks, third_picks, fourth_picks

num_simulations = 35
first_picks, second_picks, third_picks, fourth_picks = run_simulations(num_simulations)

# Count the frequency of each team getting the a specific pick
pick_counter1 = Counter(first_picks)
pick_counter2 = Counter(second_picks)
pick_counter3 = Counter(third_picks)
pick_counter4 = Counter(fourth_picks)

ordered_teams = [f'Team{i}' for i in range(1, 15)]

print("First Pick Frequency after 1000 Simulations:")
with open('nba_lottery_first_picks.txt', 'w') as file:
    for team in ordered_teams:
        count = pick_counter1[team]
        result = f"{team}: {count} times"
        print(result)
        file.write(result + '\n')

with open('nba_lottery_second_picks.txt', 'w') as file:
    for team in ordered_teams:
        count = pick_counter2[team]
        result = f"{team}: {count} times"
        print(result)
        file.write(result + '\n')

with open('nba_lottery_third_picks.txt', 'w') as file:
    for team in ordered_teams:
        count = pick_counter3[team]
        result = f"{team}: {count} times"
        print(result)
        file.write(result + '\n')

with open('nba_lottery_fourth_picks.txt', 'w') as file:
    for team in ordered_teams:
        count = pick_counter4[team]
        result = f"{team}: {count} times"
        print(result)
        file.write(result + '\n')