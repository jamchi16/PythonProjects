from PIL import Image

import glob

print(glob.glob("*.png"))

for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=95)



import os
for file in glob.glob("*.png"):
    os.remove(file)