# module_name, package_name, ClassName, method_name, ExceptionName, function_name,
# GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
import random


class Board:
    def __init__(self):
        # 00000000|00000000|00000000|00000000|00000000|00000000|101000000
        self.board = int('000000000000000000000000000000000000000000000000000000000000000', base=2)
        self.board_string=f"{self.board:#063b}"
        print(f"{self.board:#063b}")
    # 000000000 000000000 000000000 000000000 000000000 000000000 010000000
    # 111111111 111111111 111111111 111111111 111111111 111111111 000111111
    # 000000000 000000000 000000000 000000000 000000000 000000000 101000000
    # 000000000 000000000 000000000 000000000 000000000 000000000 111000000

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




if __name__ == '__main__':
    b = Board()
    i=0
    while 1:

        if i % 2:
           var=input("go on P1 : ")
           b.insert(int(var), 1)
        else:
           var=input("go on P0 : ")
           b.insert(int(var), 5)
        i+=1

