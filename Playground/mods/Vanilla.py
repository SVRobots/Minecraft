from imp import load_source
from pyglet.graphics import TextureGroup
from pyglet import image
api = load_source('api', 'api\\api.py')

blocks=[]
tile_entities=[]
entities=[]
dimensions=[]

def init():
	stone = api.NewPBlock("Stone", "Pick", 1, 1, api.Texture('blocks\\stone.png'), False)
	cobblestone = api.NewPBlock("Cobblestone", "Pick", 1, 1, api.Texture('blocks\\cobblestone.png'), False)
	blocks.append(stone)
	blocks.append(cobblestone)
	dimensions.append("DIM1")
	print 'Initialized'

def GenerateDimension(d, lx, lz, ux, uz):
	w = {}
	for x in range(lx,ux):
		for z in range(lz,uz):
			for y in range (-5,2):
				w[x,y,z]=api.BL()
				w[x,y,z].mod=0
				w[x,y,z].id=0
			for y in range (3,6):
				w[x,y,z]=api.BL()
				w[x,y,z].mod=0
				w[x,y,z].id=1
	print api.BL()
	print w[0,4,0].id
	return w

'''NewPBlock(n, w, s, h, t, f):'''
