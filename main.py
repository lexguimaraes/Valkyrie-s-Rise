from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import time
import menu

playing = False
paused = True
playing = menu.menu()
paused = False
class enemy():
    def __init__(self,pos,patru):
        self.i_pos = pos
        self.e_cooldown = 0
        self.hitbox = Sprite("HitBoxRun.png",1)
        self.sprite = Sprite("GoblinRun.png",8)
        self.sprite.set_sequence_time(0,7,100,True)
        self.sprite.set_position(self.i_pos[0],self.i_pos[1])
        self.hitbox.set_position(self.sprite.x+190,self.sprite.y+200)
        self.vel=100
        self.h_cooldown = 0
        self.dif=0
        self.dife = 0
        self.difk = 0
        self.knock=1000
        self.flip = False
        self.hp = 4
        global ch_cooldown
        ch_cooldown=0
        self.attacking = False
        self.goblin_attack_cd = -101
        self.attack_hitbox = Sprite("HitBoxRun.png",1)
        self.attack_hitbox.set_position(self.hitbox.x+(75),self.hitbox.y)
        self.patrulha = [patru[0],patru[1]]
        
        
    def movement(self):      
        if self.hitbox.x + self.hitbox.width >= self.patrulha[1] and self.vel >0:
            self.vel*=-1
        if self.hitbox.x < self.patrulha[0] and self.vel <0 :
            self.vel*=-1
        if not self.attacking:
            self.sprite.x+=self.vel*janela.delta_time() 
            
            
    def attack(self):
        
        ##print(int(char.x),int(self.hitbox.x) )
        if self.attack_hitbox.collided(hitbox) and not self.attacking and self.goblin_attack_cd<-100 and not morto:
            self.i_pos = [self.sprite.x,self.sprite.y]
            self.sprite = Sprite("GoblinAttack.png",8)
            self.sprite.set_sequence_time(0,7,50, False)
            self.sprite.set_position(self.i_pos[0],self.i_pos[1])
            self.attacking = True
            self.goblin_attack_cd = 70
        if self.attacking:
            self.goblin_attack_cd-=50*janela.delta_time()
        if self.goblin_attack_cd <= 0:
            self.attacking = False
        self.goblin_attack_cd-=100*janela.delta_time()
        
        
    
    def damage(self):
        if (self.hitbox.collided(hitbox) or (self.attack_hitbox.collided(hitbox) and 0 <self.goblin_attack_cd <20))and self.h_cooldown <= 0 and not dashing and ch_cooldown <=0 and char.file_name!="Hurt.png" and not morto:
            self.dif = 50
            self.h_cooldown = 100
            global Player_hp
            Player_hp -=1 
        if self.dif>0:       
            if  (self.vel<0):
                if char.x+60>0:
                    char.x-=350*janela.delta_time()
            else:
                if char.x + char.width -60< janela.width:
                    char.x+=350*janela.delta_time()
            char.y-=350*janela.delta_time()    
            self.dif-=350*janela.delta_time()
            global hurt
            hurt = True  
            
                  
        if self.h_cooldown >0:
            self.h_cooldown-=500*janela.delta_time()
            if self.h_cooldown == 0:
                hurt = False
            
    def direction(self):        
        if self.vel>0:
            self.flip= False
        else:
            self.flip=True
            
    def loop(self):  
        if self.hp>0:        
            self.damage()
            self.damaged()
            self.attack()
            self.direction()
            self.movement()
            self.update()
            self.draw()         
        else:
            self.sprite.update()
            if self.hp == 0:
                self.i_pos = [self.sprite.x,self.sprite.y]
                self.sprite = Sprite("GoblinDeath.png",4)
                self.sprite.set_sequence_time(0,3,100,False)
                self.sprite.set_position(self.i_pos[0],self.i_pos[1])
                self.death_cd = 100
            if self.death_cd > 0 :
                self.sprite.draw()
                self.sprite.update()
                self.death_cd-=160*janela.delta_time()
            self.hp-=1
        
    def draw(self):
        self.hitbox.draw(self.flip,True)
        self.sprite.draw(self.flip)   
        self.attack_hitbox.draw(self.flip,True)
        self.sprite.update()
        
    def damaged(self):
        if self.hitbox.collided(a_hitbox) and attacking and self.e_cooldown <= 0 and not self.attacking :
            self.difk = 100
            self.e_cooldown = 40
            if dashing == True:
                self.knock = 1750
                self.difk=160  
            if flip == True:
                self.knock *=-1
            print(self.hp)
            if self.hp>1:
                self.i_pos = [self.sprite.x,self.sprite.y]
                self.sprite = Sprite("GoblinHurt.png",4)
                self.sprite.set_sequence_time(0,3,130, False)
                self.sprite.set_position(self.i_pos[0],self.i_pos[1])
            #else:
                #self.i_pos = [self.sprite.x,self.sprite.y]
                #self.sprite = Sprite("GoblinHurt.png",4)
                #self.sprite.set_sequence_time(0,3,200,False)
                #elf.sprite.set_position(self.i_pos[0],self.i_pos[1])
            self.hp-=1
        if self.difk >0:
            #self.sprite.x +=self.knock*janela.delta_time()
            self.difk -= abs(self.knock*janela.delta_time())
            if self.difk<=0:
                self.knock=1000    
                    
        if self.e_cooldown>0:
            self.e_cooldown -=100*janela.delta_time()

    def update(self):
        self.hitbox.set_position((self.sprite.x) +190,(self.sprite.y) +200)
        if self.flip:
            self.attack_hitbox.set_position(self.hitbox.x-75,self.hitbox.y)
        else:
            self.attack_hitbox.set_position(self.hitbox.x+75,self.hitbox.y)
        #print(self.sprite.is_playing())
        if (not self.sprite.is_playing()) and not self.attacking:
            self.i_pos = [self.sprite.x,self.sprite.y]
            self.sprite = Sprite("GoblinRun.png",8)
            self.sprite.set_sequence_time(0,6,80, True)
            self.sprite.set_position(self.i_pos[0],self.i_pos[1])
        
