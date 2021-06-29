import pygame


class GUI:
    def __init__(self):
        self.window = pygame.display.set_mode((490, 490))
        self.window.fill((20, 20, 20))
        self.length = 50
        self.border = 5

    def show(self, grid, x=None, y=None):
        for row_num in range(len(grid)):
            for col_num in range(len(grid[row_num])):
                pygame.draw.rect(self.window, (200, 200, 200),
                                 [(self.length + self.border) * col_num, (self.length + self.border) * row_num, self.length, self.length])
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
