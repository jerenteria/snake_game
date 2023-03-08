import sys
import pygame

class SnakeGame:
    def __init__(self):
        pygame.init()

        # Screen settings
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Snake Game!")

        # Set background color
        self.bg_color = (0, 0, 0)

        self.snake

    def snake(self):
        pygame.draw.rect(screen, (255,255,255)
        pygame.display.update()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the background color of screen through each pass through of the loop
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.snake()

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()