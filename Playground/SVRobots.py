import time

from pyglet.gl import *
from ctypes import *
from pyglet import *

key = pyglet.window.key

objects=[]
objectTypes=[]

class ElloWindow(pyglet.window.Window):
	def __init__(self):
		super(ElloWindow, self).__init__()
		self.double_buffer=True #allows for self.flip
		#self.vsync=True #prevents tearing
		self.label = pyglet.text.Label('Ello World!')
		self.push_handlers(self.on_key_press)
		self.tri=triangle()
		self.controlindex=len(objects[0])-1
	def on_draw(self):
		self.clear()
		i=0
		for c in objects[0]:
			if i & 0x1 == 0:
				label = pyglet.text.Label(str((i/2)+1), font_name='Times New Roman', font_size=13, x=c.x, y=c.y, anchor_x='right', anchor_y='bottom', color=(0,0,0,255))
				label.draw()
				if i==self.controlindex:
					pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v3f', (c.x-50, c.y, 0.0, c.x, c.y, 0.0, c.x, c.y+50, 0.0)), ('c3B', (255,0,0,0,0,255,0,255,0)))
				else:
					pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v3f', (c.x-50, c.y, 0.0, c.x, c.y, 0.0, c.x, c.y+50, 0.0)), ('c3B', (255,255,255,255,255,255,255,255,255)))
				label.draw()
			i=i+1
	def on_key_press(self, symbol, modifier):
		if symbol == key.W:
			objects[0][self.controlindex].y=objects[0][self.controlindex].y+10
		if symbol == key.S:
			objects[0][self.controlindex].y=objects[0][self.controlindex].y-10
		if symbol == key.D:
			objects[0][self.controlindex].x=objects[0][self.controlindex].x+10
		if symbol == key.A:
			objects[0][self.controlindex].x=objects[0][self.controlindex].x-10
		if symbol == key.ENTER:
			self.tri = triangle()
			self.controlindex=len(objects[0])-1
		if symbol == key.UP:
			if self.controlindex < len(objects[0])-1:
				self.controlindex=self.controlindex+1
		if symbol == key.DOWN:
			if self.controlindex != 0:
				self.controlindex=self.controlindex-1

class triangle(object):
	ID=0 #make class get this from config
	def __init__(self):
		super(triangle, self)
		objects[self.ID].append(self)
		self.name='Triangle'
		self.x=100
		self.y=100

def newEntity(ID,NAME):
	objects.append([])
	objectTypes.append([])
	objectTypes[len(objectTypes)-1].append(NAME)

def declare_entities():
	newEntity(0,'Triangle')

if __name__ == '__main__':
	#Declare Entities
	declare_entities()
	window = ElloWindow()
	#start_game()
	pyglet.app.run()

time.sleep(0)