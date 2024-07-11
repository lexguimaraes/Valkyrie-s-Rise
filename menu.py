from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *

def menu():
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
                    return 1
        elif mouse.is_over_object(exitBtn):
                if mouse.is_button_pressed(1):
                    exit()
        window.update()