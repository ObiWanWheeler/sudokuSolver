import pygame


class GUI:
    def __init__(self):
        self.window = pygame.display.set_mode((490, 490))
        self.window.fill((20, 20, 20))
        self.length = 50
        self.border = 5
        pygame.display.set_caption("Sudoku Solver Made By Anonymous33")
        self.font = pygame.font.SysFont(None, 25)

    def show(self, grid, x, y, changeable_grid):
        for row_num in range(len(grid)):
            for col_num in range(len(grid[row_num])):
                color = (200, 200, 200)
                if row_num == y and col_num == x:
                    color = (100, 100, 255)
                if not changeable_grid[row_num][col_num]:
                    color = (100, 255, 100)
                pygame.draw.rect(self.window, color,
                                 [(self.length + self.border) * col_num, (self.length + self.border) * row_num, self.length, self.length])
                text = self.font.render(str(grid[row_num][col_num]), True, (0, 0, 0))
                self.window.blit(text, [(self.length + self.border) * col_num + self.length//2, (self.length + self.border) * row_num + self.length//2])
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
