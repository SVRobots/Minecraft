import time

from pyglet.gl import *
from ctypes import *
from pyglet import *

key = pyglet.window.key

objects=[]

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
			if i==self.controlindex:
				pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v3f', (c.x-50, c.y, 0.0, c.x, c.y, 0.0, c.x, c.y+50, 0.0)), ('c3B', (255,0,0,0,0,255,0,255,0)))
			else:
				pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v3f', (c.x-50, c.y, 0.0, c.x, c.y, 0.0, c.x, c.y+50, 0.0)), ('c3B', (255,255,255,255,255,255,255,255,255)))
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
	ID=0
	def __init__(self):
		super(triangle, self)
		objects[self.ID].append(self)
		self.name='Triangle'
		self.x=100
		self.y=100

def start_game():
	def on_key_press(symbol, modifiers):
		print 'ingamepress'
		if symbol == pyglet.window.key.ESCAPE:
			end_game()
		return True
	def on_mouse_press(x, y, button, modifiers):
		print 'ingamemouse'
		return True
	window.push_handlers(on_key_press, on_mouse_press)

def end_game():
	window.pop_handlers()

if __name__ == '__main__':
	#Declare Triangles
	objects.append([])
	window = ElloWindow()
	#start_game()
	pyglet.app.run()

time.sleep(0)