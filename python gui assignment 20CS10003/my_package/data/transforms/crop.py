#Imports
from PIL import Image


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, h, w, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)-->modified to h and w arguments
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.height = h
        self.width = w
        self.ct = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        self.w1, self.h1 = image.size
        #print(self.h1)
        #print(self.w1)
        if self.ct == 'center':
            bottom = self.h1/2+self.height/2
            top = self.h1/2-self.height/2
            left = self.w1/2-self.width/2
            right = self.w1/2+self.width/2
            im = image.crop((left, top, right, bottom))
            #im.show()
            return im
        #image = image.crop((100, 200, 200, 100))
        #image.show()
        elif self.ct == 'random':
            im = image.crop((0, 0, self.width, self.height))
            #im.show()
            return im

        

# s = Image.open('C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/imgs/0.jpg')
# r = CropImage(200,300, 'random')
# r(s)
        

 