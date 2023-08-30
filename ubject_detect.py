import cv2
import numpy as np
image=cv2.imread(r'your image location',0)    
templat=cv2.imread(r'your templat location',0)
                            #template should be like your subject you wanna detect
w,h=templat.shape
result=cv2.matchTemplate(image,templat,cv2.TM_CCOEFF_NORMED)                                        
threshuld=0.6
         #Sensitivity value
locate=np.where(result>=threshuld)
for point in zip(*locate[::-1]):
    cv2.rectangle(image,point,(point[0]+h,point[1]+w),(0.255,0),2)









cv2.imshow("birds",image)
cv2.waitKey(0)
cv2.destroyAllWindows()