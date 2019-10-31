# Define enviroment parameter

WIDTH = 800
HEIGHT = 600
player_x = 500
player_y = 550

def draw():
    screen.blit(images.backdrop,(0, 0))
    screen.blit(images.mars,(50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship,(130, 150))

def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5

clock.schedule_interval(game_loop, delay = 0.03)
    