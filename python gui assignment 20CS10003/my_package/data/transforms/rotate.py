#Imports
from PIL import Image
import PIL


class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        
        # Write your code here
        self.deg = degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        im1 = sample.rotate(self.deg, PIL.Image.NEAREST, expand = 1)
        #im1.show()
        return im1

# s = Image.open('C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/imgs/0.jpg')
# r = RotateImage(45)
# r(s)

