from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
menu_sound = pygame.mixer.Sound("menusound.wav")

def menu():
    musica_menu = pygame.mixer.Sound("musicamenu.wav")
    musica_menu.play(loops = -1)
    musica_menu.set_volume(0.6)
    window = Window(800, 600)
    window.set_title("Valkyrie's Rise")

    mouse = Mouse()
    fundomenu = Sprite("fundomenu.png",1)
    playBtn = Sprite("playtest.png")
    playBtn.set_position(window.width/2 - playBtn.width/2, window.height/2 - playBtn.height/2)
    exitBtn = Sprite("Quit.png")
    exitBtn.set_position(window.width/2 - exitBtn.width/2, window.height/2 - playBtn.height/2 + 70 +  exitBtn.height/2)
    while True:
        fundomenu.draw()
        playBtn.draw()
        exitBtn.draw()
        if mouse.is_over_object(playBtn):
                if mouse.is_button_pressed(1):
                    musica_menu.stop()
                    menu_sound.play()
                    return 1
        elif mouse.is_over_object(exitBtn):
                if mouse.is_button_pressed(1):
                    menu_sound.play()
                    exit()
        window.update()
        
        
def gameover():
    window = Window(800,600)
    window.set_title("Valkyrie's Rise")
    mouse = Mouse()
    hitbox = Sprite("hitboxbotao.png",1)
    hitbox.set_position(260,320)
    fundomenu1 = Sprite("game_over.png",1)
    while 1:
        if(mouse.is_over_object(hitbox)):
            fundomenu1 = Sprite("game_over_selec.png",1)
            if mouse.is_button_pressed(1):
                menu_sound.play()

                return 1
        else:
            fundomenu1 = Sprite("game_over.png",1)
        fundomenu1.draw()
        window.update()

def win():
    window = Window(800,600)
    window.set_title("Valkyrie's Rise")
    mouse = Mouse()
    hitbox = Sprite("hitboxbotao.png",1)
    hitbox.set_position(260,320)
    fundomenu1 = Sprite("game_win.png",1)
    while 1:
        if(mouse.is_over_object(hitbox)):
            fundomenu1 = Sprite("game_win_selec.png",1)
            if mouse.is_button_pressed(1):
                menu_sound.play()
                fim()
                
        else:
            fundomenu1 = Sprite("game_win.png",1)
        fundomenu1.draw()
        window.update()
    
def fim():
    window = Window(800,600)
    window.set_title("Valkyrie's Rise")
    fundomenu1 = Sprite("fim.png",1)
    teclado = window.get_keyboard()
    while 1:
        fundomenu1.draw()
        window.update()
        if teclado.key_pressed("esc"):
            exit()
        