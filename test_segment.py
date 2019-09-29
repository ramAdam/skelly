from unittest import TestCase
from utils import Segment, Vector
import unittest
import pyglet

class TestSegment(TestCase):
    def setUp(self):
        self.a = Vector(50, 50)
        self.s = Segment(self.a, 100, 0, batch=None)

    def test_segment_with_angle_zero(self):
        assert self.s.a.x == 50
        assert self.s.b.x == 150
        assert self.s.b.y == self.s.a.y

    


if __name__ == "__main__":
    unittest.main()    