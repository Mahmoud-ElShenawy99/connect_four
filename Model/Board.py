# module_name, package_name, ClassName, method_name, ExceptionName, function_name,
# GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
import random


class Board:
    def __init__(self):
        # 00000000|00000000|00000000|00000000|00000000|00000000|101000000
        self.board = int('00000000000000000000000000000000000000000000000001000001', base=2)
        self.board_string=f"{self.board:#063b}"
        print(f"{self.board:#063b}")
        self.p1_Hmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_Hmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_Vmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_Vmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_D1mask= int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_D1mask =int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_D2mask= int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_D2mask = int('7FFFFFFFFFFFFFFF', base=16)
        self.neighbours = []
    def get_available_positions(self):
        nboard = self.board
        for c in range (7):
            h=self.get_row_indicator(c)
            if h<6:
               self.insert_neighbour(nboard,h,c)
    # def get_neighbours(self,board):
    #    state=self.board

    def insert_neighbour(self,nboard,h,c):
        # if player == 1:
        # print(h)
        play = 1 << (c * 9 + h)
        nboard = play | nboard
        nboard=self.update_nrow_indicator(c,nboard)
        # elif player == 0:
        #     play = (1 << (col * 9 + row_indictor)) ^int('7FFFFFFFFFFFFFFF', base=16)
        #     self.board = play & self.board
        #     self.update_row_indicator(col)
        # self.board_string=f"{self.board:#065b}"
        self.neighbours.append(nboard)
        # print("[Board After Insertion] "+f"{nboard:#065b}")
    def update_nrow_indicator(self, col,nboard):

        if col == 0:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('7FFFFFFFFFFFFE3F', base=16)
        elif col == 1:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('7FFFFFFFFFFC7FFF', base=16)
        elif col == 2:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('7FFFFFFFF8FFFFFF', base=16)
        elif col == 3:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('7FFFFFF1FFFFFFFF', base=16)
        elif col == 4:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('7FFFE3FFFFFFFFFF', base=16)
        elif col == 5:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('7FC7FFFFFFFFFFFF', base=16)
        elif col == 6:
            row_indictor = self.get_nrow_indicator(nboard,col)
            clear = int('0FFFFFFFFFFFFFFF', base=16)
        nboard = nboard & clear
        row_indictor += 1
        nboard = nboard | (row_indictor << (6 + col * 9))
        return nboard
    def get_nrow_indicator(self,nboard, col):
        if col == 0:
            return (nboard & int('1C0', base=16)) >> 6
        elif col == 1:
            return (nboard & int('38000', base=16)) >> 15
        elif col == 2:
            return (nboard & int('7000000', base=16)) >> 24
        elif col == 3:
            return (nboard & int('E00000000', base=16)) >> 33
        elif col == 4:
            return (nboard & int('1C0000000000', base=16)) >> 42
        elif col == 5:
            return (nboard & int('38000000000000', base=16)) >> 51
        elif col == 6:
            return (nboard & int('7000000000000000', base=16)) >> 60

    def insert(self, col, player):
        if col > 6:
            print("[Board] Wrong Column")
            return False
        row_indictor = self.get_row_indicator(col)
        if row_indictor > 5:
            print("[Board] Full Column")
            return False
        if player == 1:
            play = 1 << (col * 9 + row_indictor)
            self.board = play | self.board
            self.update_row_indicator(col)
        elif player == 0:
            play = (1 << (col * 9 + row_indictor)) ^int('7FFFFFFFFFFFFFFF', base=16)
            self.board = play & self.board
            self.update_row_indicator(col)
        self.board_string=f"{self.board:#065b}"
        print("[Board After Insertion] "+f"{self.board:#065b}")
        return True

    def get_row_indicator(self, col):
        if col == 0:
            return (self.board & int('1C0', base=16)) >> 6
        elif col == 1:
            return (self.board & int('38000', base=16)) >> 15
        elif col == 2:
            return (self.board & int('7000000', base=16)) >> 24
        elif col == 3:
            return (self.board & int('E00000000', base=16)) >> 33
        elif col == 4:
            return (self.board & int('1C0000000000', base=16)) >> 42
        elif col == 5:
            return (self.board & int('38000000000000', base=16)) >> 51
        elif col == 6:
            return (self.board & int('7000000000000000', base=16)) >> 60

    def count_win(self,mask):
        ones=0
        zeros=0
        for i in range(63):
            if (mask & 1):
                ones+=1
            else:
                zeros+=1
            mask >>= 1;
        # print("Total zero bit is\n", zeros);
        # print("Total one bit is", ones);
        return zeros;

    def update_row_indicator(self, col):

        if col == 0:
            row_indictor = self.get_row_indicator(col)
            clear = int('7FFFFFFFFFFFFE3F', base=16)
        elif col == 1:
            row_indictor = self.get_row_indicator(col)
            clear = int('7FFFFFFFFFFC7FFF', base=16)
        elif col == 2:
            row_indictor = self.get_row_indicator(col)
            clear = int('7FFFFFFFF8FFFFFF', base=16)
        elif col == 3:
            row_indictor = self.get_row_indicator(col)
            clear = int('7FFFFFF1FFFFFFFF', base=16)
        elif col == 4:
            row_indictor = self.get_row_indicator(col)
            clear = int('7FFFE3FFFFFFFFFF', base=16)
        elif col == 5:
            row_indictor = self.get_row_indicator(col)
            clear = int('7FC7FFFFFFFFFFFF', base=16)
        elif col == 6:
            row_indictor = self.get_row_indicator(col)
            clear = int('0FFFFFFFFFFFFFFF', base=16)
        self.board = self.board & clear
        row_indictor += 1
        self.board = self.board | (row_indictor << (6 + col * 9))

    def invert_board(self):
        c0=  pow(2,self.get_row_indicator(0))-1
        c1 = pow(2,self.get_row_indicator(1))-1
        c2 = pow(2,self.get_row_indicator(2))-1
        c3 = pow(2,self.get_row_indicator(3))-1
        c4 = pow(2,self.get_row_indicator(4))-1
        c5 = pow(2,self.get_row_indicator(5))-1
        c6 = pow(2,self.get_row_indicator(6))-1
        invboard = self.board ^ int('7FFFFFFFFFFFFFFF', base=16)
        invboard=invboard & c0 + 9223372036854775296
        invboard = invboard & ((c1 << 9) + 9223372036854514175)
        invboard = invboard & ((c2 << 18) + 9223372036720820223)
        invboard = invboard & ((c3 << 27) + 9223371968269516799)
        invboard = invboard & ((c4 << 36)+ 9223336921202163711)
        invboard = invboard & ((c5 << 45)+ 9205392822717382655)
        invboard = invboard & ((c6 << 54)+ 18014398509481983)
        return invboard
    def checkwin(self):
        p0_score=0
        p1_score=0
        invboard=self.invert_board()
        print(bin(invboard))
        board=self.board & int('000111111000111111000111111000111111000111111000111111000111111',base=2)
        temp = (board & (board >> 1) & (board >> 2) & (board >> 3)) & self.p1_Vmask

        if (temp != 0):#vertical
            self.p1_Vmask &= temp ^int('7FFFFFFFFFFFFFFF', base=16)
            print("vwinner",bin(self.p1_Vmask))
        temp=(board & (board >> 10) & (board >> 20) & (board >> 30)) & self.p1_Hmask
        if (temp != 0): #horizontal
            self.p1_Hmask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("hwinner")
        temp=(board & (board >> 8) & (board >> 16) & (board >> 24)) & self.p1_D1mask
        print("test", f"{board:#065b}")
        print("test",f"{board >> 8:#065b}")
        print("test", f"{board >> 16:#065b}")
        print("test", f"{board >> 24:#065b}")
        if (temp != 0): #diagonal/
            self.p1_D1mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("d1winner")
        temp=(board & (board >> 11) & (board >> 22) & (board >> 33)) & self.p1_D2mask
        if (temp != 0):#diagonal\
            self.p1_D2mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("d2winner")
        p1_score=self.count_win(self.p1_Vmask) + self.count_win(self.p1_Hmask) + self.count_win(self.p1_D2mask) + self.count_win(self.p1_D1mask)
        ######################################################################33
        temp=(invboard & (invboard >> 1) & (invboard >> 2) & (invboard >> 3)) & self.p0_Vmask
        if (temp != 0):#vertical
            self.p0_Vmask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("vp0winner")
        temp=(invboard & (invboard >> 10) & (invboard >> 20) & (invboard >> 30)) & self.p0_Hmask
        if (temp != 0): #horizontal
            self.p0_Hmask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("hp0winner")
        temp=(invboard & (invboard >> 8) & (invboard >> 16) & (invboard >> 24)) & self.p0_D1mask
        if (temp != 0): #diagonal/
            self.p0_D1mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("d1p0winner")
        temp=invboard & (invboard >> 6 ) & (invboard >> 12) & (invboard >> 18) & self.p0_D2mask
        print("test", f"{invboard:#065b}")
        print("test", f"{invboard >> 6:#065b}")
        print("test", f"{invboard >> 12:#065b}")
        print("test", f"{invboard >> 18:#065b}")
        if (temp != 0):#diagonal\
            self.p0_D2mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            print("d2p0winner")
        p0_score=self.count_win(self.p0_Vmask) + self.count_win(self.p0_Hmask) + self.count_win(self.p0_D2mask) + self.count_win(self.p0_D1mask)
        return p0_score,p1_score
if __name__ == '__main__':
    b = Board()
    i=1
    b.get_available_positions()
    b.neighbours[0]
    # while 1:
    #     p0_score, p1_score = b.checkwin()
    #     print("Player0 score:\n", p0_score)
    #     print("Player1 score:\n", p1_score)
    #     if i % 2:
    #        var=input("go on P1 : ")
    #        b.insert(int(var), 1)
    #     else:
    #        var=input("go on P0 : ")
    #        b.insert(int(var), 0)
    #     i+=1
