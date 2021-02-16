import pygame
import os
import random

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
FPS = 60
is_game_over = False
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Helix Jump')
ball = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ball.png')), (50, 50))
ball_rect = pygame.Rect(155, 10, 50, 50)
VELOCITY = 5

rect_one = pygame.Rect(random.randint(0, 260), 450, 100, 50)
rect_two = pygame.Rect(random.randint(0, 260), 450, 100, 50)
rect_vel = 5
main_rect = pygame.Rect(0, 450, 360, 50)

losing_font = pygame.font.SysFont('comicsans', 100)
text = losing_font.render('You Lost!!', 1, (0, 0, 0))

score_font = pygame.font.SysFont('comicsans', 50)
score = 0
s = pygame.transform.scale(score_font.render('S', 1, (0, 255, 0)), (73, 73))
s_rect = pygame.Rect(390, 0, 80, 80)
c = pygame.transform.scale(score_font.render('C', 1, (0, 255, 0)), (73, 73))
c_rect = pygame.Rect(390, 75, 73, 73)
o_rect = pygame.Rect(390, 150, 73, 73)
r_rect = pygame.Rect(390, 225, 73, 73)
e_rect = pygame.Rect(390, 300, 73, 73)
o = pygame.transform.scale(score_font.render('O', 1, (0, 255, 0)), (73, 73))
r = pygame.transform.scale(score_font.render('R', 1, (0, 255, 0)), (73, 73))
e = pygame.transform.scale(score_font.render('E', 1, (0, 255, 0)), (73, 73))
equal = pygame.transform.scale(score_font.render('=', 1, (0, 0, 255)), (73, 37))
equal_rect = pygame.Rect(390, 375, 73, 37)
score_Rect = pygame.Rect(390, 420, 75, 75)

def draw():
    screen.fill((255, 255, 255))
    screen.blit(s, s_rect)
    screen.blit(c, c_rect)
    screen.blit(o, o_rect)
    screen.blit(r, r_rect)
    screen.blit(e, e_rect)
    screen.blit(equal, equal_rect)
    screen.blit(score_text, score_Rect)
    pygame.draw.line(screen, (0, 0, 0), (360, 0), (360, 500))
    pygame.draw.rect(screen, (255, 255, 255), main_rect)
    screen.blit(ball, ball_rect)
    pygame.draw.rect(screen, (0, 0, 255), rect_one)
    pygame.draw.rect(screen, (0, 0, 255), rect_two)

def ball_control(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and ball_rect.x - VELOCITY > 0:
        ball_rect.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and ball_rect.x + VELOCITY + ball_rect.width < 360:
        ball_rect.x += VELOCITY

def matter_of_life_and_death():
    if main_rect.y == -100:
        main_rect.y = 450
        rect_two.y = 450
        rect_one.y = 450
        rect_one.x = random.randint(0, 260)
        rect_two.x = random.randint(0, 260)


while not is_game_over:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys_pressed = pygame.key.get_pressed()
    ball_control(keys_pressed)

    rect_one.y -= rect_vel
    rect_two.y -= rect_vel
    main_rect.y -= rect_vel

    score_text = pygame.transform.scale(score_font.render(str(score), 1, (255, 0, 0)), (75, 75))
    draw()
    matter_of_life_and_death()
    if main_rect.y + main_rect.height == ball_rect.y:
        score += 1
    if rect_one.colliderect(ball_rect) or rect_two.colliderect(ball_rect):
        is_game_over = True
    pygame.display.update()

text2 = losing_font.render(f'Score: {score}', 1, (0, 0, 0))

rect = pygame.Rect(100, 175, 300, 100)
rect2 = pygame.Rect(100, 300, 300, 100)

while is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    screen.blit(text, rect)
    screen.blit(text2, rect2)
    pygame.display.update()