import numpy as np
from PIL import Image

class img:
	def __init__(self, path):
		'''
		Open an image and store the matrix
		'''
		self.matrix = np.array(Image.open(path))

	def mean(self):
		'''
		Return the mean pixel of all the pixels of the matrix
		'''
		(r, v, b) = (0, 0, 0)
		for x in range(len(self.matrix)):
			for y in range(len(self.matrix[0])):
				r += self.matrix[x][y][0]
				v += self.matrix[x][y][1]
				b += self.matrix[x][y][2]

		r /= len(self.matrix)*len(self.matrix[0])
		v /= len(self.matrix)*len(self.matrix[0])
		b /= len(self.matrix)*len(self.matrix[0])

		return (r, v, b)

	def getMatrix(self):
		return self.matrix

	def print(self):
		for x in range(len(self.matrix)):
			print()
			for y in range(len(self.matrix[0])):
				print(self.matrix[x][y], end =" ")
		print()

	def save(self, name):
		im = Image.fromarray(self.matrix)
		im.save(name + ".jpg")

	def computeDistance(self, val):
		'''
		Should return the distance between val et the mean of the image
		'''
		(r, v, b) = val

		#### TODO ####

		return 

	def getSubQuares(self, n):
		'''
		Should return subsquared of size n*n as a liste of img objects
		'''

		#### TODO ####

		return

def constructDataBase(path):
	'''
	Open all the files from the path and return a list of all the resulting subsquares
	'''

	#### TODO ####

	return 

def sortImages(images):
	'''
	For every image in images, find the closest point of the dicretized space and save the image in the directory with the name of this point
	'''

	#### TODO ####

	return

def discretizeSpace(n):
	'''
	Return n^3 points equaly distributed in the pixel space (0, 0, 0) -> (255, 255, 255)
	'''

	points = []

	for r in range(n):
		for v in range(n):
			for b in range(n):
				points.append((r*255//n + 255//(2*n), v*255//n + 255//(2*n), b*255//n + 255//(2*n)))

	return points


def main():
	'''
	Do the job if all the functions are working correctly
	'''
	data = constructDataBase("Data")
	sortImages(data)
