from ursina import *
from ursina.prefabs.first_person_controller import *
app = Ursina()

window.exit_button.enabled = True
window.fps_counter.enabled = True
window.cog_button.enabled = False
window.fullscreen = True
#Game's settings



maze = Entity(model = 'maze',texture='Texture', scale = 20, collider = 'mesh') #Set model




#dev settings
player = FirstPersonController(x = 12.6267, y = 0, z = -18.4179)
player.jumping = False
def update():
    if player.y < 0:
        player.position = Vec3(12.6267, 0, -18.4179)

update()

app.run()