# coding: utf-8
with open("input.txt", encoding="utf-8") as f:
    data = f.readlines()
    
rounds = list(map(lambda r: r.strip().split(' '), data))

def choice_score(symbol):
    if symbol == 'X': # Rock
        return 1
    elif symbol == 'Y': # Paper
        return 2
    elif symbol == 'Z': # Scissors
        return 3
        
def outcome_score(opponent, yours):
    if opponent == 'A': #Rock
        if yours == 'X': #Rock
            return 3 # tie
        elif yours == 'Y': #paper
            return 6 # win
        elif yours == 'Z': #scissors
            return 0 # lose
    if opponent == 'B': #paper
        if yours == 'X': #rock
            return 0 #lose
        elif yours == 'Y': #paper
            return 3 #tie
        elif yours == 'Z': #scissors
            return 6 #win
    if opponent == 'C': #scissors
        if yours == 'X': #rock
            return 6 #win
        elif yours == 'Y': #paper
            return 0 #lose
        elif yours == 'Z':
            return 3 #tie
            
scores = [outcome_score(opponent, yours) + choice_score(yours) for opponent, yours in rounds]
total_score = sum(scores)
print(total_score)

def outcome_score_2(yours):
    if yours == 'X':
        return 0 #lose
    if yours == 'Y':
        return 3 #draw
    if yours == 'Z':
        return 6
        
def choice_score_2(opponent, yours):
    if opponent == 'A': #rock
        if yours == 'X': #lose=scissors
            return 3
        if yours == 'Y':
            return 1
        if yours == 'Z':
            return 2
    if opponent == 'B': #paper
        if yours == 'X': #l=r
            return 1
        if yours == 'Y': #d=p
            return 2
        if yours == 'Z': #w=s
            return 3
    if opponent == 'C': #scissors
        if yours == 'X': #l=p
            return 2
        if yours == 'Y':
            return 3
        if yours == 'Z':
            return 1
            
scores_2 = [outcome_score_2(yours) + choice_score_2(opponent, yours) for opponent, yours in rounds]
total_score_2 = sum(scores_2)
print(total_score_2)
