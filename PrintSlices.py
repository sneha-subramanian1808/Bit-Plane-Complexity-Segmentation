#Importing needed libraries
import argparse
import numpy
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--infile', type=str, help='path to vessel image (.png)')
opts = parser.parse_args()

#Loading the image
image = Image.open(opts.infile).convert('L')

#Converting the image to an array
array = numpy.array(image)

#Slicing the BitPlane
print('Slicing...')
bitPlaneArr  = numpy.zeros( (array.shape[0], array.shape[1], 8), dtype = 'uint8' )
bitPlaneArr[:,:,0] = numpy.copy(array)
for i in range(bitPlaneArr.shape[0]):
    for j in range(bitPlaneArr.shape[1]):
        bitArr = numpy.unpackbits(numpy.uint8(bitPlaneArr[i,j,0]))
        for k in range(8):
            bitPlaneArr[i,j,k] =  bitArr[k]
print('Sliced.')

#Printing all the BitPlanes by creating a copy of BitMatrix and making each plane copy a 8 bit image
print('Displaying all bitplanes in order of most to least signifigant')
tmparr = numpy.copy(bitPlaneArr)
for k in range(8):
    for j in range(tmparr.shape[0]):
        for i in range(tmparr.shape[1]):
            if tmparr[j,i,k] == 1:
                tmparr[j,i,k] = 255

    printImage = Image.fromarray(tmparr[:,:,k],mode="L")
    printImage.show()
