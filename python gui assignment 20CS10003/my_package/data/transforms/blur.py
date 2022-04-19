#Imports
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius = 3):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

        # Write your code here
        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        #OriImage = Image.open('images/boy.jpg')
        OriImage = image
        #OriImage.show()

        #Applying GaussianBlur filter
        gaussImage = OriImage.filter(ImageFilter.GaussianBlur(self.radius))
        #gaussImage.show()
        return gaussImage

# b = BlurImage(5)
#tImage = Image.open('C:/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/imgs/0.jpg')
# b(tImage)

