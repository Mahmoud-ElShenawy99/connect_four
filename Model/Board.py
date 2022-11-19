# module_name, package_name, ClassName, method_name, ExceptionName, function_name,
# GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
import random
import numpy as np


class Board:
    def __init__(self):
        # 00000000|00000000|00000000|00000000|00000000|00000000|101000000
        self.board = int('0000000000000000000000000000000000000000000000000000000000000000', base=2)
        self.board_string=f"{self.board:#065b}"
        print("tttt ", f"{self.board:#065b}\n\n")
        self.p1_Hmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_Hmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_Vmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_Vmask=int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_D1mask= int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_D1mask =int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_D2mask= int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_D2mask = int('7FFFFFFFFFFFFFFF', base=16)
        # self.numberOfThrees=[]

    def reset_masks(self):
        self.p1_Hmask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_Hmask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_Vmask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_Vmask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_D1mask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_D1mask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p1_D2mask = int('7FFFFFFFFFFFFFFF', base=16)
        self.p0_D2mask = int('7FFFFFFFFFFFFFFF', base=16)
    def get_neighbours(self,b,player):
        neighbours=[]
        if player == 1:
            for c in range(0,7,1):
                row_indictor = self.get_row_indicator(b,c)
                if row_indictor > 5:
                    print("[GET_NEIGHBOURS] Full Column")
                    continue
                play = 1 << (c * 9 + row_indictor)
                neighbours.append((bin(self.update_row_indicator(play | b, c)),c))

        else :
            for c in range(0, 7, 1):
                row_indictor = self.get_row_indicator(b, c)
                if row_indictor > 5:
                    print("[GET_NEIGHBOURS] Full Column")
                    continue
                play = (1 << (c * 9 + row_indictor)) ^int('7FFFFFFFFFFFFFFF', base=16)
                neighbours.append((bin(self.update_row_indicator(play & b, c)),c))

        return neighbours

    def insert(self, col, player):
        if col > 6:
            print("[Board] Wrong Column")
            return False
        row_indictor = self.get_row_indicator(self.board,col)
        if row_indictor > 5:
            print("[Board] Full Column")
            return False
        if player == 1:
            play = 1 << (col * 9 + row_indictor)
            self.board = play | self.board
            self.board=self.update_row_indicator(self.board,col)
        elif player == 0:
            play = (1 << (col * 9 + row_indictor)) ^int('7FFFFFFFFFFFFFFF', base=16)
            self.board = play & self.board
            self.board=self.update_row_indicator(self.board,col)
        self.board_string=f"{self.board:#065b}"
        print("[Board After Insertion] "+f"{self.board:#065b}")
        self.get_3_score(self.board)
        return True

    def get_row_indicator(self,b, col):
        if col == 0:
            return (b & int('1C0', base=16)) >> 6
        elif col == 1:
            return (b & int('38000', base=16)) >> 15
        elif col == 2:
            return (b & int('7000000', base=16)) >> 24
        elif col == 3:
            return (b & int('E00000000', base=16)) >> 33
        elif col == 4:
            return (b & int('1C0000000000', base=16)) >> 42
        elif col == 5:
            return (b & int('38000000000000', base=16)) >> 51
        elif col == 6:
            return (b & int('7000000000000000', base=16)) >> 60

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

    def update_row_indicator(self,b, col):

        if col == 0:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('7FFFFFFFFFFFFE3F', base=16)
        elif col == 1:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('7FFFFFFFFFFC7FFF', base=16)
        elif col == 2:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('7FFFFFFFF8FFFFFF', base=16)
        elif col == 3:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('7FFFFFF1FFFFFFFF', base=16)
        elif col == 4:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('7FFFE3FFFFFFFFFF', base=16)
        elif col == 5:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('7FC7FFFFFFFFFFFF', base=16)
        elif col == 6:
            row_indictor = self.get_row_indicator(b,col)
            clear = int('0FFFFFFFFFFFFFFF', base=16)
        b = b & clear
        row_indictor += 1
        b= b | (row_indictor << (6 + col * 9))
        return b

    def invert_board(self,b):
        c0=  pow(2,self.get_row_indicator(b,0))-1
        c1 = pow(2,self.get_row_indicator(b,1))-1
        c2 = pow(2,self.get_row_indicator(b,2))-1
        c3 = pow(2,self.get_row_indicator(b,3))-1
        c4 = pow(2,self.get_row_indicator(b,4))-1
        c5 = pow(2,self.get_row_indicator(b,5))-1
        c6 = pow(2,self.get_row_indicator(b,6))-1
        invboard = b ^ int('7FFFFFFFFFFFFFFF', base=16)
        invboard=invboard & c0 + 9223372036854775296
        invboard = invboard & ((c1 << 9) + 9223372036854514175)
        invboard = invboard & ((c2 << 18) + 9223372036720820223)
        invboard = invboard & ((c3 << 27) + 9223371968269516799)
        invboard = invboard & ((c4 << 36)+ 9223336921202163711)
        invboard = invboard & ((c5 << 45)+ 9205392822717382655)
        invboard = invboard & ((c6 << 54)+ 18014398509481983)
        return invboard

    def get_4_score(self, board):
        invboard=self.invert_board(board)

        board &= int('000111111000111111000111111000111111000111111000111111000111111',base=2)

        temp = (board & (board >> 1) & (board >> 2) & (board >> 3)) & self.p1_Vmask
        if (temp != 0):#vertical
            self.p1_Vmask &= temp ^int('7FFFFFFFFFFFFFFF', base=16)
            # print("vwinner",bin(self.p1_Vmask))

        temp=(board & (board >> 9) & (board >> 18) & (board >> 27)) & self.p1_Hmask
        if (temp != 0): #horizontal
            self.p1_Hmask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("hwinner")


        temp=(board & (board >> 8) & (board >> 16) & (board >> 24)) & self.p1_D1mask
        if (temp != 0): #diagonal/
            self.p1_D1mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("d1winner")

        temp=(board & (board >> 10) & (board >> 20) & (board >> 30)) & self.p1_D2mask
        if (temp != 0):#diagonal\
            self.p1_D2mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("d2winner")

        p1_score=self.count_win(self.p1_Vmask) + self.count_win(self.p1_Hmask) + self.count_win(self.p1_D2mask) + self.count_win(self.p1_D1mask)
        ##########################################################################################################################################

        temp=(invboard & (invboard >> 1) & (invboard >> 2) & (invboard >> 3)) & self.p0_Vmask
        if (temp != 0):# vertical
            self.p0_Vmask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("vp0winner")
        temp=(invboard & (invboard >> 9) & (invboard >> 18) & (invboard >> 27)) & self.p0_Hmask
        if (temp != 0): # horizontal
            self.p0_Hmask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("hp0winner")
        temp=(invboard & (invboard >> 8) & (invboard >> 16) & (invboard >> 24)) & self.p0_D1mask
        if (temp != 0): # diagonal /
            self.p0_D1mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("d1p0winner")
        temp=invboard & (invboard >> 10 ) & (invboard >> 20) & (invboard >> 30) & self.p0_D2mask
        if (temp != 0):# diagonal\
            self.p0_D2mask &= temp ^ int('7FFFFFFFFFFFFFFF', base=16)
            # print("d2p0winner")
        p0_score=self.count_win(self.p0_Vmask) + self.count_win(self.p0_Hmask) + self.count_win(self.p0_D2mask) + self.count_win(self.p0_D1mask)
        return p0_score,p1_score

    def convert_numpy(self):
        arr = -1 * np.ones((6, 7), dtype=int)
        board = self.board_string
        invboard = f"{self.invert_board(b.board):#065b}"
        for i in range(7):
            k = 0
            c = board[5 + (i * 9):11 + (i * 9)]
            c2 = invboard[5 + (i * 9):11 + (i * 9)]
            print("coloumn", i, c)
            for j in c:
                if (j == "1"):
                    print(j)
                    arr[k][i] = j
                k = k + 1
            k = 0
            for j2 in c2:
                if (j2 == "1"):
                    print(j)
                    arr[k][i] = 0
                k = k + 1
        return arr

    def get_3_score(self, board):
        invboard = self.invert_board(board)
        board &= int('000111111000111111000111111000111111000111111000111111000111111', base=2)

        temp = (board & (board >> 1) & (board >> 2)) & self.p1_Vmask
        x = temp & (invboard >> 3)
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # vertical
            if (x4 != (pow(2,63)-1)):
                self.p1_Vmask &= x4
                print("vwinner", bin(self.p1_Vmask))

        temp = (board & (board >> 9) & (board >> 18)) & self.p1_Hmask
        temp2 = (board>>9&(board >>18)&(board >>27))& self.p1_Hmask
        x = (temp & ((invboard >>27)+self.calculation(27)))
        x2 = (temp2 & (invboard))
        x3 = x2 | (temp2 ^ int('7FFFFFFFFFFFFFFF', base=16))
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # horizontal
            if (x4 != (pow(2,63)-1)):
                self.p1_Hmask &=x4
                print("hwinner from left ", bin(self.p1_Hmask))
                print("enterd ")
        if (temp2 != 0):
            if (x3!=(pow(2,63)-1)):
                self.p1_Hmask &= x3
                print("hwinner from right", bin(self.p1_Hmask))
                print("enterd 2")

        temp = (board & (board >> 8) & (board >> 16)) & self.p1_D1mask
        temp2 = (board >> 8 & (board >> 16) & (board >> 24)) & self.p1_D1mask
        x = (temp & ((invboard >> 24)))
        x2 = (temp2 & (invboard))
        x3 = x2 | (temp2 ^ int('7FFFFFFFFFFFFFFF', base=16))
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # horizontal
            if (x4 != (pow(2, 63) - 1)):
                self.p1_D1mask &= x4
                print("D1winner from left ", bin(self.p1_D1mask))
                print("enterd ")
        if (temp2 != 0):
            if (x3 != (pow(2, 63) - 1)):
                self.p1_D1mask &= x3
                print("D1 from right", bin(self.p1_D1mask))
                print("enterd 2")

        temp = (board & (board >> 10) & (board >> 20)) & self.p1_D2mask
        temp2 = (board >> 10 & (board >> 20) & (board >> 30)) & self.p1_D2mask
        x = (temp & ((invboard >> 30)))
        x2 = (temp2 & (invboard))
        x3 = x2 | (temp2 ^ int('7FFFFFFFFFFFFFFF', base=16))
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # horizontal
            if (x4 != (pow(2, 63) - 1)):
                self.p1_D2mask &= x4
                print("D2winner from left ", bin(self.p1_D2mask))
                print("enterd ")
        if (temp2 != 0):
            if (x3 != (pow(2, 63) - 1)):
                self.p1_D2mask &= x3
                print("D2 from right", bin(self.p1_D2mask))
                print("enterd 2")

        temp = (invboard & (invboard >> 1) & (invboard >> 2)) & self.p0_Vmask
        x = temp & (board >> 3)
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # vertical
            if (x4 != (pow(2, 63) - 1)):
                self.p0_Vmask &= x4
                print("vwinner", bin(self.p0_Vmask))

        temp = (invboard & (invboard >> 9) & (invboard >> 18)) & self.p0_Hmask
        temp2 = (invboard >> 9 & (invboard >> 18) & (invboard >> 27)) & self.p0_Hmask
        x = (temp & ((board >> 27)+self.calculation(27)))
        x2 = (temp2 & (board))
        x3 = x2 | (temp2 ^ int('7FFFFFFFFFFFFFFF', base=16))
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # horizontal
            if (x4 != (pow(2, 63) - 1)):
                self.p0_Hmask &= x4
                print("hwinner from left ", bin(self.p0_Hmask))
                print("enterd ")
        if (temp2 != 0):
            if (x3 != (pow(2, 63) - 1)):
                self.p0_Hmask &= x3
                print("hwinner from right", bin(self.p0_Hmask))
                print("enterd 2")

        temp = (invboard & (invboard >> 8) & (invboard >> 16)) & self.p0_D1mask
        temp2 = (invboard >> 8 & (invboard >> 16) & (invboard >> 24)) & self.p0_D1mask
        x = (temp & ((board >> 24)))
        x2 = (temp2 & (board))
        x3 = x2 | (temp2 ^ int('7FFFFFFFFFFFFFFF', base=16))
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # horizontal
            if (x4 != (pow(2, 63) - 1)):
                self.p0_D1mask &= x4
                print("D1winner from left ", bin(self.p0_D1mask))
                print("enterd ")
        if (temp2 != 0):
            if (x3 != (pow(2, 63) - 1)):
                self.p0_D1mask &= x3
                print("D1 from right", bin(self.p0_D1mask))
                print("enterd 2")
        temp = (invboard & (invboard >> 10) & (invboard >> 20)) & self.p0_D2mask
        temp2 = (invboard >> 10 & (invboard >> 20) & (invboard >> 30)) & self.p0_D2mask
        x = (temp & ((board >> 30)))
        x2 = (temp2 & (board))
        x3 = x2 | (temp2 ^ int('7FFFFFFFFFFFFFFF', base=16))
        x4 = x | (temp ^ int('7FFFFFFFFFFFFFFF', base=16))
        if (temp != 0):  # horizontal
            if (x4 != (pow(2, 63) - 1)):
                self.p0_D2mask &= x4
                print("D2winner from left ", bin(self.p0_D2mask))
                print("enterd ")
        if (temp2 != 0):
            if (x3 != (pow(2, 63) - 1)):
                self.p0_D2mask &= x3
                print("D2 from right", bin(self.p0_D2mask))
                print("enterd 2")

        p0_score = self.count_win(self.p0_Vmask) + self.count_win(self.p0_Hmask) + self.count_win(
            self.p0_D2mask) + self.count_win(self.p0_D1mask)
        print("player0 Vscore:", self.count_win(self.p0_Vmask))
        print("player0 Hscore:", self.count_win(self.p0_Hmask))
        print("player0 d1score:", self.count_win(self.p0_D1mask))
        print("player0 d2score:", self.count_win(self.p0_D2mask))

        p1_score = self.count_win(self.p1_Vmask) + self.count_win(self.p1_Hmask) + self.count_win(
            self.p1_D2mask) + self.count_win(self.p1_D1mask)

        print("player1 Vscore:", self.count_win(self.p1_Vmask))
        print("player1 Hscore:", self.count_win(self.p1_Hmask))
        print("player1 d1score:", self.count_win(self.p1_D1mask))
        print("player1 d2score:", self.count_win(self.p1_D2mask))
        self.reset_masks()
        return p1_score,p0_score
    def calculation(self, shift):
        sum = 0
        for i in range(shift):
            sum += pow(2, 62 - i)
        return sum


if __name__ == '__main__':
    b = Board()
    i=0
    # print(b.convert_numpy())
    # print(b.connected_three(b.invert_board(b.board),b.board))
    b.get_3_score(b.board)
    # print(b.get_neighbours(int("000000000000000000000000000000000000000000000000000000010000001",base=2),1))
    # while 1:
    #     p0_score, p1_score = b.checkwin()
    #     print("Player0 score:\n", p0_score)
    #     print("Player1 score:\n", p1_score)
    #     if i % 2:
    #        var=input("go on P0 : ")
    #        b.insert(int(var), 1)
    #        print(b.get_neighbours(b.board, 0))
    #     else:
    #        var=input("go on P1 : ")
    #        b.insert(int(var), 0)
    #        print(b.get_neighbours(b.board,1))
    #     i+=1

    # 010000000001000000000000000001000000001000001001000001001000001
