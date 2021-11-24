#Import  library
from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.shaders import lit_with_shadows_shader
#load window
app = Ursina()

#main program
map = Entity(model = 'maze.blend'
,texture = "grass_texture"
, scale = 20
, collider = 'mesh'
, shader = lit_with_shadows_shader) #Set model

amogus = Entity(model = "amogus.blend"
,texture = "A_Texture", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader
, rotation =(0,0,0))
base = Entity(model = "base.blend"
, texture = "water.png", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader)
#Environment
sky_texture = load_texture('assets/skybox.png')
sky = Sky()
#movement
player = FirstPersonController(model = 'player')

def update(): #Fix freefall
    if player.y < -1:
        player.position = Vec3(0,0,0)

#Rotation
def rotation():
    amogus.rotation_y += 50 * time.dt
    amogus.position += amogus.forward * time.dt

#run window
app.run()