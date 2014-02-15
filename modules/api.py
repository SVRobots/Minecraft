from pyglet.graphics import TextureGroup
from pyglet import image
from pyglet.gl import *

glEnable(GL_CULL_FACE)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
tex = TextureGroup(image.load('modules\\icon.png').get_texture())

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

def NewFBlock(n, w, s, h, tt, tb, tn, ts, te, tw, f, b):
	a = NewBlock()
	a.name = n
	a.strength = s
	a.hardness = h
	a.tool = w
	a.north = tn
	a.south = ts
	a.east = te
	a.west = tw
	a.top = tt
	a.bottom = tb
	a.flammable = f
	a.behavior = b
	return a

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
	glEnable(GL_CULL_FACE)##Rem
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
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