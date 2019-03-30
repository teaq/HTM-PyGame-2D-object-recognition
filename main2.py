import pygame as pg
import numpy as np
import os 
import random


win = pg.display.set_mode((950,950))
pg.display.set_caption("2D object recognition HTM")

wordcategory = ['grass','gold','water','fire','emptyspace','diamond']

def map_generator():
	i = 0
	j = 0
	seed = []
	while i < 20:
		seed.append([random.uniform(0,1) for _ in range(20)])
		i = i + 1
	i = 0
	map = []
	bucket = []
	for i in range(0,20):
		for j in range(0,20):
			if seed[i][j] < 0.60:
				bucket.append("emptyspace")
			elif ((seed[i][j] < 0.70) & (seed[i][j] > 0.60)):
				bucket.append("grass")
			elif (seed[i][j] < 0.80) & (seed[i][j] > 0.70):
				bucket.append("water")
			elif (seed[i][j] < 0.90) & (seed[i][j] > 0.80):
				bucket.append("fire")
			elif (seed[i][j] < 0.95) & (seed[i][j] > 0.90):
				bucket.append("gold")
			elif (seed[i][j] < 1) & (seed[i][j] > 0.95):
				bucket.append("diamond")
		map.append(bucket)
		bucket = []
	return map



x = 50
y = 50
width = 40
height = 60
vel = 5

map = map_generator()
print(map)

run = True
while run:
	pg.time.delay(100)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		win.fill((0,0,0))

#	win.blit(emptyspace, (100,100))
	for i in range(0,20):
		for j in range(0,20):
			win.blit(pg.image.load('data/'+map[i][j]+'.jpg'), (j*45,i*45))
	pg.display.update()

pg.quit()
