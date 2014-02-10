import time

from pyglet.gl import *
from ctypes import *
from pyglet import *

key = pyglet.window.key

class ElloWindow(pyglet.window.Window):
	def __init__(self):
		super(ElloWindow, self).__init__()
		self.double_buffer=True #allows for self.flip
		#self.vsync=True #prevents tearing
		self.label = pyglet.text.Label('Ello World!')
		self.push_handlers(self.on_key_press)
		self.x=30.0
		self.y=35.0
	def on_draw(self):
		self.clear()
		self.label.draw()
		pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v3f', (self.x-50, self.y, 0.0, self.x, self.y, 0.0, self.x, self.y+50, 0.0)), ('c3B', (255,0,0,0,0,255,0,255,0)))
	def on_key_press(self, symbol, modifiers):
		if symbol == key.W:
			self.y=self.y+10
		if symbol == key.S:
			self.y=self.y-10
		if symbol == key.D:
			self.x=self.x+10
		if symbol == key.A:
			self.x=self.x-10

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
	window = ElloWindow()
	#start_game()
	pyglet.app.run()

time.sleep(0)