#Test Message
#Import  library
from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.shaders import lit_with_shadows_shader
#load window
app = Ursina()

#Entity
map = Entity(model = 'maze.blend'
,texture = "Barski_text"
, scale = 2
, collider = 'mesh'
, shader = lit_with_shadows_shader) #Set model

amogus = Entity(model = "amogus.blend"
,texture = "Barski_text", scale = 1,collider = 'mesh', shader = lit_with_shadows_shader
, rotation =(12,12,12))
base = Entity(model = "base.blend"
, texture = "water.png", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader)
baldski = Entity(model = "baldski.blend"
, texture = "Barski_text.png", scale = 30,collider = 'mesh', shader = lit_with_shadows_shader)
baldski.position=Vec3(0,0,0)
#Environment
sky_texture = load_texture('Barski_text')
sky = Sky()
#movement
player = FirstPersonController(model = 'player',speed=30)

# def update(): #Fix freefall
#     if player.y < -1:
#         player.position = Vec3(0,0,0)
player.position=Vec3(0,3,0)

#Rotation
def rotation():
    amogus.rotation_y += 999 * time.dt
    amogus.position += amogus.forward * time.dt

#run window
app.run()
