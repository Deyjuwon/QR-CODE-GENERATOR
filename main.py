import qrcode
from PIL import Image

data = input('Enter link to generate qr code: ')

qr = qrcode.QRCode(version=2, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill='black', back_color='green')

image.save('qrcode.png')
Image.open('qrcode.png')