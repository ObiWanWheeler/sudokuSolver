from gui import GUI
import pygame
pygame.init()

class Board:
    def __init__(self):
        self.current_row = 0
        self.current_col = -1
        self.rows = []
        self.count = 0
        # self.solved_cells = 0
        with open("board.txt", "r") as file:
            lines = file.readlines()
        for i in lines:
            self.rows.append(list(map(int, i.split())))

        self.changeable = [[cell == 0 for cell in row] for row in self.rows]
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.gui = GUI()

    def show_board(self):
        print()
        for row in self.rows:
            print(row)
        print()

    def solve_board(self):
        self.find_next_changeable()
        while True:
            # increment cell by 1
            self.rows[self.current_row][self.current_col] += 1
            self.count += 1
            # if cell is 10, move to last cell
            if self.rows[self.current_row][self.current_col] > 9:
                self.rows[self.current_row][self.current_col] = 0
                self.find_last_changeable()
                continue
            # check if board is allowed
            # if allowed, move onto next cell
            # if not allowed, move back to last changeable cell and increment by 1
            if self.check_if_possible():
                if self.complete():
                    print(self.count)
                    self.show_board()
                    break
                self.find_next_changeable()
            self.gui.check_events()
            self.gui.show(self.rows, self.current_col, self.current_row, self.changeable)
            self.clock.tick(self.fps)

    def find_next_changeable(self):
        self.set_next_coord()
        while not self.changeable[self.current_row][self.current_col]:
            self.set_next_coord()

    def find_last_changeable(self):
        self.set_last_coord()
        while not self.changeable[self.current_row][self.current_col]:
            self.set_last_coord()

    def set_next_coord(self):
        self.current_col += 1
        if self.current_col > 8:
            self.current_row += 1
            self.current_col = 0

    def set_last_coord(self):
        self.current_col -= 1
        if self.current_col == -1:
            self.current_col = 8
            self.current_row -= 1

    def check_if_possible(self) -> bool:
        if self.check_row() and self.check_col() and self.check_square():
            return True
        return False

    def check_row(self) -> bool:
        row = self.rows[self.current_row]
        return self.check_list(row)

    def check_col(self) -> bool:
        col = []
        for row in self.rows:
            col.append(row[self.current_col])
        return self.check_list(col)

    def check_square(self) -> bool:
        x = []
        top = (self.current_row//3)*3
        left = (self.current_col//3)*3
        for i in range(top, top + 3):
            for j in range(left, left + 3):
                x.append(self.rows[i][j])
        return self.check_list(x)

    def check_list(self, x: list) -> bool:
        val = self.rows[self.current_row][self.current_col]
        if x.count(val) > 1:
            return False
        return True

    def complete(self):
        for i in self.rows:
            if sum(i) != 45:
                return False

        x = []
        top = (self.current_row // 3) * 3
        left = (self.current_col // 3) * 3
        for i in range(top, top + 3):
            for j in range(left, left + 3):
                x.append(self.rows[i][j])
        if sum(x) != 45:
            return False

        x=[]
        for row in self.rows:
            x.append(row[self.current_col])
        if sum(x) != 45:
            return False
        return True


