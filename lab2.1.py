import numpy as np
from PIL import Image

image = Image.open(input())

data = np.asarray(image)
mi=data.min()
ma=data.max()

sh=data.shape

n_data=np.zeros((sh[0],sh[1]),dtype='uint8')

for i in range(sh[0]):
    for j in range(sh[1]):
        n_data[i][j]=(data[i][j]-mi)*255/(ma-mi)//1

print(n_data)

res_img = Image.fromarray(n_data)
res_img.save(input())
#C:\Информатика\lunar01_raw.jpg