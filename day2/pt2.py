score_map = {"Rock": ['A', 'X', 1], "Paper": ['B', 'Y', 2], "Scissors": ['C', 'Z', 3]}

def find_score(opp, player):
    if opp=="Rock" and player=="Paper":
        return 8
    if opp=="Rock" and player=="Rock":
        return 4
    if opp=="Rock" and player=="Scissors":
        return 3
    if opp=="Paper" and player=="Rock":
        return 1
    if opp=="Paper" and player=="Paper":
        return 5
    if opp=="Paper" and player=="Scissors":
        return 9
    if opp=="Scissors" and player=="Rock":
        return 7
    if opp=="Scissors" and player=="Paper":
        return 2
    if opp=="Scissors" and player=="Scissors":
        return 6


def find_player_throw(opp, outcome):
    if opp=="Rock" and outcome=="X":
        return "Scissors"
    if opp=="Rock" and outcome=="Y":
        return "Rock"
    if opp=="Rock" and outcome=="Z":
        return "Paper"
    if opp=="Paper" and outcome=="X":
        return "Rock"
    if opp=="Paper" and outcome=="Y":
        return "Paper"
    if opp=="Paper" and outcome=="Z":
        return "Scissors"
    if opp=="Scissors" and outcome=="X":
        return "Paper"
    if opp=="Scissors" and outcome=="Y":
        return "Scissors"
    if opp=="Scissors" and outcome=="Z":
        return "Rock"



with open('./day2/input') as file:
    lines = file.readlines()

total_score = 0
for line in lines:
    print(f'{line[0]} \t {line[2]} ')
    opp_char=line[0]
    player_outcome=line[2]
    opp, player = "", ""
    for k,v in score_map.items():
        if opp_char in v:
            opp = k
            player=find_player_throw(opp, player_outcome)
    print(f'OPP: {opp} PLAYER: {player}')
    score = find_score(opp, player)
    total_score+=score




print(total_score)
