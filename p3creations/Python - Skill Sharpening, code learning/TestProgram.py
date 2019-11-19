import pygame
import random

#initializing my variables
snake_x = []
snake_y = []
length_allowed = 1
x_player = 0
y_player = 0
velocity = 25
player_width =25
player_height = 25
screen_height = 500
screen_width = 500
pellet_width = 25
pellet_height = 25
score = 0
run = True
direction = 2;
screen_height -= screen_height % 25
screen_width -= screen_width % 25

recount = True
while recount:
   
    x_pellet = random.randint(0, screen_width/velocity) * velocity
   
    y_pellet = random.randint(0, screen_height/ velocity) * velocity
   
    if x_pellet >= screen_width or x_pellet <= 0:
        recount = True;
    elif y_pellet >= screen_height or y_pellet <= 0:
        recount = True;
    else:
        break;
       

while x_pellet < 0 and x_pellet >= screen_width and y_pellet < 0 and y_pellet >= screen_height:

    x_pellet = random.randint(0, screen_width/velocity) * velocity

    y_pellet = random.randint(0, screen_height/ velocity) * velocity    

#windowing stuff

pygame.init();

win = pygame.display.set_mode((screen_width,screen_height));

pygame.display.set_caption("Snake");


while run:
    pygame.time.delay(120)
   
    #checks for a quit button
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
   
            run = False;
        #gets a list of keys pressed and sees if it's any they want
   
        keys=pygame.key.get_pressed()
       
        if  keys[pygame.K_UP]:
           
            direction = 0;
           
        elif keys[pygame.K_LEFT]:
       
            direction = 1;
           
        elif keys[pygame.K_DOWN]:
           
            direction = 2;
           
        elif keys[pygame.K_RIGHT]:
           
            direction = 3;
           
   #checks for points
   
    if x_player == x_pellet and y_player == y_pellet:
       
        score += 1
        length_allowed += 2
        recount = True
        while recount:
           
            x_pellet = random.randint(0, screen_width/velocity) * velocity
           
            y_pellet = random.randint(0, screen_height/ velocity) * velocity
           
            if x_pellet >= screen_width or x_pellet <= 0:
                recount = True;
            elif y_pellet >= screen_height or y_pellet <= 0:
                recount = True;
            else:
                break;
               
   
   
   #Moves the player
    if direction == 0:
       
        y_player -= velocity
   
    elif direction == 1:
       
        x_player -= velocity;

    elif direction == 2:
       
        y_player += velocity;
   
    else:
   
        x_player += velocity;
   
    if x_player < 0:
   
        x_player = screen_width
   
    elif x_player > screen_width:
   
        x_player = 0
   
    if y_player < 0:
   
        y_player = screen_height
   
    elif y_player >= screen_height:
   
        y_player = 0
   
    for x in range(len(snake_x)-2):
   
            if snake_x[x] == snake_x[len(snake_x)-1] and snake_y[x] == snake_y[len(snake_y)-1]:
   
                run = False;
   
    snake_x.append(x_player)
   
    snake_y.append(y_player)
   
    pygame.draw.rect(win, (0, 0, 0),(0 , 0 , screen_width, screen_height));
   
    #draws the snake
   
    for x in range(len(snake_x)):
       
        pygame.draw.rect(win, (225, 235, 52),(snake_x[x] , snake_y[x] , player_width, player_height));
    pygame.draw.rect(win, (255,0,0),(x_pellet , y_pellet, pellet_width , pellet_height));
    for x in range(len(snake_x)):
        if snake_x[x] == x_pellet and snake_y[x] == y_pellet:

            score += 1

            length_allowed += 2

            recount = True

            while recount:

                x_pellet = random.randint(0, screen_width/velocity) * velocity

                y_pellet = random.randint(0, screen_height/ velocity) * velocity

                if x_pellet >= screen_width or x_pellet <= 0:

                    recount = True;

                elif y_pellet >= screen_height or y_pellet <= 0:

                    recount = True;

                else:

                    break;



   
    if len(snake_x) > length_allowed:
       
        snake_x.remove(snake_x[0])
       
        snake_y.remove(snake_y[0])
       
   
   
    pygame.display.update();    
 
pygame.quit()

