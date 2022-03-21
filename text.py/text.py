
import pygame
pygame.init()

Width_of_pygame = 400
height_of_pygame = 400
Window_in_pygame = pygame.display.set_mode((Width_of_pygame,height_of_pygame))
pygame.display.set_caption("My First Game")

Color_of_square = (0,0,255)
x = 100
y = 100
width = 30
height = 30
run_my_game = True
jump = False
jump_speed = 20
speed = 1
while run_my_game:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run_my_game= False
    pygame.draw.rect(Window_in_pygame, (Color_of_square), (x,y,width,height))
    pygame.display.update()
    
    key_pressed = pygame.key.get_pressed()

    if jump is False:
        if key_pressed[pygame.K_UP] and y > speed:
            y -= speed
        if key_pressed[pygame.K_DOWN] and y < height_of_pygame - height:
            y += speed
    if key_pressed[pygame.K_RIGHT] and x < Width_of_pygame - width: 
        x += speed
    if key_pressed[pygame.K_LEFT] and x > speed:
        x -= speed

    if jump is False and key_pressed[pygame.K_SPACE]:
        jump = True

    if jump is True:
        y -= jump_speed
        jump_speed -= 1
        if jump_speed < -20:
            jump = False
            jump_speed = 20
    
    pygame.time.delay(30)
    Window_in_pygame.fill((0,0,0))
pygame.quit()

