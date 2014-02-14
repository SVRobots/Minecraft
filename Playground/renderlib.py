from pyglet.gl import *

def RenderMode3D(window):
	width, height = window.get_size()
	glEnable(GL_DEPTH_TEST)
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(65.0, width / float(height), 0.1, 60.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def Generate3DRender(blocklist, c):
	r=pyglet.graphics.Batch()
	for pos in blocklist:
		x,y,z=pos
		#north
		#r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].north,('v3f/static', (x-0.5,y-0.5,z-0.5, x+0.5,y-0.5,z-0.5, x+0.5,y+0.5,z-0.5, x-0.5,y+0.5,z-0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
		#south
		#r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].south,('v3f/static', (x+0.5,y-0.5,z+0.5, x-0.5,y-0.5,z+0.5, x-0.5,y+0.5,z+0.5, x+0.5,y+0.5,z+0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
		#top
		r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].top,('v3f/static', (x-0.5,y+0.5,z-0.5, x-0.5,y+0.5,z+0.5, x+0.5,y+0.5,z+0.5, x+0.5,y+0.5,z-0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
	return r
	#add(4, GL_QUADS, self.c.blocks[0][0].north,('v3f/static', (x-0.5,y-0.5,z, x+0.5,y-0.5,z, x+0.5,y+0.5,z, x-0.5,y+0.5,z)), ('t2f/static', (0,0,1,0,1,1,0,1)))