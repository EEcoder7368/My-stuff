import pygame
import time
import random

from pygame import(
   K_UP,
   K_w,
   K_LEFT,
   K_a,
   K_RIGHT,
   K_d,
   K_r,
   QUIT,
   K_ESCAPE,
)
#have to blit image on
pygame.init()
screen_length = 600
screen = pygame.display.set_mode((screen_length, screen_length))
pygame.display.set_caption("Robobuild - The simple version")
font = pygame.font.SysFont(None, 36)
score = 0
jump_distance = 0
is_jumping = False

player_pos = [275, 0]
prev_pos = player_pos
pos_choice = random.randint(0, 2)
part_box = pygame.Rect(0, 0, 1, 1)
lava = pygame.Rect(0, 0, 1, 1,)
lava_choice = random.randint(0, 2)
plats = [None, None, None]
y_vel = 0
player_img = pygame.image.load("[insert_file_name_here].png")
plat_img = pygame.image.load("[insert_file_name_here].png")
part_box_img = pygame.image.load("")
lava_img = pygame.image.load("")

def plat_draw(plat_name, posx, posy):
    plat_name = pygame.Rect(posx, posy, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), (posx, posy, 200, 50))
    return plat_name
def centre(x, width):
    x -= (width / 2)
    return x
def gravity(vel):
   if vel != -0.5:
     vel -= 0.5
   return vel
def draw(posx, posy, collidor, R = 194, G = 146, B = 103, length = 50, width = 50):
  pygame.draw.rect(screen, (R, G, B), (posx, posy, length, width))
  collidor = pygame.Rect(posx, posy, length, width)
  return collidor
def draw_rect(choice, collidor, change_from_50 = 0, R = 194, G = 146, B = 103, width = 50, length = 50):
  if choice == 0:
    collidor = draw(275, (180 + change_from_50), collidor, R, G, B, length, width)
  if choice == 1:
    collidor = draw(20, (300 + change_from_50), collidor, R, G, B, length, width)
  if choice == 2:
    collidor = draw(530, (300 + change_from_50), collidor, R, G, B, length, width)
  return collidor

running = True
while running:
  while lava_choice == pos_choice:
    lava_choice = random.randint(0, 2)
  screen.fill((255, 255, 255))
  keys = pygame.key.get_pressed()
  y_vel = gravity(y_vel)
  
  part_box = draw_rect(pos_choice, part_box)
  lava = draw_rect(lava_choice, lava, 25, 255, 0, 0, 25)
  plats[0] = plat_draw(plats[0], centre(490, 200), 350)
  plats[1] = plat_draw(plats[1], centre(300, 200), 230)
  plats[2] = plat_draw(plats[2], centre(110, 200), 350)
  player = pygame.Rect(player_img.get_rect(), 50, 50)
  for i in plats:
    if i.colliderect(player):
      player_pos = prev_pos
      y_vel = 0
    else:
      prev_pos = player_pos
  if player.colliderect(part_box):
    pos_choice = random.randint(0, 2)
    score += random.randint(1, 10)
  elif player.colliderect(lava):
    while True:
      lava_choice = random.randint(0, 2)
      if lava_choice != pos_choice:
        break
    score -= random.randint(1, 10)
    if score < 0:
      score = 0
    
  if score < 100:
    text_surface = font.render(f"{score}/100", True, (0, 0, 0))
    screen.blit(text_surface, (500, 5))
  else:
    font = pygame.font.SysFont(None, 100)
    text_surface = font.render("YOU WIN!", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(text_surface, (centre(300, 325), centre(300, 68)))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

  for event in pygame.event.get():
    if event.type == QUIT or keys[pygame.K_ESCAPE]:
      running = False
    
  if keys[pygame.K_UP] or keys[pygame.K_w]:
    if any(player.colliderect(plat) for plat in plats):
      is_jumping = True
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    player_pos[0] -= 1
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player_pos[0] += 1
  if keys[pygame.K_r]:
    y_vel = 0
    player_pos[0] = centre(300, 50)
    player_pos[1] = 0

  if jump_distance != 17 and is_jumping:
    y_vel += 1
    jump_distance += 1
  elif jump_distance == 17:
    is_jumping = False
    jump_distance = 0

  player_pos[1] -= y_vel
  pygame.draw.rect(screen, (0, 0, 0), (player_pos[0], player_pos[1], 50, 50))
  pygame.display.flip()

pygame.quit()
