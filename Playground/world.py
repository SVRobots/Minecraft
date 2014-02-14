from os import listdir, mkdir
import cPickle

class World(object):
	#initialize
	def __init__(self):
		super(World, self).__init__()
		self.world="Default"
		self.dimension="DIM1"
		self.playername="Default"
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
		#make some bs blocks
		self.shown_blocks={}
		for x in range(-10,10):
			for z in range(-10,10):
				self.shown_blocks[x,-2,z]=NewBL(0,0)
				print 'added',x,z
	#save player
	def savePlayer(self):
		save(self.savedir + 'players\\' + self.player.name, self.player, True)
	#load player
	def loadPlayer(self):
		self.player = load(self.savedir + 'players\\' + self.playername)
	def quit(self):
		self.savePlayer()

def NewBL(m,i):
	b=BL
	b.mod=m
	b.id=i
	return b

class BL(object):
	def __init__(self):
		self.mod=0
		self.id=0

class Player(object):
	def __init__(self):
		self.name='Default'
		self.x=0
		self.y=0
		self.z=0
		self.r=0
		self.p=0

def InitializeWorld(world, dimension):
	w=World()
	w.world = world
	w.dimension = dimension
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