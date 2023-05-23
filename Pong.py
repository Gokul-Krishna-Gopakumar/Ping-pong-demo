import pygame, sys, random

#animation-function
def ball_animation():
        #animation
        global ball_speed_x,ball_speed_y,player_score,opponent_score
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        #animation boundry-collision logic
        if ball.top <= 0 or ball.bottom >= screen_height:
                ball_speed_y *= -1
        '''if ball.left <=0 or ball.right >= screen_width:
                ball_restart()'''
        if ball.left <=0 :
                opponent_score+=1
                ball_restart()
        if ball.right >=screen_width:
                player_score+=1
                ball_restart()                
        #animation collision-player-opponent logic
        if ball.colliderect(player) or ball.colliderect(opponent):
                ball_speed_x *= -1

def player_animation():
        player.y += player_speed
        if player.top<=0:
                player.top=0
        if player.bottom>=screen_height:
                player.bottom=screen_height

def opponent_animation():
        if opponent.top < ball.y:
                opponent.top += opponent_speed
        if opponent.bottom > ball.y:
                opponent.bottom -= opponent_speed
        if opponent.top<=0:
                opponent.top=0
        if opponent.bottom>=screen_height:
                opponent.bottom=screen_height
                
def ball_restart():
        global ball_speed_x, ball_speed_y
        ball.center=(screen_width/2, screen_height/2)
        ball_speed_y *= random.choice((1,-1))
        ball_speed_x *= random.choice((1,-1))

#general setup
pygame.init()
clock = pygame.time.Clock()

#main window setup
screen_width =1200
screen_height=960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#game rectangles
ball= pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70 ,10,140)
opponent = pygame.Rect(10, screen_height/2-70, 10,140) 


#color elements
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#ball-variables
ball_speed_x=7 * random.choice((1,-1))
ball_speed_y=7 * random.choice((1,-1))
player_speed=0
opponent_speed=7

#score variables
player_score=0
opponent_score=0


WHITE=(255,255,255)

while True:
        #handling input
        for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                #keyboard inputs for game
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                                player_speed +=7
                        if event.key == pygame.K_UP:
                                player_speed -=7
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                                player_speed -=7
                        if event.key == pygame.K_UP:
                                player_speed +=7 

        #animations        
        ball_animation()
        player_animation()
        opponent_animation()
        

        #visuals
        screen.fill(bg_color)
        pygame.draw.rect(screen,light_grey,player)
        pygame.draw.rect(screen,light_grey,opponent)
        pygame.draw.ellipse(screen,light_grey,ball)
        pygame.draw.aaline(screen,light_grey,(screen_width/2,0), (screen_width/2,screen_height))
        '''pygame.draw.rect(screen, light_grey,player_score)
        pygame.draw.rect(screen,light_grey,opponent_score)'''

        #updating score
        font = pygame.font.Font(None, 75)
        text = font.render(str(player_score), 1, WHITE)
        screen.blit(text, (screen_width/4,10))
        text = font.render(str(opponent_score), 1, WHITE)
        screen.blit(text, (screen_width*3/4,10))

        '''if player_score == 10 or opponent_score == 10:
                text = font.render("Game Over", 1, WHITE)
                player_speed=0
                opponent_speed=0
                ball_speed_x=0
                ball_speed_y=0'''

        #updating window
        pygame.display.flip()
        clock.tick(60)

