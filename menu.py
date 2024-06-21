from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import main

def menu():
    window = Window(800, 600)
    window.set_title("Valkyrie's Rise")

    mouse = Mouse()

    playBtn = Sprite("Play.png")
    playBtn.set_position(window.width/2 - playBtn.width/2, window.height/2 - playBtn.height/2)
    playBtnClicked = Sprite("Play.png")
    playBtnClicked.set_position(playBtn.x, playBtn.y)

    exitBtn = Sprite("Sair.png")
    exitBtnClicked = Sprite("Sair.png")
    exitBtnClicked.set_position(exitBtn.x, exitBtn.y)
    playing = False
    while True:
        playBtn.draw()
        if mouse.is_over_object(playBtn) and not playing:
                playBtnClicked.draw()
                if mouse.is_button_pressed(1):
                    playing = True
                    main()
        elif mouse.is_over_object(exitBtn):
                exitBtnClicked.draw()
                if mouse.is_button_pressed(1):
                    exit()
        window.update()
        