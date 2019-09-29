from math import cos, sin, radians
import pyglet

class Vector:
  def __init__(self, x, y):
    self.x =int(x)
    self.y = int(y)

  def sub(self, b):
    return Vector(self.x - b.x, self.y - b.y)


class Segment:
    def __init__(self,
                 a, length,
                 angle, child=None,
                 batch=None,
                 format='v2i'):
        self.a = a
        self.length = length
        self.angle = angle
        self.child = child
        self._calculateB()
        self.format = format
        self.points = (self.a.x, self.a.y, self.b.x, self.b.y)
        if batch:
          self._initBatch(batch)

    def _calculateB(self):
        dx = self.length * cos(radians(self.angle))
        dy = self.length * sin(radians(self.angle))
        self.b = Vector(int(self.a.x + dx), int(self.a.y + dy))
        if self.child:
          self.child.a = self.b
          self.child._calculateB()

    def _initBatch(self, batch):
      pyglet.gl.glLineWidth(1)
      batch.add(2, pyglet.gl.GL_LINES, None, (self.format, self.points)
      ,('c3B', (0, 0, 255, 0, 0, 255)))
      pyglet.gl.glPointSize(5)
      batch.add(2, pyglet.gl.GL_POINTS, None, (self.format, self.points),
      ('c3B', (0, 255, 0, 0, 255, 0))
      )
        