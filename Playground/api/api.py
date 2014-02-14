from pyglet.graphics import TextureGroup
from pyglet import image

tex = TextureGroup(image.load('icon.png').get_texture())

class NewBlock(object):
	def __init__(self):
		self.name= "Unnamed Block"
		self.strength = 1
		self.hardness = 1
		self.flammable = False
		self.north = tex
		self.south = tex
		self.east = tex
		self.west = tex
		self.top = tex
		self.bottom = tex
		self.behavior = False
		self.tool = None

def NewPBlock(n, w, s, h, t, f):
	b = NewBlock()
	b.name = n
	b.strength = s
	b.hardness = h
	b.tool = w
	b.north = t
	b.south = t
	b.east = t
	b.west = t
	b.top = t
	b.bottom = t
	b.flammable = f
	return b

def Texture(f):
	return TextureGroup(image.load(f).get_texture())

def NewBL(m,i):
	b=BL
	b.mod=m
	b.id=i
	print b.id
	return b

class BL(object):
	def __init__(self):
		self.mod=0
		self.id=0