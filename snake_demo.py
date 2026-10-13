import pygame
import math
import sys
import random
import neat
import pickle
random.seed(14)
#3,8,10,14,27
pygame.init()
clock = pygame.time.Clock()

config = neat.Config(
    neat.DefaultGenome,
    neat.DefaultReproduction,
    neat.DefaultSpeciesSet,
    neat.DefaultStagnation,
    "config-neat.txt",
)

BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
RED    = (130, 20, 20)    
GREEN  = (34, 155, 58)
DARKGREEN = (76, 108, 46)
HEADGREEN = (20, 64, 14)    
BLUE   = (34, 108, 150)   
YELLOW = (220, 196, 64)   
GRAY   = (120, 120, 128)  
ORANGE = (224, 132, 56)

current_x_first = 150
current_y_first = 150
snake_head_size_x = 50
snake_head_size_y = 50
velocity = "right"
position_x = [150]
position_y = [150]
apples_eaten = 0
spaces_moved = 0
in_body = False
alive = True
engage_ai = True
old_dist = 0
new_dist = 0
dist_points = 0


apple_alive = False
game_start = True
appleX = 650
appleY = 350
filename = "best_snake_16735.pkl" #this
with open(filename, "rb") as f:
    winner = pickle.load(f)

winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
net = winner_net
p = neat.Population(config)
genome_id, genome = next(iter(p.population.items()))


def New_Game():
    global current_x_first, current_y_first, snake_head_size_x, snake_head_size_y, velocity, spaces_moved, old_dist, new_dist
    global position_x, position_y, apples_eaten, apple_alive, game_start, appleX, appleY, in_body, alive, engage_ai
    global sensors, alive, net, dist_points
    current_x_first = 150
    current_y_first = 150
    snake_head_size_x = 50
    snake_head_size_y = 50
    velocity = "right"
    position_x = [150]
    position_y = [150]
    appleX = 650
    appleY = 350
    apples_eaten = 0
    spaces_moved = 0
    in_body = False
    alive = True
    engage_ai = True
    old_dist = 0
    new_dist = 0
    dist_points = 0

def ai_imput():

    output = net.activate(sensors)
    ai_direction = ["right", "down", "left", "up"]
    choice = ai_direction[output.index(max(output))]
    return choice
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(filename)
New_Game()
old_dist = abs(appleX - current_x_first) + abs(appleY - current_y_first)
while alive == True:
        if (current_x_first == appleX and current_y_first == appleY):
                spaces_moved = 0
                in_body = True
                while in_body == True:
                    appleX = random.randrange(50,1200, 50)
                    appleY = random.randrange(50,600, 50)
                    in_body = False
                    for i in range(len(position_x)):
                        if appleX == position_x[i] and appleY == position_y[i]:
                            in_body = True
                apples_eaten = apples_eaten + 1
        if(spaces_moved>200):
             alive = False
                


        for event in pygame.event.get():
            
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()            

        

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if velocity != "left":
                        velocity = "right"


                if event.key == pygame.K_s:
                    if velocity != "up":
                        velocity = "down"


                if event.key == pygame.K_a:
                    if velocity != "right":
                        velocity = "left"


                if event.key == pygame.K_w:
                    if velocity != "down":
                        velocity = "up"



                if event.key == pygame.K_r:
                    alive = False

        sensors = [
            ((appleX - current_x_first) / 50), 
            ((appleY - current_y_first) / 50),
            ((1150 - current_x_first) / 50),
            ((current_x_first - 50) / 50),
            ((600 - current_y_first) / 50),
            ((current_y_first - 50) / 50),
        ]

                
        if engage_ai == True:
            choice = ai_imput()
            if choice == "right" and velocity != "left":
                velocity = "right"
            if choice == "left" and velocity != "right":
                velocity = "left"
            if choice == "down" and velocity != "up":
                velocity = "down"
            if choice == "up" and velocity != "down":
                velocity = "up"
        

        if velocity == "right":
                        current_x_first = current_x_first + 50
                        spaces_moved = spaces_moved + 1
        if velocity == "down":
                        current_y_first = current_y_first + 50
                        spaces_moved = spaces_moved + 1

        if velocity == "left":
                        current_x_first = current_x_first + -50
                        spaces_moved = spaces_moved + 1

        if velocity == "up":
                        current_y_first = current_y_first + -50
                        spaces_moved = spaces_moved + 1


                
        position_x.append(current_x_first)
        position_y.append(current_y_first)


        if (current_x_first >= 1151) or (current_x_first <= 49):
            alive = False

        if (current_y_first >= 601) or (current_y_first <= 49):
            alive = False
        new_dist = abs(appleX - current_x_first) + abs(appleY - current_y_first)

        if new_dist < old_dist:
            dist_points = dist_points + 1
        old_dist = new_dist




        screen.fill(GREEN)
            
        pygame.draw.rect(screen, BLUE, (0, 0, 50, 720))
        pygame.draw.rect(screen, BLUE, (0, 0, 1280, 50))
        pygame.draw.rect(screen, BLUE, (0, 650, 1280, 350))
        pygame.draw.rect(screen, BLUE, (1200, 0, 450, 720))

        pygame.draw.rect(screen, RED, (appleX, appleY, 50, 50))
        pygame.draw.rect(screen, BLACK, (appleX, appleY, 50, 50), 2)
        pygame.draw.rect(screen, HEADGREEN, (position_x[-1], position_y[-1], snake_head_size_x, snake_head_size_y))
        pygame.draw.rect(screen, BLACK, (position_x[-1], position_y[-1], snake_head_size_x, snake_head_size_y), 2)

        for i in range (apples_eaten):
                if len(position_x)>i+1:
                    pygame.draw.rect(screen, DARKGREEN, (position_x[-i-2], position_y[-i-2], snake_head_size_x, snake_head_size_y))
                    pygame.draw.rect(screen, BLACK, (position_x[-i-2], position_y[-i-2], snake_head_size_x, snake_head_size_y), 2)

                    if (position_x[-1] == position_x[-i-2]) and (position_y[-1] == position_y[-i-2]) and (apples_eaten>2):
                        #alive = False
                        pass


        if (current_x_first == appleX and current_y_first == appleY) or len(position_x) == 0:
            pass
        else:
            position_y.pop(0)
            position_x.pop(0)
        






        pygame.display.flip()


        
        clock.tick(10)
