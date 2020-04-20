from PIL import Image
import numpy

im = Image.open('images/MapofVideos.jpg') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
# print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
width, height = im.size
pixel_values = list(im.getdata())

f = open("out.txt","w+")

# pix=im.load()
w=im.size[0]
h=im.size[1]
for i in range(0, w, 10):
  for j in range(0, h, 10):
  	# if(pix[i,j][1] > 100):
  	# print(str(i) + ", " + str(j) + ": " + str(pix[i,j]))
  	f.write(str(i) + ", " + str(j) + ": " + str(pix[i,j]) + "\n")
    # print(pix[i,j])
# pixel_values = numpy.array(pixel_values).reshape((width, height, 3))
# print(pixel_values)
f.close() 

# def get_image(image_path):
#     """Get a numpy array of an image so that one can access values[x][y]."""
#     image = Image.open(image_path, 'r')
#     width, height = image.size
#     pixel_values = list(image.getdata())
#     if image.mode == 'RGB':
#         channels = 3
#     elif image.mode == 'L':
#         channels = 1
#     else:
#         print("Unknown mode: %s" % image.mode)
#         return None
#     pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
#     return pixel_values