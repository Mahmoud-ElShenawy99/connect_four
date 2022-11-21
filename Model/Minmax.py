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
        temp=10*x[0]-10*x[1]+2*x1[0]-2*x1[1]
        # temp=0
        # print(col)
        if col > 1 and col < 5:
            # print(col)
            t = self.b.utils(current_board)
            if maximizing_player:
                temp += (t[col][0] * 2)
            else:
                temp += (t[col][1] * -2)


        return temp

    def minmax_mutli(self, current_board, depth,tree,parent):
        neighbours=self.b.get_neighbours(current_board[0],0)
        t = []

        # for n in neighbours:
           # print(bin(n[0]))
        for n,i in zip(neighbours,range(len(neighbours))) :
             child_ID = 7 * parent + 1 + i
             tree.create_node(f"{n[0]:#065b}", child_ID, parent=parent)
             t.append((n, depth-1 ,True,True,tree,child_ID))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(self.minimax,t)
        max=-math.inf
        j=0

        for r,i in zip(results,range(len(t))):

            # print(r)
            # print(bin(r[0][0]))
            if r[1] >= max:
                if r[0][1] not in [2,3,4] and r[1] == max:
                    # print("in",r[0][1])
                    continue
                max=r[1]
                j=r

        # print(j)
        return j
    def minmax_alpha_mutli(self, current_board, depth):
        neighbours=self.b.get_neighbours(current_board[0],0)
        t = []

        # for n in neighbours:
           # print(bin(n[0]))
        for n in neighbours:
             t.append((n, depth-1 ,-math.inf, math.inf,True,True))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(self.minimax_alpha_beta,t)
        max=-math.inf
        j=0
        for r,i in zip(results,range(len(t))):
            # print(r)
            # print(bin(r[0][0]))
            if r[1] >= max:
                if r[0][1] not in [2,3,4] and r[1] == max:
                    # print("in",r[0][1])
                    continue
                max=r[1]
                j=r

        # print(j)
        return j
    def minimax(self,param):
        current_board , depth, maximizingPlayer,f,tree,parent=param # current_board fe elawl tb3tlaha tuple (el board,-1)
        if depth == 0:  # or game over in position
            return None, self.eval_heuristic(current_board[0],current_board[1],maximizingPlayer)

        if maximizingPlayer:  # 0
            chosen_child, maxEval = None, -math.inf
            if not f:
                neighbours = self.b.get_neighbours(current_board[0], 0)
            else:
                neighbours = [current_board]
            for child,i in zip(neighbours,range(len(neighbours))) :  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                child_ID = 7*parent+1+i
                tree.create_node(f"{child[0]:#065b}",child_ID, parent=parent)
                returned_child, eval = self.minimax((child, depth - 1, False,False,tree,child_ID))
                if eval > maxEval:
                    chosen_child, maxEval = child, eval
                    # print(chosen_child)                      #0
                                                          #1 2 3 4 5 6 7
                                                    #8 9 10 11 12 13 14

            return chosen_child, maxEval

        else:  # minimizer 1
            chosen_child, minEval = None, math.inf

            neighbours=self.b.get_neighbours(current_board[0], 1)

            for child,i in zip(neighbours,range(len(neighbours))):  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                child_ID=7*parent+1+i
                tree.create_node(f"{child[0]:#065b}",child_ID ,parent=parent)
                returned_child, eval = self.minimax((child, depth - 1, True,False,tree,child_ID))
                if eval < minEval:
                    chosen_child, minEval = child, eval
                    # print(chosen_child)
            return chosen_child, minEval

    def minimax_alpha_beta(self, param):  # current_board fe elawl tb3tlaha tuple (el board,-1)
        current_board, depth, alpha, beta, maximizingPlayer, f,tree,parent = param  # current_board fe elawl tb3tlaha tuple (el board,-1)
        if depth == 0:  # or game over in position
            return None, self.eval_heuristic(current_board[0], current_board[1],
                                             maximizingPlayer)  # static evaluation of position

        if maximizingPlayer:
            chosen_child, maxEval = None, -math.inf
            if not f:
                neighbours = self.b.get_neighbours(current_board[0], 0)
            else:
                neighbours = [current_board]
            for child,i in zip(neighbours,range(len(neighbours))):  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                child_ID = 7 * parent + 1 + i
                tree.create_node(f"{child[0]:#065b}", child_ID, parent=parent)
                returned_child, eval = self.minimax_alpha_beta((child, depth - 1, alpha, beta, False, False,tree,child_ID))
                if eval > maxEval:
                    chosen_child, maxEval = child, eval
                alpha = max(alpha, maxEval)  # elsa7 maxeval wala eval hna ?
                if beta <= alpha:
                    break
            return chosen_child, maxEval

        else:
            chosen_child, minEval = None, math.inf
            neighbours = self.b.get_neighbours(current_board[0], 1)

            for child,i in zip(neighbours,range(len(neighbours))):  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                child_ID = 7 * parent + 1 + i
                tree.create_node(f"{child[0]:#065b}", child_ID, parent=parent)
                returned_child, eval = self.minimax_alpha_beta((child, depth - 1, alpha, beta, True, False,tree,child_ID))
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

    x1=time.time()
    print(c.minmax_alpha_mutli((c.b.board,-1), 7))
    x2 = time.time()
    print("alphamulti",x2-x1)


    x1=time.time()
    print(c.minimax_alpha_beta((((c.b.board,-1), 12,-math.inf,math.inf, True, False))))
    x2 = time.time()
    print("alphanorm",x2-x1)

    x1=time.time()
    print(c.minmax_mutli((c.b.board,-1), 7))
    x2 = time.time()
    print("norm mutli",x2-x1)




