#Import  library
from ursina import *
from ursina import collider
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.first_person_controller import camera
from ursina.shaders import lit_with_shadows_shader
from ursina import curve

import time
#load window
app = Ursina()

#Entity
map = Entity(model = 'maze.blend'
,texture = "Barski_text"
, scale = 2
, collider = 'mesh'
, shader = lit_with_shadows_shader) #Set model

#Walls
wall = Entity(model = "cube"
, position = Vec3(1.39086, 0.752942, 23.2763)
, scale = (80,70,1)
, collider = "mesh"
, texture = "Barski_text")
wall2 = Entity(model = "cube"
, position = Vec3(22.7444, 0.752942, 3.30865)
, scale = (80,70,1)
, collider = "mesh"
, rotation_y = 90
, texture = "Barski_text")
wall3 = Entity(model = "cube"
, position = Vec3(-1.09923, 0, -21.8463)
, scale = (80,70,1)
, collider = "mesh"
, texture = "Barski_text")
wall4 = Entity(model = "cube"
, position = Vec3(-22.9727, 0, 3.39197)
, scale = (80,70,1)
, collider = "mesh"
, rotation_y = 90
, texture = "Barski_text")
# other entities
amogus = Entity(model = "amogus.blend"
,texture = "Barski_text", scale = 10,collider = 'mesh', shader = lit_with_shadows_shader)

amogus.position = Vec3(2,6,0)

base = Entity(model = "base.blend"
, texture = "water.png", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader)
baldski = Entity(model = "baldski.blend"
, texture = "Barski_text.png", scale = 1, shader = lit_with_shadows_shader)
baldski.position = (2,5,0)

#gun 
gun = Entity(parent = camera,model = "source/Gun low poly.fbx", scale = 0.25
,position = Vec3(2,-0.25,2.5), rotation = Vec3(0,90,0), texture = "textures/Gun_low_poly_gun_AlbedoTransparency.png")

# gun = Entity(model="source/Gun low poly.fbx"
# ,  texture = "Barski_text.png", scale = 0.5, shader = lit_with_shadows_shader)
# position = Vec3(2,5,0)

#Environment
sky_texture = load_texture('Barski_text')
sky = Sky()
#movement
player = FirstPersonController(model = 'player',speed=30)
baldski_pos = player.position + (3,3,0) 
def update(): #Fix freefall
    print(player.position)
    # if player.y < -1: 
    # player.position = Vec3(0,3,0)



#run window
app.run()
