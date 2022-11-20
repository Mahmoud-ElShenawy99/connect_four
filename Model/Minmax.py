import concurrent.futures
import math
from Model.Board import Board
import time

class Minmax:
    def __init__(self):
        self.b = Board()

    def eval_heuristic(self, current_board,col,maximizing_player):
        x= self.b.get_4_score(current_board)
        x1=self.b.get_3_score(current_board)
        temp=x[0]-40*x[1]+x1[0]-30*x1[1]

        # print(col)
        if col > 1 and col < 5:
            # print(col)
            temp=(temp+4)*8
            if maximizing_player:
                temp*=-1

        # print(x)
        # print(x1)
        return temp

    def minmax_mutli(self, current_board, depth):
        neighbours=self.b.get_neighbours(current_board[0],0)
        t = []

        # for n in neighbours:
           # print(bin(n[0]))
        for n in neighbours:
             t.append((n, depth-1 ,True,True))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(self.minimax,t)
        max=-math.inf
        j=0

        for r,i in zip(results,range(len(t))):
            print(r)
            # print(bin(r[0][0]))
            if r[1] > max:
                # print("in")
                max=r[1]
                j=r

        # print(j)
        return j

    def minimax(self,param):
        current_board , depth, maximizingPlayer,f=param # current_board fe elawl tb3tlaha tuple (el board,-1)
        if depth == 0:  # or game over in position
            # x=self.eval_heuristic(current_board[0], current_board[1])
            # print(bin(current_board[0]), current_board[1],x)
            return None, self.eval_heuristic(current_board[0],current_board[1],maximizingPlayer)

        if maximizingPlayer:  # 0
            chosen_child, maxEval = None, -math.inf
            if not f:
                neighbours = self.b.get_neighbours(current_board[0], 0)
            else:
                neighbours = [current_board]
            for child in neighbours:  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                returned_child, eval = self.minimax((child, depth - 1, False,False))
                if eval > maxEval:
                    chosen_child, maxEval = child, eval
                    # print(chosen_child)

            return chosen_child, maxEval

        else:  # minimizer 1
            chosen_child, minEval = None, math.inf

            neighbours=self.b.get_neighbours(current_board[0], 1)

            for child in neighbours:  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                returned_child, eval, = self.minimax((child, depth - 1, True,False))
                if eval < minEval:
                    chosen_child, minEval = child, eval
                    # print(chosen_child)
            return chosen_child, minEval

    def minimax_alpha_beta(self, current_board :tuple, depth, alpha, beta, maximizingPlayer):  # current_board fe elawl tb3tlaha tuple (el board,-1)
        if depth == 0:  # or game over in position
            return None, self.eval_heuristic(current_board[0])  # static evaluation of position

        if maximizingPlayer:
            chosen_child, maxEval = None, -math.inf
            for child in self.b.get_neighbours(current_board[0], 1):  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                eval = self.minimax(child, depth - 1, alpha, beta, False)
                if eval > maxEval:
                    chosen_child, maxEval = child, eval
                alpha = max(alpha, maxEval)  # elsa7 maxeval wala eval hna ?
                if beta <= alpha:
                    break
            return chosen_child, maxEval

        else:
            chosen_child, minEval = None, math.inf
            for child in self.b.get_neighbours(current_board[0], 0):  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                eval = self.minimax(child, depth - 1, alpha, beta, True)
                if eval < minEval:
                    chosen_child, minEval = child, eval
                beta = min(beta, minEval)  # elsa7 mineval wala eval hna?
                if beta <= alpha:
                    break
            return chosen_child, minEval
if __name__ == '__main__':
    c= Minmax()
    b = Board()
    i=0
    y:tuple =(c.b.board,-1)
    # x=b.get_neighbours(b.board,0)
    # test=[]
    # for n in x:
    #     test.append(c.minimax(((n, 3,True,True))))
    # print(test)

    print("multi:",c.minmax_mutli(y,4))
    print("norm",c.minimax((y, 4,True,False)))
    # print(type(y[0]))
    # x1=time.time()
    # c.minmax_mutli(y, 6)
    # x=c.minimax((y,7,False))
    # x2=time.time()
    # print(x2-x1)
    # print(x[0][1])
    # print(bin(x[0][0]))
   # print(c.b.get_neighbours(int("000000000000000000000000000000000000000000000000000000010000001",base=2),1))
   # print(c.b.get_4_score(int("110011111110110101110010010110010101110001000110100000110011000", base=2)))