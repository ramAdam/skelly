from pyglet.window import Window
from pyglet.sprite import Sprite
import pyglet
from utils import Segment, Vector

window = Window(800, 600)
# bone_img = pyglet.image.load("bone.png")
# bone_img.anchor_x = bone_img.width 
# bone_img.anchor_y = bone_img.height 
# boneX, boneY = window.width/2, window.height/2
# bone = Sprite(bone_img, x=200, y=200)

# bone.image.anchor_x = bone.image.width / 2
# bone.image.anchor_y = bone.image.height / 2
# bone.rotation = 90
batch = pyglet.graphics.Batch()
childSegment = Segment(Vector(200, 200), 100, 45, batch=batch)
segment = Segment(Vector(300, 300), 200, 35, child =None, batch=batch)
childSegment.a.x = segment.b.x
childSegment.a.y = segment.b.y

assert childSegment.a.y == segment.b.y
childSegment._initBatch(batch)


def update(dt):
    # global rot
    # if rot == 180:
    #     rot = 0
    # else:
    #     rot += 1
    # bone.rotation = rot
	 pass
    

@window.event
def on_draw():
    window.clear()
    batch.draw()


if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()
