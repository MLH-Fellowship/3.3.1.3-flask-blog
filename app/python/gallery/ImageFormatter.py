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
        for row in range(int(image_info[0])):
            for column in range(int(image_info[1])):
                try:
                    r,g,b,_ = image_info[index].split(',')
                    r = int(r[1:])
                    g = int(g[1:])
                    b = int(b[1:-1]) if b[-1] == ')' else int(b[1:])
                
                    pixels[row,column] = (r,g,b)
                except Exception as E:
                    try:
                        r,g,b = image_info[index].split(',')
                        r = int(r[1:])
                        g = int(g[1:])
                        b = int(b[1:-1]) if b[-1] == ')' else int(b[1:])
                        pixels[row,column] = (r,g,b)

                    except Exception as E:
                        return self.pModeImage(msg)
                
                index += 1
        return img

    def pModeImage(self,msg):
        image_info = msg.split(';')
        img = Image.new('P', (int(image_info[0]), int(image_info[1])), color = 'white')
        pixels = img.load()
        index = 1
        for row in range(int(image_info[0])):
            for column in range(int(image_info[1])):
                index += 1
                pixels[row,column] = int(image_info[index])
        
        return img.convert('RGB')