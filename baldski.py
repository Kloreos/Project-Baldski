#Import  library
from ursina import *
from ursina import collider
from ursina import vec3
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.first_person_controller import camera
from ursina.shaders import lit_with_shadows_shader
from ursina import curve

import time
#load window
app = Ursina()
window.fullscreen = False

#Environment


#Baldski texture
BTexture = "Baldski_dlc/Barski_text"
WallB = "Baldski_dlc/WallTexture.jpg"
#Entity
map = Entity(model = 'maze.blend'
,texture = BTexture
, scale = 2
, collider = 'mesh'
, shader = lit_with_shadows_shader) #Set model

#Walls
wall = Entity(model = "cube"
, position = Vec3(1.39086, 0.752942, 23.2763)
, scale = (80,70,1)
, collider = "mesh"
, texture = WallB)
wall2 = Entity(model = "cube"
, position = Vec3(22.7444, 0.752942, 3.30865)
, scale = (80,70,1)
, collider = "mesh"
, rotation_y = 90
, texture = WallB)
wall3 = Entity(model = "cube"
, position = Vec3(-1.09923, 0, -21.8463)
, scale = (80,70,1)
, collider = "mesh"
, texture = WallB)
wall4 = Entity(model = "cube"
, position = Vec3(-22.9727, 0, 3.39197)
, scale = (80,70,1)
, collider = "mesh"
, rotation_y = 90
, texture = WallB)
wall5 = Entity(model = "cube"
, position = Vec3(2.38985, 30, -0.799802)
, scale = (80,70,1)
, collider = "mesh"
, rotation_x =90     
, texture =WallB)
#Wall fix
fix1 = duplicate(wall,Vec3(1.38086, 0.752942, 23.2663) )
fix2 = duplicate(wall,Vec3(22.7399, 0.752942, 3.2999) )
fix3 = duplicate(wall,Vec3(-1, 0, -21.79999) )
fix4 = duplicate(wall,Vec3(-22.89999, 0, 3.2999))
#player
player = FirstPersonController(model = 'player',speed=30,y = 10)
player.jump_height = 6
player.gravity = 1
player.position = Vec3(2.24184, 0, 15.8104)

#GUI    

show_text = True
text1 = ""
Quest_text = Text(text = text1,origin =Vec2(x = 2.25, y = -18))

def quest():
    global text1
    global Quest_text
    if held_keys["tab"]:
        Quest_text.text = "Quest: Find baldski hair"
    elif not held_keys["tab"]:
        Quest_text.text = ""

#Start Menu

def start_menu():
    player.disable()
    global menu
    global Play_button
    menu = Entity(model = "quad",
     texture = "Game_menu.png",
     position = Vec2(.3,-.1),parent=camera.ui,
     scale=(2.4,1.2))
    Play_button=Button(text="Play",text_color=color.white,scale=(.80,.20),origin=(0,1),on_click=returnPLayer)
def returnPLayer(): 
    player.enable()
    menu.disable()
    Play_button.disable()
start_menu()
#Sound Effects
amogus_audio = Audio("amogus.mp3",loop = False, autoplay = False)

def walksound():
    if held_keys["a"] or held_keys["d"] or held_keys["w"] or held_keys["s"]:
        amogus_audio.play()


# other entities
amogus = Entity(model = "amogus.blend"
,texture =BTexture, scale = 4,collider = 'mesh', shader = lit_with_shadows_shader)

amogus.position = Vec3(2,5,0)
amogus.add_script(SmoothFollow(target = player, offset =[-2,4,0], speed = 2.5))

#Base
base = Entity(model = "base.blend"
, texture = "water.png", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader)
baldski = Entity(model = "baldski.blend"
, texture = BTexture, scale = 1, shader = lit_with_shadows_shader)
baldski.position = (2,5,0)

#Weapon
basic_gun = "source/Pistol.fbx"
baldski_face = "baldski.blend"
weapon = Entity(parent = camera,model = basic_gun, scale = 0.05
,position = Vec3(2,-2,-0.5), rotation = Vec3(2,0,8), texture = "textures/PistolTexture.png")

weapon2 = Entity(model = basic_gun, scale = 0.05
,position = Vec3(2,5,0), rotation = Vec3(2,0,8), texture = "textures/PistolTexture.png")

bang = Audio("bang.mp3",loop = False, autoplay = False )

def action():
    bang.play()
Entity(model='square', parent=camera.ui, scale=.1, collider='box', on_click=action)


#Weapon animations

#Load DlC
DLC_load = False
def DLC():
    if DLC_load == True:
        BTexture = "Dam_dlc/dam1.jpg"
        WallB = "Dam_dlc/dam2.jpg"
    else: 
        Btexture ="Baldski_dlc/Barski_text"
        WallB = "Baldski_dlc/WallTexture.jpg"

#Environment
sky = Sky(texture = BTexture)
#Fix player
# start_menu()
def update(): #upate function
    print(player.position)
    # if player.y < -1: 
    #     player.position = Vec3(0,3,0)
    quest()
    DLC()
    if held_keys["2"]:
        weapon.model = baldski_face
        weapon.texture = BTexture
        weapon.position = Vec3(2,-0.25,2.5)
        weapon.rotation= Vec3(0,90,0)
        weapon.scale = 0.25
        amogus_audio.play()

    elif held_keys["1"]:
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = Vec3(-0.5,-2,-1)
        weapon.rotation =Vec3(0,0,0)
        weapon.scale = 0.05


    elif held_keys["q"]:
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = Vec3(-0.5,-2,-1)
        weapon.rotation =Vec3(0,0,0)
        weapon.scale =  0.05

    elif held_keys["e"]:
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position =Vec3(2,-2,-0.5)
        weapon.rotation =Vec3(2,0,8)
        weapon.scale =  0.05

    elif held_keys["p"]:
        player.position = Vec3(0,40,0)

    elif held_keys["o"]:
        player.position = Vec3(0,0,0)

 #run window
app.run()
