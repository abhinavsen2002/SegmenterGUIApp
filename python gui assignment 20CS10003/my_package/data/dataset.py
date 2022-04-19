#Imports
import json
#from Python_DS_Assignment.my_package.data.transforms.crop import CropImage
#from transforms import *
from my_package.data.transforms import CropImage, BlurImage, FlipImage, RescaleImage, RotateImage
import matplotlib.pylab as  plt

from numpy import asarray

from PIL import Image


class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None, imgPath = 'C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/imgs/'):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
            imgPath: the path in which images are stored. images should be stored with names 0.jpg, 1.jpg etc
        '''
        self.t = transforms
        self.imgPath = imgPath
        
        with open(annotation_file) as file:
            self.Imagedata = list(file)
        

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.Imagedata)

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: 
                image: image (in the form of a numpy array) (shape: (3, H, W))
                after all transforms have been done

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        '''
        data = json.loads(self.Imagedata[idx])
        idx = str(idx)
        tImage = Image.open(self.imgPath+idx+'.jpg')
        if self.t!=None:
            for i in self.t:                         
                tImage = i(tImage)
        #tImage.show()
        numpydata = asarray(tImage)
        numpydata = numpydata.transpose(2,1,0)
        numpydata = numpydata/255
        numpydata = numpydata.transpose(0, 2, 1)
        return numpydata





        