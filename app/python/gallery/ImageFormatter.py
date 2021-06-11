#code taken from: https://crashlaker.github.io/python/2020/08/26/image_encode_decode_base64.html

import base64
import io
from PIL import Image

class ImageFormatter:
    
    def encode_img(self,filename):
        msg = b"<plain_txt_msg:img>"
        with open(filename, "rb") as imageFile:
            msg = msg + base64.b64encode(imageFile.read())
        msg = msg + b"<!plain_txt_msg>"
        return msg

    def decode_img(self,msg):
        msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):
                msg.find(b"<!plain_txt_msg>")]
        msg = base64.b64decode(msg)
        buf = io.BytesIO(msg)
        img = Image.open(buf)
        img.save("TE.jpg")
