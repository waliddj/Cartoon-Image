import cv2 as cv
import os

def BilateralFiltering(input_path,output_path):
    root = os.getcwd()
    imgPath = os.path.join(root,input_path) 
    img = cv.imread(imgPath,1)
    imgFilter = cv.bilateralFilter(img,33,90,200) #img,15,75,75 / img,5,20,20

    cv.imwrite(output_path,imgFilter)

if __name__ =='__main__':
    input_path_img = "IMG_0178 600x600 px.jpg"   #Input the image path
    output_path_img= "cartoon.jpg" #Input the output file name
    BilateralFiltering(input_path_img,output_path_img)

