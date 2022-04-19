#Imports
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from my_package.data.transforms import BlurImage, FlipImage, RotateImage, CropImage, RescaleImage
from my_package.data import Dataset
from my_package import model
from numpy import asarray
import matplotlib.patches as patches

def plot_visualization(numpArray, path = 'C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/im1.png'): # Write the required arguments
  # saves the image with segmentation masks and bboxes separately in analysis1 folder
  
  s = model.InstanceSegmentationModel()
  # numpArray = numpArray.transpose(0, 2, 1)
  a1, a2, a3, a4 = s(numpArray)
  e2 = a2[0]
  for i in range (min(2,len(a2)-1)):
      e2+=a2[i+1]
  
  #c2 = c2/len(a2)
  n_min = e2.min(axis = (1,2), keepdims = True)
  n_max = e2.max(axis = (1,2), keepdims = True)  
  e2 = (e2-n_min)/(n_max-n_min)
  e2 = (7*e2+numpArray)/8
  e2 = (e2*255).astype(np.uint8)
  c2 = e2.transpose(1,2,0)
  numpArray = numpArray.transpose(1, 2, 0)
  # print(e2.shape)
  # im1 = Image.fromarray(d2[0], 'L')
  # im1.show()
  # print(a1)
  print(a3)
  # print(a4)
  #print((a1))
  boxes = []
  labels = []
  l = len(a1)
  for i in range(min(3,l)):
    max = np.argmax(a4)     #to get most confident prediction
    boxes.append(np.array(a1[max]))
    labels.append((a3[max]))
    a1.pop(max)
    a2.pop(max)
    a3.pop(max)
    a4.pop(max)
  path1 = path+"segmentation.png" 
  path2 = path+"bboxes.png" 
  #print(boxes)
  #print(labels)
  fig,ax = plt.subplots(1)
  ax.imshow(c2)
  plt.axis('off')
  plt.savefig(path1, bbox_inches = "tight" )
  # print(path1)
  #plt.show()
  
  fig,ax = plt.subplots(1)
  ax.imshow(numpArray/3)
  for i in range(min(3,l)):
    rect = patches.Rectangle(boxes[i][0], boxes[i][1][0]-boxes[i][0][0], boxes[i][1][1]-boxes[i][0][1], edgecolor = 'y', facecolor = 'none')
    plt.text(boxes[i][0][0], boxes[i][0][1], labels[i], fontsize = 12, color = 'w')
    ax.add_patch(rect)
  plt.axis('off')
  plt.savefig(path2, bbox_inches = "tight" )
  # print(path1)
  # plt.axis('off')
  # plt.savefig(path2,
  #             bbox_inches = "tight" )
  # plt.show()
  

  # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.