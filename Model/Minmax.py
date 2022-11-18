import math
import Board


class controller:
    def __init__(self):
        self.b = Board.Board()

    def eval_heuristic(self, current_board):
        x= self.b.get_4_score(current_board)
        return x[0]-x[1]

    def minimax(self, current_board : tuple , depth, maximizingPlayer):  # current_board fe elawl tb3tlaha tuple (el board,-1)
        if depth == 0:  # or game over in position
            return None, self.eval_heuristic(current_board[0])

        if maximizingPlayer:  # 0
            chosen_child, maxEval = None, -math.inf
            neighbours = self.b.get_neighbours(current_board[0], 0)
            print(neighbours[0])
            for child in neighbours:  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                print(bin(current_board[0]))
                print(type(child[0]),type(child[1]))
                returned_child, eval = self.minimax(child, depth - 1, False)
                if eval > maxEval:
                    chosen_child, maxEval = child, eval
            return chosen_child, maxEval

        else:  # minimizer 1
            chosen_child, minEval = None, math.inf
            neighbours=self.b.get_neighbours(current_board[0], 1)
            for child in neighbours:  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
                returned_child, eval, = self.minimax(child, depth - 1, True)
                if eval < minEval:
                    chosen_child, minEval = child, eval
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
    c= controller()
   # b = Board()
    i=0
    y:tuple =(c.b.board,-1)
    print(type(y[0]))
    x=c.minimax(y,4,False)
    print(x[0][1])
    print(bin(x[0][0]))
   # print(c.b.get_neighbours(int("000000000000000000000000000000000000000000000000000000010000001",base=2),1))
   # print(c.b.get_4_score(int("110011111110110101110010010110010101110001000110100000110011000", base=2)))