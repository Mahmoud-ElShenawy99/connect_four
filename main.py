from Controller.MainWindowController import MainWindowController
from PyQt5 import QtWidgets
import sys


def minimax_alpha_beta(self, param):  # current_board fe elawl tb3tlaha tuple (el board,-1)
    current_board, depth, alpha, beta, maximizingPlayer,f = param  # current_board fe elawl tb3tlaha tuple (el board,-1)
    if depth == 0:  # or game over in position
        return None, self.eval_heuristic(current_board[0],current_board[1],maximizingPlayer)  # static evaluation of position

    if maximizingPlayer:
        chosen_child, maxEval = None, -math.inf
        if not f:
            neighbours = self.b.get_neighbours(current_board[0], 0)
        else:
            neighbours = [current_board]
        for child in neighbours:  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
            eval = self.minimax_alpha_beta((child, depth - 1, alpha, beta, False,False))
            if eval > maxEval:
                chosen_child, maxEval = child, eval
            alpha = max(alpha, maxEval)  # elsa7 maxeval wala eval hna ?
            if beta <= alpha:
                break
        return chosen_child, maxEval

    else:
        chosen_child, minEval = None, math.inf
        neighbours = self.b.get_neighbours(current_board[0], 1)

        for child in neighbours:  #######de lazm tb2a el neighbours bto3 current_board fa lazm nst5dm get_neighbours 34an t4t8l
            eval = self.minimax_alpha_beta((child, depth - 1, alpha, beta, True,False))
            if eval < minEval:
                chosen_child, minEval = child, eval
            beta = min(beta, minEval)  # elsa7 mineval wala eval hna?
            if beta <= alpha:
                break
        return chosen_child, minEval
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindowController()
    ui.show()
    sys.exit(app.exec_())

