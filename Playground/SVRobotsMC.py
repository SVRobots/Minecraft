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
		self.block_render=Generate3DRender(self.world.shown_blocks, c)
		self.mouse_exclusive=True
	def on_draw(self):
		RenderMode3D(self)
		self.clear()
		#move to player location
		glRotatef(self.world.player.r,0,1,0)
		glRotatef(self.world.player.p,math.cos(math.radians(self.world.player.r)),0,math.sin(math.radians(self.world.player.r)))
		glTranslatef(self.world.player.x,-(self.world.player.y+1.8),self.world.player.z)
		#draw everything
		self.block_render.draw()
		self.
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
		#player movement motion
		dx = 0
		dz = 0
		dy = 0
		if keys[key.W]:
			dx-=math.sin(math.radians(self.world.player.r))
			dz+=math.cos(math.radians(self.world.player.r))
		if keys[key.S]:
			dx+=math.sin(math.radians(self.world.player.r))
			dz-=math.cos(math.radians(self.world.player.r))
		if keys[key.A]:
			dx+=math.cos(math.radians(self.world.player.r))
			dz+=math.sin(math.radians(self.world.player.r))
		if keys[key.D]:
			dx-=math.cos(math.radians(self.world.player.r))
			dz-=math.sin(math.radians(self.world.player.r))
		dx = dx*4.3*dt
		dz = dz*4.3*dt
		#block contact (side)
		if (dx != 0) or (dz != 0):
			if dx == 0:
				dx=0.01
			l = math.sqrt(pow(dx,2)+pow(dz,2))
			t = math.atan(dz/dx)
			while (round(self.world.player.x+dx), round(self.world.player.y+.5), round(self.world.player.z+dz)) in self.world.world_blocks:
				l-=0.05
				dx = l*math.cos(t)
				dz = l*math.sin(t)
			while (round(self.world.player.x+dx), round(self.world.player.y+1.5), round(self.world.player.z+dz)) in self.world.world_blocks:
				l-=0.05
				dx = l*math.cos(t)
				dz = l*math.sin(t)
			self.world.player.x+=dx
			self.world.player.z+=dz
		#creative motion (flying)
		if self.world.player.flying==True:
			if keys[key.SPACE]:
				dy+=3*dt
			if keys[key.Z]:
				dy-=3*dt
		#player on ground
		if (round(self.world.player.x),round(self.world.player.y-0.1),round(self.world.player.z)) in self.world.world_blocks and self.world.player.vy <= 0:
			self.world.player.onGround=True#ADD DAMAGE
			self.fallDistance=0
			self.world.player.vy=0
			if key.SPACE not in keys or self.world.player.flying == False:
				self.world.player.y=round(self.world.player.y-0.1)
		else:
			self.world.player.onGround=False
		#jump
		if keys[key.SPACE] and self.world.player.flying == False and self.world.player.onGround == True:
			self.world.player.vy = math.sqrt(((1.25)*math.pow(self.world.a,2))/(self.world.a/2))
			self.world.player.onGround == False
			dy=0.1
		#gamemode
		if keys[key.G]:
			self.world.player.flying=False
			self.world.player.gameMode=0
		if keys[key.H]:
			self.world.player.gameMode=1
			self.world.player.flying=True
		#gravity
		if self.world.player.onGround == False and self.world.player.flying == False:
			dy = (self.world.player.vy*dt)+((self.world.a/2)*math.pow(dt,2))
			self.world.player.fallDistance -= dy
			self.world.player.vy -= self.world.a*dt
			self.world.player.y += dy
		print self.world.player.x
		#player hits head
		if self.world.player.onGround == True and dy < 0:
			dy=0
		if (round(self.world.player.x),round(self.world.player.y+2.1),round(self.world.player.z)) in self.world.world_blocks and self.world.player.onGround==False:
			dy = 0
			self.world.player.vy = 0
		self.world.player.y+=dy
		print self.world.player.onGround

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