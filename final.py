import pygame
from random import *

pygame.init()

pygame.mixer.music.load("unity_fat_rat_cut_3.mp3")


white = (255,255,255)

black = (0,0,0)

red = (255,0,0)

green=(0,255,0)

blue=(0,206,209)

yellow=(255,230,0)

purple=(148,0,212)

pink =(255,20,147)










colours=[red,green,blue,green,purple,pink,blue,red,purple,yellow,green,blue,purple,red,yellow,pink]
mycolours=[red,green,blue,purple,pink,yellow]



gameDisplay = pygame.display.set_mode((800,800))

pygame.display.set_caption('AMAZ0')


background=pygame.image.load("BACKGROUND2.2.jpg")


play=pygame.image.load("PLAY.PNG")
quitting=pygame.image.load("QUIT.png")
score=pygame.image.load("SCORE.png")
game_over=pygame.image.load("GAME-OVER.png")
def game_intro():
       intro=True
       while intro:
              for event in pygame.event.get():
                     if event.type== pygame.QUIT:
                            pygame.quit()
                            quit()
              gameDisplay.blit(background,[0,0])
              play_button()
              quit_button()
              pygame.display.update()
              clock.tick(15)

def play_button():
       mouse = pygame.mouse.get_pos()
       click=pygame.mouse.get_pressed()
       print(click)
       if 522>mouse[0]>278 and 545>mouse[1]>450:
              if click[0]==1:
                     
                     game_loop()
       gameDisplay.blit(play,[278,450])
       
def quit_button():
       mouse =pygame.mouse.get_pos()
       click=pygame.mouse.get_pressed()
       if 495>mouse[0]>278 and 745>mouse[1]>650:
              if click[0]==1:
                     pygame.quit()
                     quit()
       gameDisplay.blit(quitting,[278,650])

def text_objects(text,font):
       textSurface = font.render(text,True,white)
       return textSurface,textSurface.get_rect()


def inside_score(text):
       myfont=pygame.font.Font('freesans.ttf',20)
       TextSurf,TextRect= text_objects(text,myfont)
       TextRect.center=(700,30)
       gameDisplay.blit(TextSurf,TextRect)
       

def grid(lead_x,lead_y):
    grid_x=(lead_x//200+1)
    grid_y=(lead_y//200+1)
    return(grid_x,grid_y)



def game_loop():
       gameExit = False

       points=20

       lead_x = 400
       
       lead_y = 400

       lead_x_change = 0

       lead_y_change = 0

       colour=white
       
       pygame.mixer.music.play(-1)
       while not gameExit:
              

              for event in pygame.event.get():
                     
                                               
              #for checking if quit is pressed.
                     if event.type == pygame.QUIT:
                            gameExit = True
                   
              #for changing directions.
                     if event.type == pygame.KEYDOWN:
                                   
                            if event.key == pygame.K_LEFT:
                                   lead_x_change = -10
                                   lead_y_change =0

                            if event.key == pygame.K_RIGHT:

                                   lead_x_change = 10
                                   lead_y_change = 0
                            if event.key==pygame.K_UP:

                                   lead_y_change = -10
                                   lead_x_change = 0

                            if event.key==pygame.K_DOWN:
                                   lead_y_change =10
                                   lead_x_change = 0



              lead_x += lead_x_change
              lead_y += lead_y_change
           

              #generates the colour blocks.       
              gameDisplay.fill(black)
              for i in colour_coordinates:
                     pygame.draw.rect(gameDisplay,i[0], [i[1][0],i[1][1],20,20])

              amazo(colour,lead_x,lead_y)#generates amazo.
              mygrid=grid(lead_x,lead_y)#gives the grid in which amazo is in.
           
              #checks if amazo is not colliding with the borders or game over.
              if mygrid[0]>4 or mygrid[0]<1 or mygrid[1]>4 or mygrid[1]<1:
                     
                     print("game over")
                     gameDisplay.blit(game_over,[108,400])
                     gameExit=True
              else:
                     a=gcc[mygrid][1][0]
                     b=gcc[mygrid][1][1]
                     c=gcc[mygrid][0]
           
                     every_point,colour=collision(a,b,c,colour,lead_x,lead_y)
                     points=points+every_point
                     print(points)
                     gameExit=points_fun(points)
              text="ENERGY:"+str(points)
              inside_score(text)

              pygame.display.update()
              clock.tick(30)
       pygame.quit()
       quit()

              

def collision(block_x,block_y,block_colour,snake_colour,lead_x,lead_y):
       points=0
       if(block_x==lead_x and block_y==lead_y):
              previous_colour=snake_colour
              snake_colour=choice(mycolours)
              if(block_colour==previous_colour):
                     points+=10
              else:
                     points-=10

       return points,snake_colour



       

def points_fun(p):
       if p<=0:
              gameDisplay.blit(game_over,[108,400])
              
              return True
       else:
              
              return False


       
def amazo(colour,lead_x,lead_y):
       pygame.draw.rect(gameDisplay, colour, [lead_x,lead_y,20,20])





clock = pygame.time.Clock()

rand_xNy=[[29,100],[210,180],[450,90],[700,190],[90,220],[300,300],[500,390],[610,250],[33,450],[230,550],[500,500],[750,490],[180,650],[360,640],[490,700],[700,740]]


grid_list=[(j,i) for i in range(1,5) for j in range(1,5)]
print(grid_list)




colour_coordinates=list(zip(colours,rand_xNy))
print(colour_coordinates)
gcc=dict(zip(grid_list,colour_coordinates))
print(gcc)



game_intro()