class plataforma():
    def __init__(self, x1,x2,y1,y2):
        self.hitboxcima = Sprite("HitboxCima.png",1)
        self.hitboxcima.set_position(x1+15,y1)
        self.hitboxbaixo = Sprite("HitboxCima.png",1)
        self.hitboxbaixo.set_position(x1+15,y2)
        self.hitboxladod = Sprite("Hitboxlado.png",1)
        self.hitboxladoe = Sprite("Hitboxlado.png",1)
        self.hitboxladod.set_position(x2,y1+10)
        self.hitboxladoe.set_position(x1,y1+10)
    def loop(self):
        self.hitboxcima.draw(sprite = True)
        self.hitboxbaixo.draw(sprite = True)
        self.hitboxladod.draw(sprite = True)
        self.hitboxladoe.draw(sprite = True)
        
        
    
    
        
janela = Window(800, 608)
hurt = False
ch_cooldown = 0
janela.set_title("vasco")
teclado = Window.get_keyboard()
fundo = Sprite("map.png",1)
hitbox = Sprite("Hitbox.png",1)
a_hitbox = Sprite("Hitbox.png",1)
char = Sprite("CharRun.png",8)
char.set_sequence_time(0,7,100, True) 
char.set_position(0, 340)
vel = 1
gravity = 300
jumping = False
dif = 0
difd=0
Player_hp = 3
lastpos = []
flip = 0
walking = False
idling = False
dashing = False
attacking = False
a_cooldown = 0
d_cooldown = 0
e_cooldown = 0
j_vel = 500
tick = 0
tempo = 0
usado = 100
fps=0
morto = False
deathtimer = 0
ListaInimigios = []
ListaPlataformas = []
ListaPlataformas.append(plataforma(10*16,21*16,18*16,21*16)) 
ListaPlataformas.append(plataforma(26*16,37*16,13*16,16*16))
ListaPlataformas.append(plataforma(43*16,49*16,8*16,11*16))
def em_solo(char,hitbox, ListaPlataformas):
    if char.y >= 340:
        return 1
    for i in ListaPlataformas:
        if(hitbox.collided(i.hitboxcima)):
            return 1
    return 0    
def colide_plat_d(hitbox, ListaPlataformas):
    for i in ListaPlataformas:
        if (hitbox.collided(i.hitboxladod)):
            return 1
    return 0
