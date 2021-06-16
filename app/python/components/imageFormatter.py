import base64
import io
from PIL import Image

class ImageFormatter:
    
    def encode_img(self,image):
        imageInfo = str(image.width) + ";" + str(image.height) + ';'
        for row in range(image.width):
            for column in range(image.height):
                imageInfo += str( image.getpixel((row,column) )) + ";"
        return imageInfo

    def decode_img(self,msg):
        image_info = msg.split(';')
        img = Image.new('RGB', (int(image_info[0]), int(image_info[1])), color = 'red')
        pixels = img.load()
        index = 2
        print(image.mode)
        for row in range(int(image_info[0])):
            for column in range(int(image_info[1])):
                
                pixels[row,column] = cleanSegment(image_info[index])
                index += 1

        return img

    def __cleanSegment(self,segment):
	    segment = segment.replace("(","").replace(")","").replace(" ","")
	    if "#" or "A" or "B" or "C" or "D" or "E" or "F" in segment:
		    return segment
	    if ',' in segment:
		    return tuple([int(x) for x in segment.split(',')])
	    return int(segment)
