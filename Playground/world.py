from os import listdir, mkdir
import cPickle
from imp import load_source
api = load_source('api', 'api\\api.py')
from api import *

class World(object):
	#initialize
	def __init__(self):
		super(World, self).__init__()
		self.world="Default"
		self.dimension="DIM1"
		self.playername="Default"
		self.world_blocks={}
		self.shown_blocks={}
	#load world
	def load(self):
		#set world folder location
		self.savedir = 'saves\\' + self.world + '\\'
		#init saves folder
		if FileExists('', 'saves') == False:
			mkdir('saves')
		#init world folder
		if FileExists('saves', self.world) == False:
			mkdir('saves\\' + self.world)
		#init dimension folder
		if FileExists('saves\\' + self.world, self.dimension) == False:
			mkdir('saves\\' + self.world + '\\' + self.dimension)
		#init players folder
		if FileExists(self.savedir, 'players') == False:
			mkdir(self.savedir + 'players')
		#init player
		if FileExists(self.savedir + 'players\\', self.playername) == False:
			self.player = Player()
		else:
			self.loadPlayer()
		#make some blocks
		self.GenerateWorld(-10,-10,10,10)
		self.ParseVisible()
	#Generate World
	def GenerateWorld(self, lx, lz, ux, uz):
		i=0
		for m in self.c.dimensions:
			if self.dimension in m:
				tmp = self.c.mods[i].GenerateDimension(self.dimension, lx, lz, ux, uz)
				for b in tmp:
					self.world_blocks[b] = tmp[b]
	#find visible blocks to render
	def ParseVisible(self):
		for b in self.world_blocks:
			x,y,z = b
			if ((x,y+1,z) not in self.world_blocks) or ((x,y-1,z) not in self.world_blocks) or ((x+1,y,z) not in self.world_blocks) or ((x-1,y,z) not in self.world_blocks) or ((x,y,z+1) not in self.world_blocks) or ((x,y,z-1) not in self.world_blocks):
				self.shown_blocks[b]=self.world_blocks[b]
	#save player
	def savePlayer(self):
		save(self.savedir + 'players\\' + self.player.name, self.player, True)
	#load player
	def loadPlayer(self):
		self.player = load(self.savedir + 'players\\' + self.playername)
	def quit(self):
		self.savePlayer()

class Player(object):
	def __init__(self):
		self.name='Default'
		self.x=0
		self.y=0
		self.z=0
		self.r=0
		self.p=0

def InitializeWorld(world, dimension, c):
	w=World()
	w.world = world
	w.dimension = dimension
	w.c = c
	w.load()
	return w

def save(f,o,r):
	if r == True:
		a = open(f,'wb')
	else:
		a = open(f,'r+b')
	print f
	cPickle.dump(o, a, -1)
	a.close()

def load(f):
	a = open(f, 'rb')
	o = cPickle.load(a)
	a.close()
	return o

def FileExists(direct, f):
	for p in listdir(direct):
		if p == f:
			return True
	return False