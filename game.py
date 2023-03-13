import sys, random
import pygame

pygame.init()

# Screen settings
WIN_X = 1200
WIN_Y = 800
screen = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption("Snake Game!")

# Set background color
bg_color = (0, 0, 0)


def run_game():
    # snake_pos = [250, 75]
    snake_pos=[200,70]

    # snake_body = [[200, 75]]
    snake_body=[[200,70], [200-10, 70], [200-(2*10),70]]

    food_pos = [0, 0]
    food_spawn = True

    direction = 'right'


    CLOCK = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()

            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'
        
        # Redraw the background color of screen through each pass through of the loop
        screen.fill(bg_color)

        for square in snake_body:
            # rendering the square(s) of the snake using pygame.draw.rect
            # first argument is the surface where you want to draw the which is the screen that was made above
            # second argument is the color of the rectangle
            # Third argument is the pos or where to place the rect it takes a tuple with an x coordinate as the first argument
            # and y coordinate as the second argument, width as third argument and height as fourth argument
            pygame.draw.rect(screen, (0, 255, 0), (square[0], square[1], 10, 10))

            # if direction is right 
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
            
        
            # check if x coordinate of snake is smaller than 0, if yes than snake has crossed left side of screen
            if snake_pos[0] <= 0 or snake_pos[0] >= WIN_X:
                sys.exit()

            if snake_pos[1] <= 0 or snake_pos[1] >= WIN_Y:
                sys.exit()

            if snake_pos[0]+10 <=0 or snake_pos[0] >= WIN_X:
                sys.exit()
            if snake_pos[1]+10 <=0 or snake_pos[1] >= WIN_Y:
                sys.exit()


            # draw fruit on screen
            if food_spawn:
                # generate random pos for food, x coordinate is going to be from range 40 to screen_width - 40 not starting from 0
                # b/c fruit can spawn too close to boundaries(same logic for y coordinate)
                food_pos = [random.randrange(40, WIN_X-40), random.randrange(40, WIN_Y-40)]
                food_spawn = False
            pygame.draw.rect(screen, (255, 0, 0), (food_pos[0], food_pos[1],10 ,10))

            if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(food_pos[0],food_pos[1],10,10)):
                food_spawn = True
            else:
                snake_body.pop(0)

        pygame.display.update()
        CLOCK.tick(10)

run_game()