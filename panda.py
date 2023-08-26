import sys

import pygame
from pygame.locals import QUIT
from moviepy.editor import VideoFileClip
import random

def collides_with_rocks(x, y):
    # Check if the provided position collides with any of the rock positions
    for rock_x, rock_y in rock_positions:
        if pygame.Rect(x, y, char.get_width(), char.get_height()).colliderect(
            pygame.Rect(rock_x, rock_y, rock_image.get_width(), rock_image.get_height())
        ):
            return True
    return False

pygame.init()
screen_width = 800
screen_height = 600

border_x_left = 715
border_x_right = 0
border_y_top = 4
border_y_bottom = 520 

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('panda gay af')
background_image = pygame.image.load("sa.png") 
background_image = pygame.transform.scale(background_image, (800, 600))
background_image_menu = pygame.image.load("mainscreen.png") 
background_image_menu = pygame.transform.scale(background_image_menu, (800, 600))
#panda_shipp = pygame.image.load("ship.png")
#panda_shipp = pygame.transform.scale(panda_ship, (60, 120))

play_button_image = pygame.image.load("button_green.png")
play_button_hover_image = pygame.image.load("button_white.png")

score_background_image = pygame.image.load("ring_counter.png")

planet1 = pygame.image.load("src/palnets/forest/grasss.png")
planet1 = pygame.transform.scale(planet1, (800, 600))

planet2 = pygame.image.load("src/palnets/lava/lavafloor/lavafloor8.png")
planet2 = pygame.transform.scale(planet2, (800, 600))

char = pygame.image.load("src/astronaut/astronaut_down/astronautdown1.png")
char = pygame.transform.scale(char, (50, 50))

rock_image = pygame.image.load("src/palnets/forest/rock1.png")
rock_image = pygame.transform.scale(rock_image, (50, 50))

fuel_tank_image = pygame.image.load("src/ui/fueltank.png") 
fuel_tank_image = pygame.transform.scale(fuel_tank_image, (40, 40))

