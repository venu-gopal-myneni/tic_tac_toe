from classes.base import Board
def single_play(board,player_id):
    player_input = input(f"Enter Player {player_id} Mark : ")
    x,y = player_input.split(",")
    x,y= int(x),int(y)
    print(f"Player {player_id} Input : {x},{y}")
    while not board.mark(player_id,x,y):
        player_input = input(f"Enter Player {player_id} Valid Mark : ")
        x,y = player_input.split(",")
        x,y= int(x),int(y)
        print(f"Player {player_id} Input : {x},{y}")
    return board

def run_game():
    player_0 = input("Enter Player 0 Name : ")
    player_1 = input("Enter Player 1 Name : ")
    adict = {0:player_0,1:player_1}
    board = Board()
    board.print()
    ended,winner =board.has_ended()
    while not ended:

        board = single_play(board,0)
        board.print()
        ended,winner =board.has_ended()
        print(ended,winner)
        if ended:
            break
        board = single_play(board,1)
        board.print()
        ended,winner =board.has_ended()
    print(f"Winner is : {adict[winner]}")
        
if __name__ =="__main__":
    run_game()
