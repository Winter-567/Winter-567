# import the pygame module, so you can use it
import pygame
from random import random
 
class snake:
    def __init__(self, snake_block):
        pygame.Rect(300,300,snake_block,snake_block)
        
    def move_snake(self, x1_change, y1_change):
        self.move(x1_change, y1_change)


# define a main function
def main():
     
    pygame.init()

    dis_width = 800
    dis_height = 600

    dis=pygame.display.set_mode((dis_width,dis_height))
 
    pygame.display.set_caption("Snake")
 
    game_over = False

    blue=(0,0,255)
    red=(255,0,0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()

    snake_block = 30

    x1 = 300
    y1 = 300
 
    x1_change = 0    
    y1_change = 0

    apple_x1 = (random()*800) 
    apply_y1 = (random()*600) 

 
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                

        x1 = x1 + x1_change
        y1 = y1 + y1_change
        
        snake = pygame.Rect(x1,y1,snake_block,snake_block)
        apple = pygame.Rect(apple_x1,apply_y1,snake_block,snake_block)



        if snake.colliderect(apple) or apple.colliderect(snake):
            apple_x1 = (random()*800) 
            apply_y1 = (random()*600) 
            apple = pygame.Rect(apple_x1,apply_y1,snake_block,snake_block)

        dis.fill(white)
        pygame.draw.rect(dis,blue,snake)
        pygame.draw.rect(dis,red,apple)

        pygame.display.update()
        clock.tick(10) 
    pygame.quit()
    quit()
     

if __name__=="__main__":
    main()





