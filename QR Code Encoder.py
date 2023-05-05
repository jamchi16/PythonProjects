import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)
img.save('C:/Users/james/OneDrive/Desktop/Tech Notes/Tech Project Files/myqrcode.png')