enemy_image = pygame.image.load("src/palnets/forest/enemy/brownalien1.png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

rock_positions = [(400,200),(1, 10),(1, 60),(1, 110),(1, 160),(1, 210),(1, 260),(1, 310),(1, 360),(1, 410),(1, 460),(1, 540),(1, 540),(50, 540), (100, 540) ,(150, 540) ,(200, 540) ,(250, 540) ,(300, 540) ,(350, 540) ,(400, 540) ,(450, 540) ,(500, 540) ,(550, 540) ,(600, 540) ,(650, 540) ,(700, 540) ,(750, 540) ,(800, 540), (800, 10),(800, 60),(800, 110),(800, 160),(800, 210),(800, 260),(800, 310),(800, 360),(800, 410),(800, 460),(800, 540),(750, 540),(700, 540),(650, 540),(600, 540),(550, 540),(500, 540),(450, 540),(400, 540),(350, 540),(300, 540),(250, 540),(200, 540),(150, 540),(100, 540),(50, 540),(0, 540),(0, 10),(0, 60),(0, 110),(0, 160),(0, 210),(0, 260),(0, 310),(0, 360),(0, 410),(0, 460),(0, 540),(50, 540),(100, 540),(150, 540),(200, 540),(250, 540),(300, 540),(350, 540),(400, 540),(450, 540),(500, 540),(550, 540),(600, 540),(650, 540),(700, 540),(750, 540),(800, 540)]


#r1 = VideoFileClip("r1.gif")
r1_frames = []
r1_frame = 0

rings_frames = []
rings_frame = 0

portal1_frames = []
portal1_frame = 0

portal2_frames = []
portal2_frame = 0

fuel_bar_images  = []
fuelbar_frame = 0

current_portal_frames = []
current_portal_frame = 0

portal_type = "forest"

on_planet = False

#panda_ship = pygame.image.fromstring(r1_frames[r1_frame].tostring(), r1.size, "RGB")
for i in range(1, 9): 
    frame_path = f"src/portals/portal_1/portal{i}.png"  
    frame = pygame.image.load(frame_path).convert_alpha()
    frame = pygame.transform.scale(frame, (80, 80))
    portal1_frames.append(frame)

for i in range(1, 9): 
    frame_path = f"src/portals/portal_2/portal{i}.png"  
    frame = pygame.image.load(frame_path).convert_alpha()
    frame = pygame.transform.scale(frame, (80, 80))
    portal2_frames.append(frame)

    
for i in range(1, 8): 
    frame_path = f"spaceship/re{i}.png"  
    frame = pygame.image.load(frame_path).convert_alpha()
    frame = pygame.transform.scale(frame, (80, 120))
    r1_frames.append(frame)

for i in range(1, 10): 
    frame_path = f"fuelbar/fuelbar{i}.png"  
    frame = pygame.image.load(frame_path).convert_alpha()
    frame = pygame.transform.scale(frame, (60, 400))
    fuel_bar_images.append(frame)

for i in range(1, 9): 
    frame_path = f"rings/energyring{i}.png"  
    frame = pygame.image.load(frame_path).convert_alpha()
    frame = pygame.transform.scale(frame, (80, 80))
    rings_frames.append(frame)

panda_ship = r1_frames[r1_frame]

rings = rings_frames[rings_frame]

portal = portal1_frames[current_portal_frame]

character_x = (screen_width - char.get_width()) // 2
character_y = (screen_height - char.get_height()) // 2
character_speed = 5

enemy_x = 300
enemy_y = 200
enemy_speed = 3
enemy_direction = 1

ring_x = 100
ring_y = -50
ring_speed = 8

portal_x = 100
portal_y= -50
portal_speed = 4

last_ring_spawn_time = pygame.time.get_ticks()
ring_spawn_interval = 9000

last_portal_spawn_time = pygame.time.get_ticks()
portal_spawn_interval = 3000

score = 0

font = pygame.font.Font(None, 36)
text_color = (0,0,0)

fuel_level = 100
fuel_depletion_rate = 0.03

clock = pygame.time.Clock()
bg_y = 0

scroll_speed = 2
running = True

show_menu = True
play_button_rect = play_button_image.get_rect(center=(screen_width // 2, screen_height // 1.5))
menu_font = pygame.font.Font(None, 48)
menu_text_color = (255, 255, 255)
play_text = menu_font.render("Play", True, menu_text_color)
play_rect = play_text.get_rect(center=(screen_width // 2, screen_height // 2))
blurred_background = pygame.Surface((screen_width, screen_height))
blurred_background.blit(background_image_menu, (0, 0))
blurred_background.set_alpha(128)


ship_x = (screen_width - panda_ship.get_width()) // 2
ship_y = (screen_height - panda_ship.get_height()) // 1.1

frame_counter_ship = 0
frame_update_rate_ship = 5

frame_counter_ring = 0
frame_update_rate_ring = 5

frame_counter_portal = 0
frame_update_rate_portal = 5

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if show_menu and play_button_rect.collidepoint(event.pos):
            show_menu = False
  if on_planet:
      
      if portal_type == "forest":
          fuel_tank_position = (670,500)

          fuel_tank_rect = fuel_tank_image.get_rect(topleft=fuel_tank_position)
          #print(character_x, character_y)
          screen.blit(planet1, (0, 0))
          for rock_x, rock_y in rock_positions:
              screen.blit(rock_image, (rock_x, rock_y))
          screen.blit(char, (character_x, character_y))
          screen.blit(enemy_image, (enemy_x, enemy_y))
          screen.blit(fuel_tank_image, fuel_tank_position)

          if on_planet and pygame.Rect(character_x, character_y, char.get_width(), char.get_height()).colliderect(fuel_tank_rect):
             fuel_level = 100
             on_planet = False
             fuel_tank_position = (-100, -100)
             character_x = (screen_width - char.get_width()) // 2
             character_y = (screen_height - char.get_height()) // 2  # Move fuel tank off-screen
          enemy_x += enemy_speed * enemy_direction
          if enemy_x <= 0 or enemy_x >= screen_width - enemy_image.get_width():
              enemy_direction *= -1

          if on_planet and pygame.Rect(character_x, character_y, char.get_width(), char.get_height()).colliderect(
        pygame.Rect(enemy_x, enemy_y, enemy_image.get_width(), enemy_image.get_height())
    ):
             character_x = (screen_width - char.get_width()) // 2
             character_y = (screen_height - char.get_height()) // 2
          keys = pygame.key.get_pressed()
          if keys[pygame.K_a] and character_x > 0 and not collides_with_rocks(character_x - character_speed, character_y):
              character_x -= character_speed
          if keys[pygame.K_d] and character_x < screen_width - char.get_width() and not collides_with_rocks(character_x + character_speed, character_y):
              character_x += character_speed
          if keys[pygame.K_w] and character_y > 0 and not collides_with_rocks(character_x, character_y - character_speed):
              character_y -= character_speed
          if keys[pygame.K_s] and character_y < screen_height - char.get_height() and not collides_with_rocks(character_x, character_y + character_speed):
              character_y += character_speed
      else:
          screen.blit(planet2, (0, 0))
  
  if show_menu:
      if play_button_rect.collidepoint(pygame.mouse.get_pos()):
          screen.blit(play_button_hover_image, play_button_rect)
      else:
          screen.blit(play_button_image, play_button_rect)
      screen.blit(blurred_background, (0, 0))
      #pygame.draw.rect(screen, (0, 0, 0), play_rect)
      #screen.blit(play_text, play_rect)
      bg_y += 2 
      if bg_y >= screen_height:
          bg_y = 0
      pygame.display.flip()
      continue
    
  bg_y += scroll_speed
  if bg_y >= screen_height:
    bg_y = 0
  clock.tick(60)
  pygame.display.flip()

  current_time = pygame.time.get_ticks()
  if current_time - last_ring_spawn_time >= ring_spawn_interval:
      ring_y = -50
      ring_x = random.randint(0, screen_width - 80)
      last_ring_spawn_time = current_time

  if current_time - last_portal_spawn_time >= portal_spawn_interval:
        portal_y = -50
        portal_x = random.randint(0, screen_width - 80)
        last_portal_spawn_time = current_time

  if(portal_type == "forest"):
      current_portal_frames = portal1_frames
  else:
      current_portal_frames = portal2_frames

  fuel_level -= fuel_depletion_rate
  if fuel_level < 0:
      fuel_level = 0
     
  screen.fill((0, 0, 0))
  screen.blit(background_image, (0, bg_y))
  screen.blit(background_image, (0, bg_y - screen_height))
  screen.blit(panda_ship, (ship_x, ship_y))
  screen.blit(rings, (ring_x, ring_y))
  screen.blit(portal, (portal_x, portal_y))
  #score_text = font.render(f"Rings collected: {score}", True, text_color)
  #pygame.draw.rect(screen, (0, 0, 0), (10, 10, score_text.get_width() + 20, score_text.get_height() + 20))
  #screen.blit(score_text, (20, 20))
  score_text = font.render(f"Rings collected: {score}", True, text_color)
  score_box_width = score_text.get_width() + 20
  score_background_rect = pygame.Rect(10, 10, score_box_width, score_text.get_height())
  score_background_image = pygame.transform.scale(score_background_image, (score_text.get_width()+90, score_text.get_height() + 38))
  screen.blit(score_background_image, score_background_rect)
  screen.blit(score_text, (48, 29))
  fuel_bar_height = fuel_bar_images[0].get_height()
  #pygame.draw.rect(screen, (0, 0, 0), (screen_width - 40, screen_height - fuel_bar_height, 30, fuel_bar_height))

  fuel_bar_image_index = int(fuel_level / 100 * (len(fuel_bar_images) - 1))
  fuel_bar_image_index = max(0, min(fuel_bar_image_index, len(fuel_bar_images) - 1))
  fuel_bar_image = fuel_bar_images[len(fuel_bar_images) - 1 - fuel_bar_image_index] 
  fuel_bar_rect = fuel_bar_image.get_rect(center=(screen_width - 35, screen_height - fuel_bar_height /1.5))
  screen.blit(fuel_bar_image, fuel_bar_rect)

  ring_y += ring_speed

  portal_y += portal_speed
        
  frame_counter_ship += 1
  if frame_counter_ship >= frame_update_rate_ship:
      frame_counter_ship = 0
      r1_frame = (r1_frame + 1) % len(r1_frames)
      panda_ship = r1_frames[r1_frame]

      
  frame_counter_ring += 1
  if frame_counter_ring >= frame_update_rate_ring:
      frame_counter_ring = 0
      rings_frame = (rings_frame + 1) % len(rings_frames)
      rings = rings_frames[rings_frame]

  frame_counter_portal += 1
  if frame_counter_portal >= frame_update_rate_portal:
      frame_counter_portal = 0
      current_portal_frame = (current_portal_frame + 1) % len(current_portal_frames)
      portal = current_portal_frames[current_portal_frame]

    

  
  keys = pygame.key.get_pressed()
  if keys[ord('a')]:
    if(ship_x > border_x_right):
      #print(ship_x)
      ship_x -= 5
      screen.blit(panda_ship, (ship_x, ship_y))

  if keys[ord('d')]:
    if(ship_x < border_x_left):
      #print(ship_x)
      ship_x += 5
      screen.blit(panda_ship, (ship_x, ship_y))

  if keys[ord('w')]:
    if(ship_y > border_y_top):
      ship_y -= 5
      screen.blit(panda_ship, (ship_x, ship_y))

  if keys[ord('s')]:
    if(ship_y < border_y_bottom):
      ship_y += 5
      screen.blit(panda_ship, (ship_x, ship_y))

  if pygame.Rect(ship_x, ship_y, panda_ship.get_width(), panda_ship.get_height()).colliderect(
        pygame.Rect(ring_x, ring_y, rings.get_width(), rings.get_height())
    )and on_planet == False:
      score += 1
      ring_y = 1000
      #ring_x = random.randint(0, screen_width - ring.get_width())

  if pygame.Rect(ship_x, ship_y, panda_ship.get_width(), panda_ship.get_height()).colliderect(
        pygame.Rect(portal_x, portal_y, portal.get_width(), portal.get_height())
    )and on_planet == False:
     on_planet = True

  if(score >= 10):
      portal_type = "lava"


  
  #pygame.display.update()

