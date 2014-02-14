import time

from pyglet.gl import *
from ctypes import *
from pyglet import *
from imp import load_source
from os import listdir
from renderlib import *
from world import *
from pyglet.graphics import TextureGroup
import math

key = pyglet.window.key
k=0

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
		self.c=ImportMods(NewModData())
		self.world=InitializeWorld("Default","DIM1",c)
		self.render=Generate3DRender(self.world.shown_blocks, c)
		self.mouse_exclusive=True
	def on_draw(self):
		RenderMode3D(self)
		self.clear()
		#move to player location
		glRotatef(self.world.player.r,0,1,0)
		glRotatef(self.world.player.p,math.cos(math.radians(self.world.player.r)),0,math.sin(math.radians(self.world.player.r)))
		glTranslatef(self.world.player.x,self.world.player.y,self.world.player.z)
		#draw everything
		self.render.draw()
	def on_key_press(self, s, m):
		if s == key.ENTER:
			self.world.quit()
		if s == key.ESCAPE:
			if self.mouse_exclusive == True:
				self.mouse_exclusive=False
			else:
				self.mouse_exclusive=True
		if s == key.R:
			self.render=Generate3DRender(self.world.shown_blocks, c)
	def on_mouse_motion(self, x, y, dx, dy):
		if self.mouse_exclusive != False:
			self.world.player.r+=dx/10
			self.world.player.p-=dy/10
			if self.world.player.p > 90:
				self.world.player.p=90
			if self.world.player.p < -90:
				self.world.player.p=-90
			if self.world.player.r > 360:
				self.world.player.r -= 360
			if self.world.player.r < 0:
				self.world.player.r += 360
	def update(self,dt):
		#set mouse lock
		self.set_exclusive_mouse(self.mouse_exclusive)
		#player motion
		if keys[key.W]:
			self.world.player.x-=math.sin(math.radians(self.world.player.r))*5*dt
			self.world.player.z+=math.cos(math.radians(self.world.player.r))*5*dt
		if keys[key.S]:
			self.world.player.x+=math.sin(math.radians(self.world.player.r))*3*dt
			self.world.player.z-=math.cos(math.radians(self.world.player.r))*3*dt
		if keys[key.A]:
			self.world.player.x+=math.cos(math.radians(self.world.player.r))*3*dt
			self.world.player.z+=math.sin(math.radians(self.world.player.r))*3*dt
		if keys[key.D]:
			self.world.player.x-=math.cos(math.radians(self.world.player.r))*3*dt
			self.world.player.z-=math.sin(math.radians(self.world.player.r))*3*dt
		if keys[key.SPACE]:
			self.world.player.y-=3*dt
		if keys[key.Z]:
			self.world.player.y+=3*dt

class NewModData(object):
	def __init__(self):
		super(NewModData, self).__init__()
		self.mods=[]
		self.mod_index=[]
		self.blocks=[]
		self.tile_entities=[]
		self.entities=[]
		self.dimensions=[]

def ImportMods(c): #add exception for when no mods exist
	modlist = listdir('mods')
	for mod in modlist:
		if mod[-3:len(mod)] == '.py':
			c.mods.append(load_source(mod[0:-3], '''mods\\'''+mod))
			c.mod_index.append(mod[0:-3])
			print 'Found mod: ', mod[0:-3]
	for mod in c.mods:
		mod.init()
		blo=[]
		tent=[]
		ent=[]
		for block in mod.blocks:
			blo.append(block)
			print block.name
		for tile_entity in mod.tile_entities:
			tent.append(tile_entity)
		for entity in mod.entities:
			ent.append(entity)
		c.dimensions.append(mod.dimensions)
		c.blocks.append(blo)
		c.tile_entities.append(tent)
		c.entities.append(ent)
	return c

if __name__ == '__main__':
	c = ImportMods(NewModData())
	window = MainWindow()
	pyglet.clock.schedule_interval(window.update, 1.0/60)
	keys = key.KeyStateHandler()
	window.push_handlers(keys)
	pyglet.app.run()

time.sleep(0)