import pyxel

pyxel.init(128,128, title="Player Gravité")

player_x = 0
player_y = 0
v = 0

def deplacement(vitesse, gravite, coos_y):
    if coos_y > pyxel.height-17 :
        vitesse = 0
    vitesse2 = vitesse + gravite * 1/30
    coos_y = coos_y + vitesse2
    return vitesse2, coos_y

def update():
    global player_x, player_y, v
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
        player_x = max(player_x - 2, 0)
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
        player_x = min(player_x + 2, pyxel.width - 5)
    
    if player_y >= pyxel.height - 17 :
        player_y = pyxel.height - 17
        v = 0
        
    if pyxel.btn(pyxel.KEY_SPACE) and player_y >= pyxel.height - 17 :
        v = -5
        
    
    #On sait que l'on regarde 30 fois par seconde
    #On considère que 10 pixels valent 1 mètre On considère g = 9.88
    v = deplacement(v, 9.88, player_y)[0]
    player_y = deplacement(v, 9.88, player_y)[1]

def draw():
    pyxel.cls(0)
    pyxel.rect(player_x, player_y, 5,17,1)
    
pyxel.run(update, draw)    
