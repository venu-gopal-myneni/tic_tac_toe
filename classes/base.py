class Board:
    player_0=0
    player_1 =1
    def __init__(self) -> None:
        self.state =[[None,None,None],[None,None,None],[None,None,None]]
        self.marks =0
    def mark(self,player_id,x,y):
        if self.state[x][y] is None:
            self.state[x][y] = player_id
            self.marks +=1
            return True
        else:
            return False
    def has_ended(self):

        for row in range(0,3):
            if (self.state[row][0] ==self.state[row][1]==self.state[row][2]) and (self.state[row][0] is not None):
                return (True,self.state[row][0])
        
        for col in range(0,3):
            if (self.state[0][col] ==self.state[1][col]==self.state[2][col]) and (self.state[0][col] is not None):
                return (True,self.state[0][col])
        
        if self.state[0][0]==self.state[1][1]==self.state[2][2] and self.state[0][0] is not None:
            return (True,self.state[0][0])
        
        if self.state[0][2]==self.state[1][1]==self.state[2][2] and self.state[2][0] is not None:
            return (True,self.state[1][1])
        
        if self.marks ==9:
            return (True,None)
        
        return (False,None)

    def print(self) -> str:
        print("***********")
        for row in self.state:
            print(row)




class Player:
    pass

if __name__ == "__main__":
    board = Board()
    board.print()
    board.mark(0,1,2)
    board.print()
    board.mark(1,1,1)
    board.print()
    print(board.has_ended())