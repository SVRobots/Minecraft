import time

from pyglet.gl import *
from ctypes import *
from pyglet import *
from imp import load_source, find_module
from os import listdir
from renderlib import *
from world import *

key = pyglet.window.key

class MainWindow(pyglet.window.Window):
	def __init__(self):
		super(MainWindow, self).__init__()
		#Setup window
		self.set_icon(pyglet.image.load('icon.png'))
		self.set_caption('Minecraft+')
		#Setup gl
		glEnable(GL_CULL_FACE)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

		#init world
		world=InitializeWorld("Default","DIM1")

		self.label = pyglet.text.Label('Minecraft: Take 1')
	def on_draw(self):
		self.clear()
		self.label.draw()

def ImportMods(): #add exception for when no mods exist
	modlist = listdir('mods')
	for mod in modlist:
		if mod[-3:len(mod)] == '.py':
			mods.append(load_source(mod[0:-3], '''mods\\'''+mod))
	for mod in mods:
		mod.mod()

if __name__ == '__main__':
	window = MainWindow()
	pyglet.app.run()

time.sleep(0)