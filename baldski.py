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

#--------------------quick dev
#music off:


#Baldski texture
BTexture = "Baldski_dlc/Barski_text"
WallB = "Baldski_dlc/Barski_text"


#Load DlC
DLC_load = True
def DLC():
    global BTexture
    global WallB
    if DLC_load == True:
        BTexture = "Dam_dlc/dam1.jpg"
        WallB = "Dam_dlc/dam2.jpg"
    else: 
        global Btexture
        Btexture ="Baldski_dlc/Barski_text"
        WallB = "Baldski_dlc/WallTexture.jpg"

#---------Environment------------


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
# wall5 = Entity(model = "cube" 
# , position = Vec3(2.38985, 30, -0.799802)
# , scale = (80,70,1)
# , collider = "mesh"
# , rotation_x =90     
# , texture =WallB)
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

#Add levels
level1 = ["map/amogus.blend","map/obstacle.blend""map/amogus.blend"]


#GUI    
def gameplayGui(): 
    start_button = Button(text="Start",text_color= color.white,scale=(.80,.20), origin=(0,1))
    start_button.disable()

gameplayGui()

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
b1 = "Sounds/start_menu.mp3"
menu_image = "images/temp_menu.jpg"
baldski_audio = Audio(b1, autoplay=False,loop=True)
def play_bald():
    baldski_audio.play()
def start_menu():
    player.disable()
    global menu
    global Play_button
    play_bald()
    menu = Entity(model = "quad",
     texture = menu_image,
     position = Vec2(.3,-.1),parent=camera.ui,
     scale=(2.4,1.2))
    Play_button=Button(text="Play",text_color=color.white,scale=(.80,.20),origin=(0,1),on_click=returnPlayer)
def returnPlayer(): 
    player.enable()
    menu.disable()
    Play_button.disable()
    baldski_audio.stop()

start = start_menu()
# start_menu()
#Sound Effects
amogus_audio = Audio("amogus.mp3",loop = False, autoplay = False)

def walksound():
    if held_keys["a"] or held_keys["d"] or held_keys["w"] or held_keys["s"]:
        amogus_audio.play()

# music_button = Button(text="" , icon = "Escape_Baldski_data/icon/Music_icon.jpeg", scale=.1)

# other entities
amogus = Entity(model = "amogus.blend"
,texture =BTexture, scale = 4,collider = 'mesh', shader = lit_with_shadows_shader)

amogus.position = Vec3(2,5,0)
amogus.add_script(SmoothFollow(target = player, offset =[0,0,0], speed = 2.5))

#Base
base = Entity(model = "base.blend"
, texture = "water.png", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader)
# baldski = Entity(model = "baldski.blend"
# , texture = BTexture, scale = 1, shader = lit_with_shadows_shader)
# baldski.position = (2,5,0)

#Weapon
basic_gun = "source/Pistol.fbx"
baldski_face = "baldski.blend"
weapon = Entity(parent = camera,model = basic_gun, scale = 0.05
,position = Vec3(2,-2,-0.5), rotation = Vec3(2,0,8), texture = "textures/PistolTexture.png")
bang = Audio("bang.mp3",loop = False, autoplay = False )

Weapon_list = ["pistol_l","pistol_r","Baldski","knives"]
current_weapon = ""

def check_weapon():
    pass

def action():
    bang.play()
fps = Entity(model='square', parent=camera.ui, scale=.1, collider='box', on_click=action)
#left side
position_l = (Vec3(-0.5,-2,-1))
rotation_l = (Vec3(0,0,0))
scale_l = 0.05
listl = [position_l, rotation_l, scale_l]
#right side
position_r = Vec3(2,-2,-0.5)
rotation_r = Vec3(2,0,8)
scale_r = 0.05
listr = [position_r,rotation_r,scale_r]
#Settings
window.fullscreen = True
# window.vsync = False

def fc():
    if window.fullscreen == True:
        window.fullscreen = False
    elif window.fullscreen == False: 
        window.fullscreen = True


def Settings():
    player.disable()
    fps.disable()
    global S1,S2,S3,setting_img, settingClicked
    setting_img = Entity(model = "quad",
     texture = "Settings",
     position = Vec2(.3,-.1),parent=camera.ui,
     scale=(2.4,1.2))
    S1 =Button(text="Fullscreen",text_color=color.white,scale=(.80,.20),origin=(0,1),on_click=fc)
    S3 =Button(text="close setting",text_color=color.white,scale=(.15,.20),origin=(4,-1), on_click = ReturnSettings)

def ReturnSettings():
    fps.enable()
    setting_img.disable()
    S1.disable()
    S3.disable()
    player.enable()

def fixSettings():
    if player.enable() and setting_img.enable():
            fps.enable()
            setting_img.disable()
            S1.disable()
            S3.disable()
    else:
        pass

def click_settings():
    global settingClicked 
    if held_keys["escape"]:
        Settings()
        time.sleep(0.3)
#Weapon animations



#Environment
sky = Sky(texture = BTexture)
#Fix player
# start_menu()
def update(): #update function
    # print(player.position)
    # if player.y < -1: 
    #     player.position = Vec3(0,3,0)

    #-----load functions-----
    # fixSettings()
    click_settings()
    quest()
    DLC()


    #main update
    bru = 0
    if bru == 1:
        pass

    elif held_keys["3"]:
        # weapon.model = baldski_face
        weapon.texture = BTexture
        # weapon.position = Vec3(2,-0.25,2.5)
        # weapon.rotation= Vec3(0,90,0)
        # weapon.scale = 0.25
        amogus_audio.play()

    elif held_keys["1"]:
        fps.enable()
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = listr[0]
        weapon.rotation = listr[1]
        weapon.scale = listr[2]

    elif held_keys["q"]:
        fps.enable()
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = listl[0]
        weapon.rotation = listl[1]
        weapon.scale =  listl[2]

    elif held_keys["e"]:
        fps.enable()
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = listr[0]
        weapon.rotation = listr[1]
        weapon.scale =  listr[2]

    elif held_keys["p"]:
        player.position = player.position + Vec3(0,40,0)
        print("Player teleported upward")

    elif held_keys["o"]:
        player.position = Vec3(0,0,0)
        print("Player returned ")

    

 #run window
app.run()
