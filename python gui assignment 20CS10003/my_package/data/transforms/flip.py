#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.ft = flip_type

        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        if self.ft=="horizontal":            
            img = image.transpose(Image.FLIP_LEFT_RIGHT)
            #img.show()
            return img
        else:
            img = image.transpose(Image.FLIP_TOP_BOTTOM)
            #img.show()
            return img

# f = FlipImage("vertical")
# tImage = Image.open('C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/imgs/0.jpg')
# f(tImage)       