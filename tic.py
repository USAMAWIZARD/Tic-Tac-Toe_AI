

def convert_array_tic(tic_string):
    tic_array = []
    for i in range(9):
        if tic_string[i] == " ":
            tic_array.append(None)
            continue
        tic_array.append(tic_string[i])
    return tic_array
player_bord = [None, "x", None, None, None, "x", "o", "o","x"]
#player_bord = [None]*9
player_bord=convert_array_tic("o xx  xoo")#"o xx  xoo
print(player_bord)

players = ["x", "o"]
AI = "x"
user = "o"

def get_winner(bord):
    #print("s", bord)
    sumall = 0
    for player in players:
        if bord[0:3].count(player) == 3 or bord[3:6].count(player) == 3 or bord[6:9].count(player) == 3 \
                or bord[0:10:4].count(player) == 3 or bord[2:8:2].count(player) == 3:  # get winner of the game
            print("winner", player, bord)
            return player
    if not (None in bord):
        print("draw")
        return "draw"  # draw


def MinMax(bord, player):
    current_bord = bord.copy()
    scorelist=[]

    winner = get_winner(current_bord)

    if winner == AI:
        #print( scorelist)
        return 1
    elif winner == user:
        #print(scorelist)
        return -1
    elif winner == "draw":
        return 0
        
    if player == "x":
        for i in range(9):
            if current_bord[i] == None:
                current_bord[i] = player
                newscore = MinMax(current_bord.copy(), "o")
                if newscore!=None:
                    scorelist.append(newscore)
                current_bord = bord.copy()       

        print("back track",current_bord, scorelist,newscore)
        if player == "x":
            max_list=max(scorelist)
            return max_list
        else:
            min_list=min(scorelist)
            return min_list

    else:
        for i in range(9):
            if current_bord[i] == None:
                current_bord[i] = player
                newscore = MinMax(current_bord.copy(), "x")
                if newscore!=None:
                    scorelist.append(newscore)
                current_bord = bord.copy()     

        print("back track",current_bord, scorelist,newscore)
        if player == "x":
            max_list= max(scorelist)
            return max_list
        else:
            print("failed",current_bord, scorelist,newscore)
            min_list = min(scorelist)
            return min_list
      




print(MinMax(player_bord.copy(), "x"))
# print(get_winner())
