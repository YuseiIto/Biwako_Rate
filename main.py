import cv2
import numpy as np

print("Biwako Area inspector")
print("©︎ Yusei ito 2020")
print("=========================")


print("Importing image..")
img = cv2.imread('./map.png')
height, width, channels = img.shape[:3]
print("Image Imported.")
print("\tWidth:"+str(width))
print("\tHeight:"+str(height))

count_max=50000
count_shiga=0
count_biwako=0

for i in range(0,count_max):
    px=img[np.random.randint(height),np.random.randint(width)]#Be attention. Array is formed as [y,x] and return is formed [blue,green,red]
    if (px[0]==0 and px[1]==38 and px[2]==255):
        count_shiga+=1
    if (px[0]==255 and px[1]==0 and px[2]==0):
        count_shiga+=1
        count_biwako+=1
    if (count_max%10==0):
        devisionBy=1 if count_shiga==0 else count_shiga
        print(str(i)+"\t"+str(count_biwako/devisionBy))


print("All Process succeed.\r\n\r\n")    
print("Attempt:"+str(count_max))
print("Shiga:"+str(count_shiga))
print("Biwako:"+str(count_biwako))

print("Overall Score:"+str(count_biwako/count_shiga))

