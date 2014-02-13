from pyglet import *
from pyglet.gl import *
from pyglet.graphics import *

import math

window = pyglet.window.Window()



def set_3d():
	""" Configure OpenGL to draw in 3d.
		"""
	width, height = window.get_size()
	glEnable(GL_DEPTH_TEST)
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(65.0, width / float(height), 0.1, 60.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def cube_vertices(x, y, z, n):
	""" Return the vertices of the cube at position x, y, z with size 2*n.
	"""
	return [
		x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
		x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
		x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
		x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
		x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
		x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
	]

def tex_coord(x, y, n=4):
	""" Return the bounding vertices of the texture square.
	"""
	m = 1.0 / n
	dx = x * m
	dy = y * m
	return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

def tex_coords(top, bottom, side):
	""" Return a list of the texture squares for the top, bottom and side.
	"""
	top = tex_coord(*top)
	bottom = tex_coord(*bottom)
	side = tex_coord(*side)
	result = []
	result.extend(top)
	result.extend(bottom)
	result.extend(side * 4)
	return result

def draw(dt):
	""" Called by pyglet to draw the canvas.
		"""
	set_3d()
	window.clear()
	lis.draw()

def block(q,w,e):
	print q,w,e
	vertex_data = cube_vertices(q, w, -e, 0.5)
	lis.add(24, GL_QUADS, group,('v3f/static', vertex_data), ('t2f/static', rex)) #,('t2b/static', textr)

group = TextureGroup(image.load('texture.png').get_texture())
lis = pyglet.graphics.Batch()
rex = list(tex_coords((2, 0), (2, 0), (2, 0)))

block(0,-2,5)
block(-1,-1,5)
block(1,-1,5)
block(0,-1,5)
block(0,0,5)
block(-1,0,5)
block(1,0,5)
block(-2,0,5)
block(2,0,5)
block(0,1,5)
block(-1,1,5)
block(1,1,5)
block(-2,1,5)
block(2,1,5)
block(-1,2,5)
block(1,2,5)

glEnable(GL_CULL_FACE)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

pyglet.clock.schedule_interval(draw, 1.0/60)

pyglet.app.run()