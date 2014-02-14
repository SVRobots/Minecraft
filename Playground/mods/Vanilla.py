from imp import load_source
from pyglet.graphics import TextureGroup
from pyglet import image

blocks=[]
tile_entities=[]
entities=[]
dimensions=[]

def init():
	api = load_source('api', 'api\\api.py')
	stoneT = api.Texture('icon.png')
	stoneF = TextureGroup(image.load('icon.png').get_texture())
	stone = api.NewPBlock("Stone", "Pick", 1, 1, stoneF, False)
	stone2 = api.NewPBlock("Stone", "Pick", 1, 1, stoneT, False)
	blocks.append(stone)
	blocks.append(stone2)
	print 'Initialized'

'''NewPBlock(n, w, s, h, t, f):'''
