import pyqrcode
import png
from pyqrcode import QRCode

s = 'https://www.youtube.com/channel/UC011HYruWVTtCnnPOPj7tUA'
url = pyqrcode.create(s)
url.png('yutub.png', scale=10)