def colide_plat_e(hitbox, ListaPlataformas):
    for i in ListaPlataformas:
        if(hitbox.collided(i.hitboxladoe)):
            return 1
    return 0 
    
while 1 and playing and not paused:
    if(len(ListaInimigios)== 0):
        #print("a")
        ListaInimigios.append(enemy([200,180],[200,800]))
        pass
    if(not Player_hp):
        if (not morto):
            lastpos = [char.x,char.y]
            char = Sprite("PlayerDeath.png",11)
            char.set_sequence_time(0,10,120,False)
            char.set_position(lastpos[0],lastpos[1]+10)
            morto = True
            deathtimer = 2.3
        if(char.is_playing() == False and morto and deathtimer <=0):
            paused = False
            playing = False
            playing = menu.menu()
            paused = playing
            Player_hp = 3
            morto = False
            char = Sprite("CharRun.png",8)
            char.set_sequence_time(0,7,100, True) 
            dif = 0
            difd = 0
            char.set_position(0, 340)
            ListaInimigios.clear()
            ListaInimigios.append(enemy([200,180],[200,800]))
        deathtimer-=janela.delta_time()
        janela.update()
        fundo.draw()
        char.draw(flip)
        char.update()
    ##INVENCIVEL DPS DE TOMAR DANO
    if ch_cooldown>0:
        ch_cooldown-=100*janela.delta_time()
    tempo += janela.delta_time()
    tick+=1
    if tempo >=1:
        fps = tick
        tick = 0
        tempo =0
    #FUNDO NO INICIO PARA FICAR ATRAS SEMPRE
    if(not morto):
        fundo.draw()
    if hurt and not morto:
        ch_cooldown=100
        dif=0
        lastpos= [char.x,char.y]
        char = Sprite("Hurt.png",4)
        char.set_sequence_time(0,3,80,True)
        char.set_position(lastpos[0],lastpos[1])
        hurt = False
    for i in ListaInimigios:
        i.loop()
        print("a")
    #enemy2.loop()
    #HITBOX NO CHAR
    if e_cooldown>0:
        e_cooldown -=1
    if not flip:
        hitbox.set_position(char.x + char.width/3.85, char.y+ char.height/4)
        a_hitbox.set_position(hitbox.x + hitbox.width, hitbox.y - 10) 
    else:
        hitbox.set_position(char.x + char.width/2.5, char.y + char.height/4)
        a_hitbox.set_position(hitbox.x - hitbox.width,hitbox.y- 10)
    #GRAVIDADE E FIM DO PULO    
    if not em_solo(char,hitbox, ListaPlataformas):
        char.y+= gravity*janela.delta_time()
    else: 
        if jumping:
            jumping = False
            char.stop()
    #PULO
    if (teclado.key_pressed("SPACE") or teclado.key_pressed("W"))and jumping == False and char.file_name != "Hurt.png" and not morto:
        jumping = True
        dif = 100
        usado = 0
        if not attacking:
            lastpos = [char.x,char.y]
            char = Sprite("jump.png",3)
            char.set_sequence_time(0,2,80, True)
            char.set_position(lastpos[0],lastpos[1])
    
    
    if jumping == True:
        if teclado.key_pressed("SPACE")and usado <150:
            dif +=300*janela.delta_time()
            #usado+=100*janela.delta_time()
        for i in ListaPlataformas:
            if(hitbox.collided(i.hitboxbaixo)):
                dif = 0
        gravity = 0
        if dif > 0:
            char.y-=j_vel*janela.delta_time()
            dif -=j_vel*janela.delta_time()
            usado +=j_vel*janela.delta_time()
        else:
            gravity = 340
            
    #ANIMAÇÃO PRA CORRER
    if char.is_playing()==False and not dashing and not attacking and not morto:
        if walking == True:
            lastpos = [char.x,char.y]
            char = Sprite("CharRun.png",8)
            char.set_sequence_time(0,7,100, True)
            char.set_position(lastpos[0],lastpos[1])
        else:
            lastpos = [char.x,char.y]
            char = Sprite("Idle.png",6)
            char.set_sequence_time(0,5,100,True)
            char.set_position(lastpos[0],lastpos[1])
            idling = True
    
    #ANDAR
    walking = False
    if teclado.key_pressed("D") and hitbox.x + hitbox.width< janela.width and dashing == False and not morto and not colide_plat_e(hitbox, ListaPlataformas):
        if idling == True:
            idling = False
            if jumping == False and not attacking:
                char.stop()
        char.x+=200*janela.delta_time()
        flip = False
        walking = True
    if teclado.key_pressed("A") and hitbox.x> 0 and dashing == False and not morto and not colide_plat_d(hitbox,ListaPlataformas):
        if idling == True:
            idling = False
            if jumping == False and not attacking:
                char.stop()
        flip = True
        walking = True
        char.x -=200*janela.delta_time()
        
    #DASH    
    if teclado.key_pressed("LEFT_SHIFT") and dashing == False and d_cooldown <= 0 and not morto:
        dashing = True
        a_cooldown = 0
        difd = 200
        lastpos = [char.x,char.y]
        char = Sprite("dash.png",7)
        char.set_sequence_time(0,6,100,False)
        char.set_position(lastpos[0],lastpos[1])
    if dashing == True:
        dif = 0
        gravity = 0
        if flip == True:
            if difd > 0:
                if hitbox.x >0 and not colide_plat_d(hitbox,ListaPlataformas):
                    char.x-=800*janela.delta_time()
                    difd-=800*janela.delta_time()
                else:
                    difd=0
            else:
                j_vel = 500
                gravity = 300
                dashing = False
                d_cooldown = 100
                if jumping == True and not attacking:
                    lastpos = [char.x,char.y+20]
                    char = Sprite("jump.png",3)
                    char.set_sequence_time(0,2,80, True)
                    char.set_position(lastpos[0],lastpos[1])       
        else:
            if difd > 0:
                if hitbox.x + hitbox.width< janela.width and not colide_plat_e(hitbox, ListaPlataformas):
                    char.x+=600*janela.delta_time()
                    difd -=600*janela.delta_time()
                else:
                    difd=0
            else:
                dif = 0 
                gravity = 300
                dashing = False
                d_cooldown = 100
                if jumping == True and not attacking:
                    lastpos = [char.x,char.y+20]
                    char = Sprite("jump.png",3)
                    char.set_sequence_time(0,2,80, True)
                    char.set_position(lastpos[0],lastpos[1])
    if d_cooldown >0:
        d_cooldown -=150*janela.delta_time()     
        
    #ATAQUE
    if mouse.Mouse.is_button_pressed(mouse,1) and a_cooldown <=0 and not morto:
        lastpos = [char.x,char.y]
        attacking = True
        
        if not dashing:
            a_cooldown = 80
            char = Sprite("attack.png",12)
            char.set_sequence_time(0,11,50, False)
                    
        else:
            difd=70
            a_cooldown = 50
            char = Sprite("DashAttack.png",10)
            char.set_sequence_time(0,9,40,False)
        char.set_position(lastpos[0],lastpos[1])      
            
            
            
    if a_cooldown <= 0:
        attacking = False
        #a_cooldown-=1*janela.delta_time()
        if jumping == True and not dashing and char.file_name!="Hurt.png":
            lastpos = [char.x,char.y]
            time.sleep(0.001)
            char = Sprite("jump.png",3)
            char.set_sequence_time(0,2,80, True)
            char.set_position(lastpos[0],lastpos[1])  
            if char.y>350:
                char.stop()  
    if a_cooldown >0:
        a_cooldown -=125*janela.delta_time()
        
        
        
    #IDLE            
    if walking == False and jumping == False and idling == False and dashing == False and attacking == False and morto == False:
        print("a")
        lastpos = [char.x,char.y]
        char = Sprite("Idle.png",6)
        char.set_sequence_time(0,5,100,True)
        char.set_position(lastpos[0],lastpos[1])
        idling = True
    janela.draw_text(str(fps),5,5,30,(0,255,0))
    a_hitbox.draw(flip, True)
    hitbox.draw(flip,True)
    for i in ListaPlataformas:
        i.loop()
    if(not morto):
        char.draw(flip)
        char.update()
        janela.update()