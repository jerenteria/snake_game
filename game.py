import sys, random
import pygame

pygame.init()

# Screen settings
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake Game!")

# Set background color
bg_color = (0, 0, 0)

def run_game():
    # snake_pos = [250, 75]
    snake_pos=[200,70]

    # snake_body = [[200, 75]]
    snake_body=[[200,70] , [200-10 , 70] , [200-(2*10),70]]

    direction = 'right'


    CLOCK = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # Redraw the background color of screen through each pass through of the loop
                screen.fill(self.bg_color)

            keys = pygame.key.get_pressed()


            if (keys[pygame.K_w] or keys[pygame.K_UP]):
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
                direction = 'left'
                

        for square in snake_body:
            # rendering the square(s) of the snake using pygame.draw.rect
            # first argument is the surface where you want to draw the which is the screen that was made above
            # second argument is the color of the rectangle
            # Third argument is the pos or where to place the rect it takes a tuple with an x coordinate as the first argument
            # and y coordinate as the second argument, width as third argument and height as fourth argument
            pygame.draw.rect(screen, (0, 255, 0), (square[0], square[1], 10, 10))

            if direction is right 
            if direction == 'right':
                # add 10 to x coordinate of snake_pos making it move right
                snake_pos[0] += 10
            elif direction == 'left':
                snake_pos[0] -= 10
            elif direction == 'up':
                snake_pos[1] -= 10
            elif direction == 'down':
                snake_pos[1] += 10

            snake_body.append(list(snake_pos))
            snake_body.pop(0)

            pygame.display.update()
            CLOCK.tick(25)

run_game()