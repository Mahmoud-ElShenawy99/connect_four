import random
import time
from Model.Board import Board
from PyQt5 import QtWidgets
from View.MainWindow import Ui_GUI
from Model.Minmax import Minmax

class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.board = Board()
        self.minmax=Minmax()
        self.ui = Ui_GUI()
        self.ui.setupUi(self)
        self.ui.B1.clicked.connect(
            lambda x : self.play(-1,self.player_turn))

        self.player1_style = '''background-color: rgb(0, 255, 0);
        color: rgb(37, 109, 133);
        border-radius:51px;
        '''
        self.player0_style = '''background-color: rgb(255, 0, 0);
        color: rgb(37, 109, 133);
        border-radius:51px;
        '''
        self.col = [[self.ui.l00, self.ui.l01, self.ui.l02, self.ui.l03, self.ui.l04, self.ui.l05],
                    [self.ui.l10, self.ui.l11, self.ui.l12, self.ui.l13, self.ui.l14, self.ui.l15],
                    [self.ui.l20, self.ui.l21, self.ui.l22, self.ui.l23, self.ui.l24, self.ui.l25],
                    [self.ui.l30, self.ui.l31, self.ui.l32, self.ui.l33, self.ui.l34, self.ui.l35],
                    [self.ui.l40, self.ui.l41, self.ui.l42, self.ui.l43, self.ui.l44, self.ui.l45],
                    [self.ui.l50, self.ui.l51, self.ui.l52, self.ui.l53, self.ui.l54, self.ui.l55],
                    [self.ui.l60, self.ui.l61, self.ui.l62, self.ui.l63, self.ui.l64, self.ui.l65]
                    ]
        self.player_turn=1
        self.ui.l05.mouseDoubleClickEvent= lambda _: self.play(0,self.player_turn)
        self.ui.l15.mouseDoubleClickEvent= lambda _: self.play(1,self.player_turn)
        self.ui.l25.mouseDoubleClickEvent= lambda _: self.play(2,self.player_turn)
        self.ui.l35.mouseDoubleClickEvent= lambda _: self.play(3,self.player_turn)
        self.ui.l45.mouseDoubleClickEvent= lambda _: self.play(4,self.player_turn)
        self.ui.l55.mouseDoubleClickEvent= lambda _: self.play(5,self.player_turn)
        self.ui.l65.mouseDoubleClickEvent= lambda _: self.play(6,self.player_turn)
        self.change_state(self.board.board)
    def change_state(self, state: int):
        c = [self.board.get_row_indicator(state, 0),
             self.board.get_row_indicator(state, 1),
             self.board.get_row_indicator(state, 2),
             self.board.get_row_indicator(state, 3),
             self.board.get_row_indicator(state, 4),
             self.board.get_row_indicator(state, 5),
             self.board.get_row_indicator(state, 6)]
        for j in range(7):
            x = state >> j * 9
            for i in range(c[j]):
                temp = (x >> i) & 1
                if temp == 0:
                    self.col[j][i].setStyleSheet(self.player0_style)
                else:
                    self.col[j][i].setStyleSheet(self.player1_style)
        print(self.board.get_4_score(self.board.board))
        


    def play(self, col,player):
        if (col != -1 and  not self.board.insert(col,player)):
            print("in")
            return
        self.change_state(self.board.board)
        x1=time.time()
        x=self.minmax.minmax_alpha_mutli((self.board.board,-1),8)
        x2=time.time()
        print("time",str(x2-x1))
        self.board.insert(x[0][1],0)
        self.change_state(self.board.board)


    def hello(self):
        print("S")

if __name__ == '__main__':
    while 1:
        var = input("go on P1 : ")
        c.play(int(var))
        time.sleep(1)
        c.AI()
