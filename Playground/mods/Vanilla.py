from imp import load_source
from pyglet.graphics import TextureGroup
from pyglet import image
api = load_source('api', 'api\\api.py')

blocks=[]
tile_entities=[]
entities=[]
dimensions=[]
dimension_gravity={}

def init(): #Init Function Called Before Import (setup arrays to be imported)
	grass_top = api.Texture('blocks\\grass.png')
	grass_side = api.Texture('blocks\\grass_side.png')
	dirtT = api.Texture('blocks\\dirt.png')
	stone = api.NewPBlock("Stone", "Pick", 1, 1, api.Texture('blocks\\stone.png'), False)
	cobblestone = api.NewPBlock("Cobblestone", "Pick", 1, 1, api.Texture('blocks\\cobblestone.png'), False)
	grass = api.NewFBlock("Grass", "Shovel", 1, 1, grass_top, dirtT, grass_side, grass_side, grass_side, grass_side, False, False)
	blocks.append(stone)
	blocks.append(cobblestone)
	blocks.append(grass)
	dimensions.append("DIM1")
	dimension_gravity["DIM1"]=20
	print 'Initialized Vanilla'

def GenerateDimension(d, lx, lz, ux, uz): #Generate Function Called By Game
	if d == "DIM1":
		return GenerateDIM1(lx,lz,ux,uz)


def GenerateDIM1(lx,lz,ux,uz):
	w = {}
	for x in range(lx,ux):
		for z in range(lz,uz):
			for y in range (-5,2):
				w[x,y,z]=api.BL()
				w[x,y,z].mod=0
				w[x,y,z].id=0
			for y in range (2,6):
				w[x,y,z]=api.BL()
				w[x,y,z].mod=0
				w[x,y,z].id=1
	w[0,6,0]=api.BL()
	w[0,6,0].mod=0
	w[0,6,0].id=2
	return w

'''NewPBlock(n, w, s, h, t, f):'''
